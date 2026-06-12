#!/usr/bin/env python3
"""
freundcloud logo + favicon generator.

A NixOS-style six-arm snowflake sitting inside a cloud, in the site's
terminal-green palette (--accent #00ff88 on black). Emits two SVGs:

  favicon.svg        transparent, logo fills the canvas (modern tab icon)
  favicon-tile.svg   padded logo on a rounded black tile (iOS / PWA / maskable)

Raster outputs (.png/.ico) are produced from these by the sibling shell
step using rsvg-convert + ImageMagick. Re-run this to regenerate the mark.
"""

import math

# ---- brand palette (from _sass/theme.scss :root) -------------------------
ACCENT = "#00ff88"  # --accent
ACCENT_DIM = "#00b860"  # --accent-dim
INK = "#04140a"  # near-black green for the snowflake on the cloud
BG = "#000000"  # --bg (tile background)

VB = 64  # viewBox is 0 0 64 64


# ---- snowflake -----------------------------------------------------------
def snowflake(cx, cy, R, w_arm, w_branch, color):
    """Six-arm snowflake centred at (cx,cy), arm radius R."""
    arms, branches = [], []
    for k in range(6):
        th = math.radians(-90 + 60 * k)  # -90deg => first arm points up
        dx, dy = math.cos(th), math.sin(th)  # SVG y is downward
        tx, ty = cx + R * dx, cy + R * dy  # arm tip
        arms.append(f'<line x1="{cx:.2f}" y1="{cy:.2f}" x2="{tx:.2f}" y2="{ty:.2f}"/>')
        # two outward chevron branches at 60% of the arm
        px, py = cx + 0.58 * R * dx, cy + 0.58 * R * dy
        bl = 0.32 * R
        for sign in (+1, -1):
            bth = th + sign * math.radians(58)
            bx, by = px + bl * math.cos(bth), py + bl * math.sin(bth)
            branches.append(
                f'<line x1="{px:.2f}" y1="{py:.2f}" x2="{bx:.2f}" y2="{by:.2f}"/>'
            )
    return (
        f'<g fill="none" stroke="{color}" stroke-linecap="round" stroke-linejoin="round">'
        f'<g stroke-width="{w_arm}">' + "".join(arms) + "</g>"
        f'<g stroke-width="{w_branch}">' + "".join(branches) + "</g>"
        f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{w_arm * 0.9:.2f}" fill="{color}" stroke="none"/>'
        f"</g>"
    )


# ---- cloud ---------------------------------------------------------------
def cloud(fill):
    """Seamless cloud silhouette: overlapping shapes sharing one fill."""
    parts = [
        '<rect x="12" y="36.5" width="40" height="9.5" rx="4.75"/>',
        '<circle cx="20" cy="38" r="9"/>',
        '<circle cx="30.5" cy="30.5" r="12"/>',
        '<circle cx="44" cy="37" r="10"/>',
        '<circle cx="40" cy="28" r="8"/>',
    ]
    return f'<g fill="{fill}">' + "".join(parts) + "</g>"


DEFS = (
    "<defs>"
    f'<linearGradient id="cloudg" x1="14" y1="18" x2="50" y2="46" gradientUnits="userSpaceOnUse">'
    f'<stop offset="0" stop-color="{ACCENT}"/>'
    f'<stop offset="1" stop-color="{ACCENT_DIM}"/>'
    "</linearGradient>"
    '<filter id="glow" x="-40%" y="-40%" width="180%" height="180%">'
    '<feGaussianBlur stdDeviation="1.1" result="b"/>'
    '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>'
    "</filter>"
    "</defs>"
)


def mark(glow=True):
    g = ' filter="url(#glow)"' if glow else ""
    return (
        f"<g{g}>"
        + cloud("url(#cloudg)")
        + snowflake(30.5, 33.0, 10.0, 2.5, 1.7, INK)
        + "</g>"
    )


def svg_transparent():
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VB} {VB}" '
        f'width="{VB}" height="{VB}" role="img" aria-label="freundcloud">'
        + DEFS
        + mark(glow=True)
        + "</svg>"
    )


def svg_tile():
    # logo scaled to ~78% and centred on a rounded black tile
    s = 0.80
    off = (VB - VB * s) / 2
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VB} {VB}" '
        f'width="{VB}" height="{VB}" role="img" aria-label="freundcloud">'
        + DEFS
        + f'<rect width="{VB}" height="{VB}" rx="13" fill="{BG}"/>'
        + f'<g transform="translate({off:.2f} {off:.2f}) scale({s})">'
        + mark(glow=True)
        + "</g>"
        + "</svg>"
    )


if __name__ == "__main__":
    import pathlib

    here = pathlib.Path(__file__).resolve().parent
    out = here.parent  # assets/img/
    (out / "favicon.svg").write_text(svg_transparent() + "\n")
    (here / "favicon-tile.svg").write_text(svg_tile() + "\n")
    print("wrote", out / "favicon.svg")
    print("wrote", here / "favicon-tile.svg")
