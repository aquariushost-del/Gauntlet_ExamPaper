#!/usr/bin/env python3
"""Deterministic greyscale exam figures for 5086 Lenses topical paper."""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyArrowPatch, FancyBboxPatch, Rectangle
from matplotlib.lines import Line2D

OUT = Path("/workspace/exam-paper-lenses/figures")
OUT.mkdir(parents=True, exist_ok=True)

# Print-safe settings
DPI = 300
LW = 1.35
LW_THIN = 0.95
FONT = {"fontsize": 10, "fontname": "DejaVu Sans"}


def save(fig, name: str, w_in: float, h_in: float):
    fig.set_size_inches(w_in, h_in)
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight", pad_inches=0.08, facecolor="white")
    plt.close(fig)
    print("wrote", name)


def draw_thin_lens(ax, x, y0, y1, bulge=0.35):
    """Biconvex lens outline centred at x spanning y0..y1."""
    h = y1 - y0
    cy = (y0 + y1) / 2
    # left and right arcs
    theta1, theta2 = 90, 270
    # Use two arcs approximating thin lens
    r = h / 2
    # Left surface (centre to the right of x)
    ax.add_patch(Arc((x + bulge, cy), 2 * bulge * 2, h, theta1=90, theta2=270, lw=LW, color="k"))
    ax.add_patch(Arc((x - bulge, cy), 2 * bulge * 2, h, theta1=270, theta2=90, lw=LW, color="k"))
    # top/bottom join ticks
    ax.plot([x - 0.02, x + 0.02], [y1, y1], "k", lw=LW)
    ax.plot([x - 0.02, x + 0.02], [y0, y0], "k", lw=LW)


def lens_simple(ax, x, ymin, ymax):
    """Simple exam-style thin lens (two arcs)."""
    cy = 0.5 * (ymin + ymax)
    h = ymax - ymin
    w = 0.55
    ax.add_patch(Arc((x + w * 0.15, cy), w, h, angle=0, theta1=90, theta2=270, lw=LW, color="k"))
    ax.add_patch(Arc((x - w * 0.15, cy), w, h, angle=0, theta1=270, theta2=90, lw=LW, color="k"))


def arrow_ray(ax, x0, y0, x1, y1, style="-"):
    ax.annotate(
        "",
        xy=(x1, y1),
        xytext=(x0, y0),
        arrowprops=dict(arrowstyle="-|>", color="k", lw=LW_THIN, mutation_scale=10),
    )


def fig_q1_options():
    """Four panels: which shows converging action on parallel rays."""
    fig, axes = plt.subplots(2, 2)
    labels = ["A", "B", "C", "D"]
    for ax, lab, mode in zip(axes.ravel(), labels, ["diverge", "converge", "centre", "straight"]):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.axhline(3, color="k", lw=0.6, ls="--")
        lens_simple(ax, 5, 0.8, 5.2)
        # three parallel rays approaching
        ys = [1.6, 3.0, 4.4]
        for y in ys:
            ax.plot([0.5, 5], [y, y], "k", lw=LW_THIN)
            ax.annotate("", xy=(4.7, y), xytext=(4.2, y), arrowprops=dict(arrowstyle="-|>", color="k", lw=0.7, mutation_scale=8))
        if mode == "converge":
            for y in ys:
                ax.plot([5, 8.2], [y, 3.0], "k", lw=LW_THIN)
            ax.plot(8.2, 3.0, "ko", ms=3)
            ax.text(8.2, 2.3, "F", **FONT)
        elif mode == "diverge":
            for y, ye in zip(ys, [0.6, 3.0, 5.4]):
                ax.plot([5, 9], [y, ye], "k", lw=LW_THIN)
        elif mode == "centre":
            for y in ys:
                ax.plot([5, 5.2], [y, 3.0], "k", lw=LW_THIN)
            ax.plot(5.2, 3.0, "ko", ms=3)
        else:
            for y in ys:
                ax.plot([5, 9.5], [y, y], "k", lw=LW_THIN)
        ax.text(0.3, 5.5, lab, fontsize=12, fontweight="bold", fontname="DejaVu Sans")
    save(fig, "fig_q1_options.png", 5.2, 4.0)


def fig_q3_labels():
    """Unique principal focus A: two parallel rays shown meeting at A after the lens."""
    fig, ax = plt.subplots()
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.axhline(3, color="k", lw=0.7, ls="--")
    lens_simple(ax, 6, 0.7, 5.3)
    # Parallel rays → meet at A (principal focus)
    for y in (1.8, 4.2):
        ax.plot([0.6, 6], [y, y], "k", lw=0.8)
        ax.plot([6, 9.0], [y, 3.0], "k", lw=0.8)
    ax.plot(9.0, 3, "ko", ms=4)
    ax.text(9.0, 2.2, "A", **FONT)
    # B = optical centre
    ax.plot(6, 3, "ko", ms=4)
    ax.text(5.55, 2.2, "B", **FONT)
    # C = rim point
    ax.plot(6.0, 5.0, "ko", ms=4)
    ax.text(6.25, 5.15, "C", **FONT)
    # D = point on lens mid-way up (not on axis) — not a focus
    ax.plot(6.35, 4.0, "ko", ms=4)
    ax.text(6.6, 4.05, "D", **FONT)
    ax.text(0.4, 5.5, "principal axis", fontsize=9, fontname="DejaVu Sans")
    save(fig, "fig_q3_labels.png", 5.0, 2.4)


def fig_q4_image():
    """Exact thin-lens ray geometry: parallel→F and through O meet at image tip."""
    fig, ax = plt.subplots()
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.axhline(4.0, color="k", lw=0.7, ls="--")
    lens_x, axis_y, f = 8.0, 4.0, 3.0
    lens_simple(ax, lens_x, 1.0, 7.0)
    ax.plot(lens_x - f, axis_y, "ko", ms=3)
    ax.text(lens_x - f, axis_y - 0.55, "F", fontsize=9)
    ax.plot(lens_x + f, axis_y, "ko", ms=3)
    ax.text(lens_x + f, axis_y - 0.55, "F", fontsize=9)
    # object tip (1, 6); height 2.0 above axis
    ox, oy = 1.0, 6.0  # height 2.0 above axis_y=4
    ax.annotate("", xy=(ox, oy), xytext=(ox, axis_y), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.4, mutation_scale=12))
    ax.text(ox - 0.7, oy + 0.2, "O", **FONT)
    # Exact parallel→F and through-O intersection with axis_y=4, f=3: (13.25, 2.5)
    ix, iy = 13.25, 2.5
    ax.annotate("", xy=(ix, iy), xytext=(ix, axis_y), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.4, mutation_scale=12))
    ax.text(ix + 0.25, iy - 0.35, "I", **FONT)
    # Ray 1: parallel then through F_right
    ax.plot([ox, lens_x], [oy, oy], "k", lw=0.8)
    ax.plot([lens_x, ix], [oy, iy], "k", lw=0.8)
    # Ray 2: through optical centre
    ax.plot([ox, ix], [oy, iy], "k", lw=0.8)
    save(fig, "fig_q4_image.png", 5.4, 2.8)


def fig_q6_context():
    """More recognisable stamp + eye line art (still greyscale exam style)."""
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_aspect("equal")
    ax.axis("off")
    # stamp with perforated border and simple motif
    ax.add_patch(Rectangle((1.0, 1.3), 2.6, 3.0, fill=False, lw=LW))
    for yy in [1.3, 4.3]:
        for x in [1.15 + 0.35 * i for i in range(7)]:
            ax.add_patch(Circle((x, yy), 0.08, fill=False, lw=0.6))
    ax.add_patch(Circle((2.3, 3.2), 0.55, fill=False, lw=0.9))
    ax.plot([1.4, 3.2], [2.0, 2.0], "k", lw=0.7)
    ax.plot([1.4, 3.2], [1.7, 1.7], "k", lw=0.7)
    ax.text(1.55, 4.55, "stamp", fontsize=8)
    lens_simple(ax, 5.2, 1.2, 4.6)
    ax.text(4.55, 5.15, "reading lens", fontsize=8)
    # eye: almond outline + iris + pupil + lashes hint
    ex, ey = 8.2, 3.0
    ax.add_patch(Arc((ex, ey), 1.6, 0.9, theta1=0, theta2=180, lw=LW))
    ax.add_patch(Arc((ex, ey), 1.6, 0.9, theta1=180, theta2=360, lw=LW))
    ax.add_patch(Circle((ex, ey), 0.28, fill=False, lw=LW))
    ax.add_patch(Circle((ex, ey), 0.12, fill=True, color="k"))
    for dx in (-0.45, -0.15, 0.15, 0.45):
        ax.plot([ex + dx, ex + dx], [ey + 0.55, ey + 0.75], "k", lw=0.7)
    ax.text(7.7, 1.7, "eye", fontsize=9)
    save(fig, "fig_q6_context.png", 4.4, 2.5)


def fig_q8_scale():
    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, 22)
    ax.set_ylim(0, 8)
    ax.axis("off")
    # bench rule
    ax.add_patch(Rectangle((0, 1.0), 20, 0.7, fill=False, lw=LW))
    for i in range(0, 21):
        h = 0.45 if i % 5 == 0 else 0.25
        ax.plot([i, i], [1.0, 1.0 + h], "k", lw=0.7)
        if i % 5 == 0:
            ax.text(i, 0.35, str(i), ha="center", fontsize=8)
    ax.text(8, 0.05, "distance / cm", fontsize=9)
    # lens at 5 cm
    lens_simple(ax, 5, 2.2, 6.5)
    ax.text(4.2, 6.8, "lens", fontsize=9)
    # screen at 15 cm (f = 10 cm)
    ax.add_patch(Rectangle((14.7, 2.2), 0.35, 4.3, fill=False, lw=LW))
    ax.text(14.2, 6.8, "screen", fontsize=9)
    # sharp image mark
    ax.plot([14.7, 15.05], [4.3, 4.3], "k", lw=2)
    ax.text(16.0, 4.5, "sharp image\nof distant window", fontsize=8)
    # dimension lens to screen
    ax.annotate("", xy=(15, 7.5), xytext=(5, 7.5), arrowprops=dict(arrowstyle="<->", color="k", lw=0.9))
    save(fig, "fig_q8_scale.png", 5.6, 2.5)


def fig_q10_screens():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.axhline(3.5, color="k", lw=0.6, ls="--")
    # object
    ax.annotate("", xy=(2, 5.3), xytext=(2, 3.5), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.3, mutation_scale=11))
    ax.text(1.3, 5.4, "object", fontsize=8)
    lens_simple(ax, 6.5, 0.9, 6.1)
    ax.text(6.1, 6.4, "lens", fontsize=8)
    # three rays meeting at P = (10.5, 3.5) — wait image inverted so meet below? for tip
    # Ray from tip: parallel then through F; through centre; through F then parallel
    # Simplified: three rays from object tip (2,5.3) meeting at image tip (11, 2.2)
    P = (11.0, 2.2)
    # parallel then to F right? Standard: parallel hits lens at (6.5,5.3) goes through F_right at (9,3.5) toward P
    ax.plot([2, 6.5], [5.3, 5.3], "k", lw=0.8)
    ax.plot([6.5, P[0]], [5.3, P[1]], "k", lw=0.8)
    # through optical centre
    ax.plot([2, P[0]], [5.3, P[1]], "k", lw=0.8)
    # through F_left (4,3.5): from object through F_left to lens then parallel
    ax.plot([2, 6.5], [5.3, 4.0], "k", lw=0.8)
    ax.plot([6.5, P[0]], [4.0, P[1]], "k", lw=0.8)
    ax.plot(*P, "ko", ms=4)
    ax.text(11.2, 1.5, "P", fontsize=10, fontweight="bold")
    # screen positions A–D as vertical lines
    positions = {"A": 4.0, "B": 11.0, "C": 13.0, "D": 8.0}
    for lab, x in positions.items():
        ax.plot([x, x], [1.2, 6.0], "k", lw=1.0 if lab != "B" else 1.0, ls=":")
        ax.add_patch(Rectangle((x - 0.08, 1.2), 0.16, 4.8, fill=False, lw=LW_THIN))
        ax.text(x - 0.15, 0.5, lab, fontsize=11, fontweight="bold")
    ax.text(0.3, 6.5, "Four possible screen positions A–D are shown.", fontsize=8)
    save(fig, "fig_q10_screens.png", 5.4, 2.9)


def fig_11_parallel():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    # grid
    for i in range(0, 17):
        ax.axvline(i, color="0.85", lw=0.5)
    for j in range(0, 11):
        ax.axhline(j, color="0.85", lw=0.5)
    ax.axhline(5, color="k", lw=0.8, ls="--")
    lens_simple(ax, 8, 1.5, 8.5)
    # three parallel rays approaching (stop at lens) — student completes after lens to X
    for y in [3, 5, 7]:
        ax.annotate("", xy=(7.6, y), xytext=(1.0, y), arrowprops=dict(arrowstyle="-|>", color="k", lw=0.9, mutation_scale=9))
    # Unique meeting point X at f = 4.0 cm (4 grid squares from lens centre)
    ax.plot(12, 5, "kx", ms=8, mew=1.5)
    ax.text(12.15, 5.35, "X", fontsize=11, fontweight="bold")
    ax.text(0.3, 9.2, "Fig. 11.1", fontsize=10, fontweight="bold")
    ax.text(0.3, 0.4, "Grid squares: 1.0 cm", fontsize=8)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.0)
    save(fig, "fig_11_1.png", 5.8, 3.6)


def fig_12_completed():
    """Exact geometry: f=3, object (1,7), image (13.25,3.5); rays through F and O."""
    fig, ax = plt.subplots()
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    for i in range(0, 17):
        ax.axvline(i, color="0.85", lw=0.5)
    for j in range(0, 11):
        ax.axhline(j, color="0.85", lw=0.5)
    axis_y = 5.0
    lens_x = 8.0
    f = 3.0
    ax.axhline(axis_y, color="k", lw=0.7, ls="--")
    lens_simple(ax, lens_x, 1.2, 8.8)
    ax.plot(lens_x - f, axis_y, "ko", ms=3)
    ax.text(lens_x - f, axis_y - 0.7, "F", fontsize=9)
    ax.plot(lens_x + f, axis_y, "ko", ms=3)
    ax.text(lens_x + f, axis_y - 0.7, "F", fontsize=9)
    ox, oy = 1.0, 7.0  # height 2.0 cm above axis
    ix, iy = 13.25, 3.5  # height 1.5 cm below axis
    ax.annotate("", xy=(ox, oy), xytext=(ox, axis_y), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.4, mutation_scale=12))
    ax.text(0.2, 7.3, "object", fontsize=8)
    ax.annotate("", xy=(ix, iy), xytext=(ix, axis_y), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.4, mutation_scale=12))
    ax.text(13.5, 2.7, "image", fontsize=8)
    # Ray 1 parallel → through F_right → image tip
    ax.plot([ox, lens_x], [oy, oy], "k", lw=0.9)
    ax.plot([lens_x, ix], [oy, iy], "k", lw=0.9)
    # Ray 2 through O → image tip
    ax.plot([ox, ix], [oy, iy], "k", lw=0.9)
    # Ray 3 through F_left then parallel (hits lens at y=3.5, continues to image tip)
    ax.plot([ox, lens_x], [oy, 3.5], "k", lw=0.9)
    ax.plot([lens_x, ix], [3.5, iy], "k", lw=0.9)
    ax.text(0.3, 9.3, "Fig. 12.1", fontsize=10, fontweight="bold")
    ax.text(0.3, 0.35, "Grid squares: 1.0 cm", fontsize=8)
    ax.set_xticks([])
    ax.set_yticks([])
    save(fig, "fig_12_1.png", 5.8, 3.6)


def fig_13_apparatus():
    """Richer apparatus line art closer to P5 stand/boss/clamp class."""
    fig, ax = plt.subplots()
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 12)
    ax.axis("off")
    # bench / metre rule with edges
    ax.add_patch(Rectangle((1, 1.8), 17.2, 0.85, fill=False, lw=LW))
    ax.plot([1, 18.2], [2.2, 2.2], "k", lw=0.5)
    for i in range(0, 18):
        x = 1.4 + i
        h = 0.45 if i % 5 == 0 else 0.25
        ax.plot([x, x], [1.8, 1.8 + h], "k", lw=0.6)
        if i % 5 == 0:
            ax.text(x, 1.15, str(i * 1), ha="center", fontsize=6)
    ax.text(7.5, 0.55, "metre rule / cm", fontsize=8)
    # retort stand: heavy base + vertical rod
    ax.add_patch(Rectangle((3.6, 2.65), 2.6, 0.45, fill=False, lw=LW))
    ax.add_patch(Rectangle((4.3, 2.65), 1.2, 0.2, fill=False, lw=0.8))
    ax.plot([5.1, 5.1], [3.1, 10.2], "k", lw=2.4)
    # boss (cylindrical clamp block) with screw
    ax.add_patch(FancyBboxPatch((4.55, 6.5), 1.15, 1.0, boxstyle="round,pad=0.02,rounding_size=0.15", fill=False, lw=LW))
    ax.plot([4.55, 4.35], [7.0, 7.0], "k", lw=1.2)
    ax.add_patch(Circle((4.25, 7.0), 0.18, fill=False, lw=0.9))
    ax.text(3.3, 7.3, "boss", fontsize=7)
    # clamp jaw / arm holding lens holder
    ax.plot([5.7, 7.5], [7.0, 7.0], "k", lw=2.0)
    ax.plot([7.5, 7.5], [6.5, 7.5], "k", lw=1.5)
    # lens holder: two uprights + base slot
    ax.add_patch(Rectangle((7.35, 5.2), 1.3, 0.25, fill=False, lw=LW))
    ax.plot([7.5, 7.5], [5.45, 8.7], "k", lw=1.4)
    ax.plot([8.5, 8.5], [5.45, 8.7], "k", lw=1.4)
    ax.plot([7.5, 8.5], [8.7, 8.7], "k", lw=1.2)
    lens_simple(ax, 8.0, 5.7, 8.5)
    ax.text(6.6, 9.2, "converging lens\nin holder", fontsize=8)
    # screen assembly
    ax.add_patch(Rectangle((13.2, 2.65), 2.0, 0.4, fill=False, lw=LW))
    ax.plot([14.2, 14.2], [3.05, 5.1], "k", lw=1.8)
    ax.add_patch(Rectangle((13.1, 5.1), 2.2, 3.4, fill=False, lw=LW))
    # cross on screen suggesting image plane
    ax.plot([13.3, 15.1], [6.8, 6.8], "k", lw=0.5, ls=":")
    ax.text(12.9, 8.8, "white screen", fontsize=8)
    # distant tree (simple recognisable tree, not a bare arrow)
    ax.plot([0.9, 0.9], [3.5, 5.2], "k", lw=2.0)
    ax.plot([0.9, 0.3, 0.9, 1.5, 0.9], [5.2, 6.0, 7.2, 6.0, 5.2], "k", lw=1.0)
    ax.text(0.15, 9.6, "distant\ntree", fontsize=8)
    for y in [6.0, 6.8, 7.6]:
        ax.plot([1.6, 7.7], [y, y], "k", lw=0.6, ls="--")
    ax.annotate("", xy=(14.2, 10.6), xytext=(8.0, 10.6), arrowprops=dict(arrowstyle="<->", color="k", lw=0.9))
    ax.text(9.6, 10.9, "15.0 cm", fontsize=9)
    ax.text(0.3, 11.4, "Fig. 13.1", fontsize=10, fontweight="bold")
    ax.text(3.7, 3.5, "stand", fontsize=8)
    save(fig, "fig_13_1.png", 6.2, 3.7)


def fig_14_virtual():
    """Correct virtual-image construction rays: parallel→F_right; through O; diverge on right."""
    fig, ax = plt.subplots()
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.set_aspect("equal")
    ax.axis("off")
    axis_y = 4.5
    lens_x = 7.0
    f = 2.5
    ax.axhline(axis_y, color="k", lw=0.7, ls="--")
    lens_simple(ax, lens_x, 1.2, 7.8)
    ax.plot(lens_x - f, axis_y, "ko", ms=3)
    ax.text(lens_x - f, axis_y - 0.55, "F", fontsize=9)
    ax.plot(lens_x + f, axis_y, "ko", ms=3)
    ax.text(lens_x + f, axis_y - 0.55, "F", fontsize=9)
    # object between F and lens — sizes chosen so virtual I stays on the figure
    ox, oy = 5.8, 5.8
    ax.annotate("", xy=(ox, oy), xytext=(ox, axis_y), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.3, mutation_scale=11))
    ax.text(4.85, 6.15, "object", fontsize=8)
    # Incident: parallel to axis to lens
    ax.plot([ox, lens_x], [oy, oy], "k", lw=0.9)
    # Emergent: toward F_right and beyond
    Fr = (lens_x + f, axis_y)
    t = (12.5 - lens_x) / (Fr[0] - lens_x)
    y_end = oy + t * (Fr[1] - oy)
    ax.annotate("", xy=(12.5, y_end), xytext=(lens_x, oy), arrowprops=dict(arrowstyle="-|>", color="k", lw=0.9, mutation_scale=9))
    # Through O undeviated
    slope = (axis_y - oy) / (lens_x - ox)
    y2 = axis_y + slope * (12.5 - lens_x)
    ax.plot([ox, lens_x], [oy, axis_y], "k", lw=0.9)
    ax.annotate("", xy=(12.5, y2), xytext=(lens_x, axis_y), arrowprops=dict(arrowstyle="-|>", color="k", lw=0.9, mutation_scale=9))
    ax.text(0.3, 8.4, "Fig. 14.1", fontsize=10, fontweight="bold")
    ax.text(0.3, 0.35, "The two rays on the right leave the lens and diverge.", fontsize=8)
    save(fig, "fig_14_1.png", 5.4, 3.4)


def fig_15_blank():
    """Incident ray aimed exactly at optical centre O (student continues undeviated)."""
    fig, ax = plt.subplots()
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.set_aspect("equal")
    ax.axis("off")
    axis_y = 3.5
    lens_x = 6.0
    ax.axhline(axis_y, color="k", lw=0.7, ls="--")
    lens_simple(ax, lens_x, 1.0, 6.0)
    ax.plot(3.5, axis_y, "ko", ms=3)
    ax.text(3.3, 2.9, "F", fontsize=9)
    ax.plot(8.5, axis_y, "ko", ms=3)
    ax.text(8.3, 2.9, "F", fontsize=9)
    ax.plot(lens_x, axis_y, "ko", ms=3)
    ax.text(lens_x + 0.2, axis_y + 0.25, "O", fontsize=9)
    # Ray aimed exactly at O: stop just before the lens for the student to continue
    ax.annotate("", xy=(5.75, 3.55), xytext=(1.2, 5.2), arrowprops=dict(arrowstyle="-|>", color="k", lw=0.9, mutation_scale=9))
    ax.text(0.3, 6.4, "Fig. 15.1", fontsize=10, fontweight="bold")
    save(fig, "fig_15_1.png", 4.8, 2.8)


def fig_16_camera():
    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, 22)
    ax.set_ylim(0, 9)
    ax.axis("off")
    # scale
    ax.add_patch(Rectangle((0, 1.0), 20, 0.55, fill=False, lw=LW))
    for i in range(0, 21):
        ax.plot([i, i], [1.0, 1.35 if i % 5 else 1.5], "k", lw=0.6)
        if i % 5 == 0:
            ax.text(i, 0.4, str(i), ha="center", fontsize=8)
    ax.text(7.5, 0.05, "distance / cm", fontsize=8)
    # object at 0
    ax.annotate("", xy=(0, 6.5), xytext=(0, 3.5), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.3, mutation_scale=11))
    ax.text(0.3, 6.8, "illuminated\nobject", fontsize=8)
    lens_simple(ax, 12, 2.5, 7.0)
    ax.text(11.3, 7.4, "lens", fontsize=8)
    # film at 18
    ax.add_patch(Rectangle((17.7, 2.5), 0.35, 4.5, fill=False, lw=LW))
    ax.annotate("", xy=(17.85, 2.9), xytext=(17.85, 3.5), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.2, mutation_scale=10))
    ax.text(18.3, 7.4, "film", fontsize=8)
    # rays meeting at film tip
    ax.plot([0, 12], [6.5, 6.5], "k", lw=0.7)
    ax.plot([12, 17.85], [6.5, 2.9], "k", lw=0.7)
    ax.plot([0, 17.85], [6.5, 2.9], "k", lw=0.7)
    ax.text(0.2, 8.4, "Fig. 16.1", fontsize=10, fontweight="bold")
    save(fig, "fig_16_1.png", 5.8, 2.8)


def fig_17_one():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.axhline(4, color="k", lw=0.6, ls="--")
    ax.annotate("", xy=(2.5, 6.2), xytext=(2.5, 4), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.2, mutation_scale=11))
    ax.text(1.6, 6.4, "object", fontsize=8)
    lens_simple(ax, 7, 1.3, 6.7)
    ax.add_patch(Rectangle((11.5, 1.5), 0.25, 5.0, fill=False, lw=LW))
    ax.annotate("", xy=(11.6, 2.9), xytext=(11.6, 4), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.2, mutation_scale=10))
    ax.text(11.9, 6.6, "screen", fontsize=8)
    ax.plot([2.5, 7], [6.2, 6.2], "k", lw=0.7)
    ax.plot([7, 11.6], [6.2, 2.9], "k", lw=0.7)
    ax.plot([2.5, 11.6], [6.2, 2.9], "k", lw=0.7)
    ax.text(0.3, 7.4, "Fig. 17.1", fontsize=10, fontweight="bold")
    save(fig, "fig_17_1.png", 5.0, 2.9)


def fig_18_two_lenses():
    fig, axes = plt.subplots(1, 2)
    for ax, title, f, meet_x in zip(axes, ["lens A", "lens B"], [4.0, 2.5], [12.0, 10.5]):
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.set_aspect("equal")
        ax.axis("off")
        for i in range(0, 15):
            ax.axvline(i, color="0.88", lw=0.4)
        for j in range(0, 9):
            ax.axhline(j, color="0.88", lw=0.4)
        ax.axhline(4, color="k", lw=0.6, ls="--")
        lens_simple(ax, 8, 1.2, 6.8)
        for y in [2.5, 4, 5.5]:
            ax.plot([1, 8], [y, y], "k", lw=0.7)
            ax.plot([8, meet_x], [y, 4], "k", lw=0.7)
        ax.plot(meet_x, 4, "ko", ms=3)
        ax.text(meet_x, 3.2, "F", fontsize=9)
        ax.text(0.3, 7.3, title, fontsize=10, fontweight="bold")
        ax.text(0.3, 0.3, "1 square = 1.0 cm", fontsize=7)
    fig.suptitle("Fig. 18.1", fontsize=11, fontweight="bold", y=0.98)
    save(fig, "fig_18_1.png", 6.2, 3.2)


def fig_19_rays():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.axhline(4.5, color="k", lw=0.7, ls="--")
    lens_simple(ax, 7, 1.2, 7.8)
    ax.plot(4.0, 4.5, "ko", ms=3)
    ax.text(3.7, 3.9, "F", fontsize=9)
    ax.plot(10.0, 4.5, "ko", ms=3)
    ax.text(9.7, 3.9, "F", fontsize=9)
    ax.plot(7, 4.5, "ko", ms=3)
    ax.text(7.15, 4.7, "O", fontsize=9)
    # Ray 1 parallel at y=6.5
    ax.annotate("", xy=(6.6, 6.5), xytext=(1.0, 6.5), arrowprops=dict(arrowstyle="-|>", color="k", lw=0.9, mutation_scale=9))
    ax.text(0.4, 6.7, "1", fontsize=10, fontweight="bold")
    # Ray 2 through F then to lens
    ax.annotate("", xy=(6.6, 5.3), xytext=(1.5, 2.8), arrowprops=dict(arrowstyle="-|>", color="k", lw=0.9, mutation_scale=9))
    ax.text(0.4, 2.6, "2", fontsize=10, fontweight="bold")
    # Ray 3 toward O
    ax.annotate("", xy=(6.6, 4.5), xytext=(1.5, 5.8), arrowprops=dict(arrowstyle="-|>", color="k", lw=0.9, mutation_scale=9))
    ax.text(0.4, 5.9, "3", fontsize=10, fontweight="bold")
    ax.text(0.3, 8.3, "Fig. 19.1", fontsize=10, fontweight="bold")
    ax.text(0.3, 0.35, "Draw the path of each ray after it passes through the lens.", fontsize=8)
    save(fig, "fig_19_1.png", 5.2, 3.3)


def main():
    fig_q1_options()
    fig_q3_labels()
    fig_q4_image()
    # fig_q6_context and fig_13_apparatus: prefer image-gen exam assets if present
    q6 = OUT / "fig_q6_context.png"
    f13 = OUT / "fig_13_1.png"
    sources = OUT / "sources"
    if not (sources / "fig_q6_gen.jpg").exists():
        fig_q6_context()
    else:
        print("keep image-gen fig_q6_context.png")
    fig_q8_scale()
    fig_q10_screens()
    fig_11_parallel()
    fig_12_completed()
    if not (sources / "fig_13_1_gen.jpg").exists():
        fig_13_apparatus()
    else:
        print("keep image-gen fig_13_1.png")
    fig_14_virtual()
    fig_15_blank()
    fig_16_camera()
    fig_17_one()
    fig_18_two_lenses()
    fig_19_rays()
    print("all figures done in", OUT)


if __name__ == "__main__":
    main()
