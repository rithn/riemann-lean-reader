"""Draw the original archive's cluster import depths as SVG and PNG."""

from html import escape
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH, HEIGHT = 1000, 710
BACKGROUND = '#0b1225'
INK = '#f3f5ff'
MUTED = '#b7c2df'
CREDIT = 'RH Lean Explorer (riemannhypothesissolved.com) · CC BY 4.0'
SECTION = '/proof-in-numbers/#clusters-by-distance-from-the-main-theorem'
ASSET = '/proof-in-numbers/cluster-import-depth'
TITLE = 'Import depth in the original Lean archive'
FONTS = Path(__file__).resolve().parent / 'fonts'


def write_depth_figure(output, counts, cluster_median, file_median, files, site):
    """Use one layout for the editable vector and the 2× raster download."""
    total = sum(counts.values())
    shapes, labels = [], []

    def rect(x, y, width, height, fill):
        shapes.append((x, y, width, height, fill))

    def text(x, y, value, size=18, fill=MUTED, weight=400, align='start'):
        labels.append((x, y, str(value), size, fill, weight, align))

    rect(0, 0, WIDTH, HEIGHT, BACKGROUND)
    text(48, 60, TITLE, 37, INK, 700)
    text(48, 105, f'{total:,} clusters by shortest import distance from the cluster containing Main.lean', 19)
    text(48, 156, 'Import steps', 15, MUTED, 600)
    text(152, 156, 'Clusters', 15, MUTED, 600)

    x0, span = 152, 738
    step = max(1, 10 ** (len(str(max(counts.values()))) - 1) // 2)
    cap = (max(counts.values()) + step - 1) // step * step
    y0, stride = 184, 42
    for tick in range(0, cap + 1, step):
        x = x0 + tick / cap * span
        rect(x, y0 - 9, 1, len(counts) * stride + 1, '#303c57')
        text(x, y0 + len(counts) * stride + 10, f'{tick:,}', 14, align='middle')
    peak = max(counts, key=counts.get)
    for i, (depth, count) in enumerate(sorted(counts.items())):
        y = y0 + i * stride
        width = count / cap * span
        text(76, y + 17, depth, 19, INK, 600)
        rect(x0, y, width, 24, '#f5c46b' if depth == peak else '#8fa4f5')
        text(x0 + width + 11, y + 18, f'{count:,}', 18, INK, 700 if depth == peak else 500)

    text(48, 618, f'Cluster median: {cluster_median} steps ({total:,} clusters)', 19, INK, 600)
    text(508, 618, f'File median: {file_median} steps ({files:,} Lean files)', 19, INK, 600)
    rect(48, 641, WIDTH - 96, 1, '#303c57')
    text(48, 668, CREDIT, 15, MUTED, 600)
    text(48, 693, site + SECTION, 14)

    body = [f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="{fill}"/>'
            for x, y, w, h, fill in shapes]
    body += [f'<text x="{x:g}" y="{y:g}" font-size="{size}" fill="{fill}" font-weight="{weight}" '
             f'text-anchor="{align}">{escape(value)}</text>'
             for x, y, value, size, fill, weight, align in labels]
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
           f'viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">\n'
           f'<title id="title">{TITLE}</title>\n'
           f'<desc id="desc">{total:,} clusters. Depth and cluster counts: '
           + ', '.join(f'{depth}: {count:,}' for depth, count in sorted(counts.items()))
           + f'. Cluster median {cluster_median}; file median {file_median} across {files:,} files.</desc>\n'
           + '<g font-family="Inter, sans-serif">\n' + '\n'.join(body) + '\n</g>\n</svg>\n')
    target = Path(output) / ASSET.strip('/')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.with_suffix('.svg').write_text(svg, encoding='utf-8')

    scale = 2
    image = Image.new('RGB', (WIDTH * scale, HEIGHT * scale), BACKGROUND)
    draw = ImageDraw.Draw(image)
    for x, y, w, h, fill in shapes:
        left, top = round(x * scale), round(y * scale)
        right, bottom = round((x + w) * scale) - 1, round((y + h) * scale) - 1
        draw.rectangle((left, top, max(left, right), max(top, bottom)), fill=fill)
    fonts = {}
    for x, y, value, size, fill, weight, align in labels:
        key = size, weight
        if key not in fonts:
            font = ImageFont.truetype(str(FONTS / 'Inter.ttf'), size * scale)
            font.set_variation_by_axes([weight])
            fonts[key] = font
        draw.text((x * scale, y * scale), value, fill=fill, font=fonts[key],
                  anchor='ms' if align == 'middle' else 'ls')
    image.save(target.with_suffix('.png'), optimize=True)
