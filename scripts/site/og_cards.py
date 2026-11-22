"""Share cards: one 1200x630 PNG per cluster and theme, the og:image / twitter:image of its static page.

usage (build_site.py runs this; it needs Pillow: add --with pillow to the uv run command):
  python -I og_cards.py <jobs.json>
jobs.json: {"out": <site dir>, "jobs": [{"path": "og/c/k0677.png", "key": <content hash>, ...card fields}]}

A card is re-rendered only when its key (a hash of everything drawn on it, the fonts and CARD_V) differs from the key
stored in the existing PNG's text chunk, so an unchanged map costs one header read per card. Rendering runs in a few
processes. The PNGs are palette images (256 colours), about 25-45 KB each.
"""
import os, sys, json, math, colorsys
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, 'fonts')
W, H = 1200, 630
BG0, BG1 = (5, 8, 21), (11, 18, 48)
FG, FG2, MUTE, GOLD, ACC2 = (233, 237, 255), (195, 203, 239), (139, 150, 194), (245, 196, 107), (180, 193, 255)
_F = {}
QN, QD = 256, 0   # palette size; dithering (QD) makes the files 4x bigger


def font(kind, size):
    from PIL import ImageFont
    k = (kind, size)
    if k not in _F:
        if kind == 'serif':
            f = ImageFont.truetype(os.path.join(FONTS, 'Fraunces.ttf'), size)
            f.set_variation_by_axes([min(144, size), 600, 0, 0])     # opsz, wght, SOFT, WONK
        else:
            f = ImageFont.truetype(os.path.join(FONTS, 'Inter.ttf'), size)
            f.set_variation_by_axes([min(32, max(14, size)), {'reg': 400, 'med': 500, 'semi': 600}[kind]])
        _F[k] = f
    return _F[k]


def rgb(hue, l):   # the site's field colour, hsla(hue, 80%, l%)
    r, g, b = colorsys.hls_to_rgb(hue / 360, l / 100, .8)
    return round(r * 255), round(g * 255), round(b * 255)


def wrap(d, text, f, width, lines):
    """Greedy word wrap into at most `lines` lines; None if it does not fit."""
    out, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= width:
            cur = t
        else:
            if not cur or d.textlength(w, font=f) > width:
                return None
            out.append(cur); cur = w
    out.append(cur)
    return out if len(out) <= lines else None


def clip1(d, text, f, width):
    if d.textlength(text, font=f) <= width:
        return text
    while text and d.textlength(text + '…', font=f) > width:
        text = text[:-1]
    return text.rstrip(' ,·–-') + '…'


def mix(a, b, t):   # t of colour a over colour b
    return tuple(round(x * t + y * (1 - t)) for x, y in zip(a, b))


def background(col, seed):
    from PIL import Image, ImageDraw
    g = Image.new('RGB', (2, 2)); g.putdata([BG0, BG1, BG1, BG0])      # diagonal navy gradient, smooth after the resize
    img = g.resize((W, H), Image.BICUBIC)
    d = ImageDraw.Draw(img)
    r = seed
    for i in range(70):                      # a few faint stars, the same for the same card
        r = (r * 1103515245 + 12345) & 0x7fffffff; x = r % W
        r = (r * 1103515245 + 12345) & 0x7fffffff; y = r % H
        r = (r * 1103515245 + 12345) & 0x7fffffff; a = 40 + r % 90
        d.point((x, y), fill=tuple(min(255, c + a // 2) for c in BG1))
    # the field colour: a bar down the left edge and faint rings around the bottom-right corner (the /route/ rings)
    d.rectangle((0, 0, 9, H), fill=col)
    for i, rr in enumerate((210, 330, 450, 570)):
        d.ellipse((W - 70 - rr, H + 40 - rr, W - 70 + rr, H + 40 + rr), outline=mix(col, BG1, .34 - .07 * i), width=2)
    return img


def star(d, cx, cy, R, fill):
    pts = [(cx + (R if j % 2 == 0 else R * .45) * math.cos(-math.pi / 2 + j * math.pi / 5),
            cy + (R if j % 2 == 0 else R * .45) * math.sin(-math.pi / 2 + j * math.pi / 5)) for j in range(10)]
    d.polygon(pts, fill=fill)


def glyph(d, x, cy, dd, col, s=2.6):
    """The route glyph of the site (route_glyph() in build_site.py), scaled by s; returns its right edge."""
    parts = ['star'] if dd == 0 else (['dot'] * dd if dd <= 3 else ['dot', 'dot', 'gap', 'num']) + ['star']
    wd, G = {'dot': 7, 'gap': 10, 'num': 15, 'star': 14}, 5
    for i, p in enumerate(parts):
        if i:
            d.line((x, cy, x + G * s, cy), fill=tuple(int(c * .6 + b * .4) for c, b in zip(col, BG1)), width=max(2, round(1.4 * s * .8))); x += G * s
        cx = x + wd[p] * s / 2
        if p == 'dot':
            r = 3.2 * s; d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col)
        elif p == 'gap':
            for o in (-3.2, 0, 3.2):
                r = 1.1 * s; d.ellipse((cx + o * s - r, cy - r, cx + o * s + r, cy + r), fill=col)
        elif p == 'num':
            r = 6.8 * s; d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=col, width=round(1.3 * s))
            d.text((cx, cy + 1), str(dd), font=font('semi', round((7.5 if dd > 9 else 9) * s)), fill=col, anchor='mm')
        else:
            star(d, cx, cy, 6.8 * s, GOLD)
        x += wd[p] * s
    return x


_LOGO = []
def logo():   # the site's logo (logo.png in the site), round, 56 px, at the top left
    from PIL import Image, ImageDraw
    if not _LOGO:
        im = Image.open(os.path.join(OUT, 'logo.png')).convert('RGB').resize((56, 56), Image.LANCZOS)
        m = Image.new('L', (224, 224), 0); ImageDraw.Draw(m).ellipse((0, 0, 223, 223), fill=255)
        _LOGO.extend([im, (72, 57), m.resize((56, 56), Image.LANCZOS)])
    return _LOGO


def render(job):
    from PIL import Image, ImageDraw, PngImagePlugin
    col = rgb(job['hue'], job['l'])
    img = background(col, int(job['key'][:8], 16))
    d = ImageDraw.Draw(img)
    L, R = 72, W - 72
    # header: the logo, the site name, the cluster or theme id
    img.paste(*logo())
    d.text((L + 70, 84), 'RH Lean Explorer', font=font('med', 26), fill=FG2, anchor='lm')
    d.text((R, 84), job['tag'], font=font('med', 24), fill=MUTE, anchor='rm')
    # eyebrow: field and theme, in the field colour
    y = 168
    d.ellipse((L, y - 8, L + 16, y + 8), fill=col)
    d.text((L + 30, y), clip1(d, job['eyebrow'], font('semi', 28), R - L - 30), font=font('semi', 28), fill=col, anchor='lm')
    # title: serif, wrapped, as large as fits in four lines
    for size in (74, 68, 62, 56, 50, 46, 42):
        lines = wrap(d, job['title'], font('serif', size), R - L, 4 if size < 62 else 3)
        if lines:
            break
    else:
        size = 42; lines = wrap(d, job['title'], font('serif', size), R - L, 99)[:4]; lines[-1] = clip1(d, lines[-1] + ' …', font('serif', size), R - L)
    lh = round(size * 1.16)
    ty = 214 + max(0, (4 * 50 - len(lines) * lh) // 4)
    for i, t in enumerate(lines):
        d.text((L, ty + i * lh), t, font=font('serif', size), fill=FG)
    # footer: the route glyph and its words, then the domain
    fy = H - 92
    if job.get('d') is not None:
        x = glyph(d, L, fy, job['d'], col)
        d.text((x + 18, fy), job['route'], font=font('med', 28), fill=FG2, anchor='lm')
    elif job.get('route'):
        d.text((L, fy), job['route'], font=font('med', 28), fill=FG2, anchor='lm')
    d.line((L, H - 54, R, H - 54), fill=(30, 40, 80), width=1)
    d.text((L, H - 30), 'riemannhypothesissolved.com', font=font('med', 24), fill=ACC2, anchor='lm')
    d.text((R, H - 30), 'Map of the Lean proof of the Riemann hypothesis', font=font('reg', 22), fill=MUTE, anchor='rm')
    pal = img.quantize(QN, method=Image.Quantize.MEDIANCUT)
    img = img.quantize(palette=pal, dither=Image.Dither(QD)) if QD else pal
    meta = PngImagePlugin.PngInfo(); meta.add_text('rhkey', job['key'])
    out = os.path.join(OUT, job['path'])
    tmp = out + '.tmp'
    img.save(tmp, 'PNG', optimize=True, pnginfo=meta)
    os.replace(tmp, out)
    return job['path']


def stale(job):
    from PIL import Image
    try:
        with Image.open(os.path.join(OUT, job['path'])) as im:
            return im.text.get('rhkey') != job['key']
    except Exception:
        return True


OUT = None
def _init(out):
    global OUT
    OUT = out


if __name__ == '__main__':
    spec = json.load(open(sys.argv[1]))
    _init(spec['out'])
    jobs = spec['jobs']
    for j in jobs:
        os.makedirs(os.path.dirname(os.path.join(OUT, j['path'])), exist_ok=True)
    todo = [j for j in jobs if stale(j)]
    if todo:
        n = min(6, os.cpu_count() or 2)
        with ProcessPoolExecutor(n, initializer=_init, initargs=(OUT,)) as ex:
            list(ex.map(render, todo, chunksize=16))
    print(f'share cards: {len(jobs)} cards, {len(todo)} rendered, {len(jobs) - len(todo)} unchanged')
