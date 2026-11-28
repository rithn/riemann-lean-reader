"""Render the publication's reviewed prose formulas before writing HTML."""

from html import escape, unescape
import json
from pathlib import Path
import re
import subprocess


# Spellings from the article drafts, learning path and reading notes. Keep the
# source text for Markdown, previews and content revision hashes.
FORMULAS = {
    "ζ(s) = 1 + 1/2^s + 1/3^s + 1/4^s + …": r"\zeta(s)=1+\frac{1}{2^s}+\frac{1}{3^s}+\frac{1}{4^s}+\cdots",
    "1 + 1/2^s + 1/3^s + ...": r"1+\frac{1}{2^s}+\frac{1}{3^s}+\cdots",
    "ζ(s) = ∏ over primes p of 1 / (1 − p^(−s))": r"\zeta(s)=\prod_{p\ \mathrm{prime}}\frac{1}{1-p^{-s}}",
    "ζ(s) = Σ 1/n^s": r"\zeta(s)=\sum_n\frac{1}{n^s}",
    "L(χ, s) = Σ χ(n)/n^s": r"L(\chi,s)=\sum_n\frac{\chi(n)}{n^s}",
    "ζ(s) = 2 (2π)^(s-1) Γ(1-s) cos(π(1-s)/2) ζ(1-s)": r"\zeta(s)=2(2\pi)^{s-1}\Gamma(1-s)\cos(\pi(1-s)/2)\zeta(1-s)",
    "ζ(1-s) = 2 (2π)^(-s) Γ(s) cos(πs/2) ζ(s)": r"\zeta(1-s)=2(2\pi)^{-s}\Gamma(s)\cos(\pi s/2)\zeta(s)",
    "π(x) = Li(x) + O(√x log x)": r"\pi(x)=\operatorname{Li}(x)+O(\sqrt{x}\log x)",
    "σ(n) < e^γ n log log n": r"\sigma(n)<e^\gamma n\log\log n",
    "0 < Re s < 1": r"0<\operatorname{Re}(s)<1",
    "0 < Re(s) < 1": r"0<\operatorname{Re}(s)<1",
    "1 < Re(s)": r"1<\operatorname{Re}(s)",
    "re s ≤ 1": r"\operatorname{Re}(s)\le1",
    "Re(1-s) > 1/2": r"\operatorname{Re}(1-s)>\tfrac12",
    "Re > 1/2": r"\operatorname{Re}>\tfrac12",
    "L(χ, s) ≠ 0": r"L(\chi,s)\ne0",
    "L(s, χ) ≠ 0": r"L(s,\chi)\ne0",
    "L(χ, s) = 0": r"L(\chi,s)=0",
    "L(s, χ) = 0": r"L(s,\chi)=0",
    "L(s, χ)": r"L(s,\chi)",
    "L(χ, s)": r"L(\chi,s)",
    "L(χ̄, s)": r"L(\bar\chi,s)",
    "ζ(s) = 0": r"\zeta(s)=0",
    "ζ(1-s) = 0": r"\zeta(1-s)=0",
    "ζ ≠ 0": r"\zeta\ne0",
    "ζ(s)": r"\zeta(s)",
    "χ mod N": r"\chi\bmod N",
    "s = σ + it": r"s=\sigma+it",
    "s = -2, -4, -6, …": r"s=-2,-4,-6,\ldots",
    "¬∃ n : ℕ, s = -2 * (n + 1)": r"\nexists n\in\mathbb{N},\ s=-2(n+1)",
    "s = 1": "s=1",
    "s ≠ 1": r"s\ne1",
    "s = 0": "s=0",
    "N ≥ 1": r"N\ge1",
    "N = 1": "N=1",
    "σ > 1": r"\sigma>1",
    "n > 5040": "n>5040",
    "n > 0": "n>0",
    "χ = 1": r"\chi=1",
    "½ + it": r"\tfrac12+it",
    "1/2 + it": r"\tfrac12+it",
}
for written in ('Re s', 'Re(s)'):
    for operator, tex_op in [('=', '='), ('>', '>'), ('<', '<'), ('≥', r'\ge '), ('≤', r'\le ')]:
        for bound, tex_bound in [('0', '0'), ('1', '1'), ('½', r'\tfrac12'), ('1/2', r'\tfrac12')]:
            FORMULAS[f'{written} {operator} {bound}'] = rf'\operatorname{{Re}}(s){tex_op}{tex_bound}'

DISPLAY = {
    "ζ(s) = 1 + 1/2^s + 1/3^s + 1/4^s + …",
    "ζ(s) = ∏ over primes p of 1 / (1 − p^(−s))",
}
CODE = re.compile(r'<code\b[^>]*>([^<]+)</code>\Z', re.I)
TAGS = re.compile(r'(<svg\b[^>]*>.*?</svg>|<(?:pre|script)\b[^>]*>.*?</(?:pre|script)>|<code\b[^>]*>.*?</code>|<[^>]+>)', re.I | re.S)


class MathMarkup:
    def __init__(self, vendor):
        requests = sorted({(formula, written in DISPLAY) for written, formula in FORMULAS.items()})
        node_program = """
const fs = require('node:fs');
const katex = require(process.argv[1]);
const formulas = JSON.parse(fs.readFileSync(0, 'utf8'));
console.log(JSON.stringify(formulas.map(([tex, displayMode]) =>
  katex.renderToString(tex, {displayMode, output: 'htmlAndMathml', strict: 'error', throwOnError: true}))));
"""
        try:
            response = subprocess.run(['node', '-e', node_program, str(vendor / 'katex.min.js')],
                                      input=json.dumps(requests), capture_output=True, text=True, check=True)
        except FileNotFoundError as error:
            raise RuntimeError('Node.js must be on PATH to render the site maths') from error
        except subprocess.CalledProcessError as error:
            raise RuntimeError(error.stderr) from error
        rendered = dict(zip(requests, json.loads(response.stdout), strict=True))
        self.markup = {escape(text, quote=False): rendered[formula, text in DISPLAY]
                       for text, formula in FORMULAS.items()}
        options = '|'.join(re.escape(text) for text in sorted(self.markup, key=len, reverse=True))
        self.prose_pattern = re.compile(r'(?<![\w/])(?:' + options + r')(?![\w/]|[.,]\d)')

    def text(self, escaped):
        return self.prose_pattern.sub(lambda match: self.markup[match[0]], escaped)

    def html(self, html):
        # Render an entire code span only when its text is a reviewed formula.
        # Leave fenced code and Lean declarations as literal source.
        chunks = TAGS.split(html)
        for index, chunk in enumerate(chunks):
            if index % 2 == 0:
                chunks[index] = self.text(chunk)
            elif match := CODE.fullmatch(chunk):
                key = escape(unescape(match[1]), quote=False)
                chunks[index] = self.markup.get(key, chunk)
        return ''.join(chunks)
