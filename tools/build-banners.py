#!/usr/bin/env python3
"""Собирает banner-light.svg и banner-dark.svg в палитре сайта samuray4ik04.github.io."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

THEMES = {
    "light": {
        "paper": "#f6f5ed", "frame": "#dcded2", "ink": "#263f37", "muted": "#626d62",
        "accent": "#315b49", "honey": "#dec28c", "mint": "#aed8c1",
        "glow_left": "#f0dfbb", "glow_right": "#d0e7d7",
        "arch_honey": ("#f4e4c4", "#e7c98d"), "arch_mint": ("#d9ebcb", "#90c7ac"),
        "card": "#fffaf0", "kanji": "#ffffff",
    },
    "dark": {
        "paper": "#122c27", "frame": "#3b5447", "ink": "#edf3df", "muted": "#b1c7b8",
        "accent": "#b2dfbe", "honey": "#d5bc87", "mint": "#a6dcc0",
        "glow_left": "#394632", "glow_right": "#285b49",
        "arch_honey": ("#6e6240", "#a88d52"), "arch_mint": ("#2c5a4a", "#4d8f76"),
        "card": "#1c3830", "kanji": "#edf3df",
    },
}

SPARKS = [  # x, y, размер, символ, задержка
    (560, 58, 30, "✦", 0), (905, 300, 22, "✧", 1.3), (470, 296, 18, "✦", 2.1),
]


def arch(x, y, tilt, gradient_id, colors, kanji, label, symbol, t):
    top, bottom = colors
    return f"""
  <g transform="translate({x} {y}) rotate({tilt})">
    <animateTransform attributeName="transform" type="translate" additive="sum"
      values="0 0; 0 -6; 0 0" dur="6s" begin="{0 if tilt < 0 else -3}s" repeatCount="indefinite"/>
    <linearGradient id="{gradient_id}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/>
    </linearGradient>
    <path d="M-72,95 V-40 A72,72 0 0 1 72,-40 V95 Q72,105 62,105 H-62 Q-72,105 -72,95 Z"
      fill="{t['card']}" stroke="{t['frame']}"/>
    <path d="M-64,62 V-38 A64,64 0 0 1 64,-38 V62 Z" fill="url(#{gradient_id})"/>
    <text x="40" y="-30" font-family="serif" font-size="30" fill="{t['kanji']}" fill-opacity="0.6"
      writing-mode="tb" letter-spacing="2">{kanji}</text>
    <text x="0" y="22" text-anchor="middle" font-size="42" fill="{t['kanji']}" fill-opacity="0.85">{symbol}</text>
    <text x="-60" y="89" font-family="Georgia, serif" font-size="16" font-style="italic"
      font-weight="600" fill="{t['ink']}">{label}</text>
  </g>"""


def banner(t):
    sparks = "".join(
        f"""
  <text x="{x}" y="{y}" font-size="{s}" fill="{t['accent']}">{c}<animate attributeName="opacity"
    values="1;0.25;1" dur="3.2s" begin="{d}s" repeatCount="indefinite"/></text>"""
        for x, y, s, c, d in SPARKS
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 340" width="960" height="340" role="img" aria-label="Samuray43k — лютый вайбкодер">
  <defs>
    <radialGradient id="glowLeft"><stop offset="0" stop-color="{t['glow_left']}"/><stop offset="1" stop-color="{t['glow_left']}" stop-opacity="0"/></radialGradient>
    <radialGradient id="glowRight"><stop offset="0" stop-color="{t['glow_right']}"/><stop offset="1" stop-color="{t['glow_right']}" stop-opacity="0"/></radialGradient>
    <clipPath id="typeClip">
      <rect x="62" y="228" width="0" height="34">
        <animate attributeName="width" from="0" to="342" dur="1.6s" begin="0.5s" fill="freeze"/>
      </rect>
    </clipPath>
  </defs>

  <rect x="1.5" y="1.5" width="957" height="337" rx="24" fill="{t['paper']}" stroke="{t['frame']}" stroke-width="3"/>
  <circle cx="690" cy="120" r="230" fill="url(#glowLeft)" opacity="0.8"/>
  <circle cx="900" cy="200" r="210" fill="url(#glowRight)" opacity="0.8"/>
  <ellipse cx="770" cy="175" rx="190" ry="120" fill="none" stroke="{t['frame']}" transform="rotate(-20 770 175)"/>

  <text x="64" y="72" font-family="ui-monospace, Consolas, Menlo, monospace" font-size="13"
    letter-spacing="3" fill="{t['muted']}">● PERSONAL SPACE / 043</text>

  <text x="60" y="158" font-family="Georgia, 'Times New Roman', serif" font-size="84"
    font-weight="600" letter-spacing="-2" fill="{t['ink']}">Samuray<tspan font-style="italic"
    fill="{t['accent']}">43k</tspan><tspan font-size="46" dy="-30" fill="{t['honey']}"> ✳</tspan></text>

  <text x="64" y="196" font-family="Georgia, serif" font-style="italic" font-size="21"
    fill="{t['muted']}">немного кода, немного аниме</text>

  <g font-family="ui-monospace, Consolas, Menlo, monospace" font-size="19">
    <text x="64" y="252" clip-path="url(#typeClip)"><tspan fill="{t['accent']}">$ whoami</tspan><tspan
      fill="{t['ink']}" xml:space="preserve">  →  лютый вайбкодер</tspan></text>
    <rect x="394" y="235" width="10" height="22" fill="{t['honey']}">
      <animate attributeName="opacity" values="1;1;0;0;1" keyTimes="0;0.45;0.5;0.95;1" dur="1.1s" repeatCount="indefinite"/>
    </rect>
  </g>

  <text x="64" y="304" font-family="ui-monospace, Consolas, Menlo, monospace" font-size="12"
    letter-spacing="2.5" fill="{t['muted']}">a little sunshine. a little spirit.</text>
{arch(690, 150, -8, "archHoney", t["arch_honey"], "真昼", "Mahiru", "☀", t)}
{arch(840, 178, 8, "archMint", t["arch_mint"], "藿藿", "Huohuo", "✧", t)}
{sparks}
</svg>
"""


for name, theme in THEMES.items():
    (ROOT / f"banner-{name}.svg").write_text(banner(theme), encoding="utf-8")
    print(f"banner-{name}.svg")
