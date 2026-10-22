#!/usr/bin/env python3
"""Build SACSS 5086 Lenses Topical Worksheet DOCX (Draft_01+)."""
from __future__ import annotations

import copy
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import OxmlElement
from docx.oxml.ns import qn, nsmap
from docx.shared import Cm, Mm, Pt, Twips, Emu, Inches, RGBColor
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT

ROOT = Path("/workspace/exam-paper-lenses")
FIG = ROOT / "figures"
OUT = ROOT / "drafts"


def set_run_font(run, size=11, bold=False, name="Arial"):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.bold = bold
    run.font.color.rgb = RGBColor(0, 0, 0)


def set_para_spacing(p, before=0, after=0, line=None, exact=None):
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    if exact is not None:
        pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY
        pf.line_spacing = Pt(exact)
    elif line is not None:
        pf.line_spacing = line


def add_border_bottom(paragraph):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "12")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "000000")
    pBdr.append(bottom)
    pPr.append(pBdr)


def add_page_number(paragraph):
    """Insert PAGE field."""
    run = paragraph.add_run()
    fldChar1 = OxmlElement("w:fldChar")
    fldChar1.set(qn("w:fldCharType"), "begin")
    instrText = OxmlElement("w:instrText")
    instrText.set(qn("xml:space"), "preserve")
    instrText.text = " PAGE "
    fldChar2 = OxmlElement("w:fldChar")
    fldChar2.set(qn("w:fldCharType"), "end")
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    set_run_font(run, 11, bold=True)


def setup_section(section, footer_centre="5086 Lenses", turn_over=True):
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.left_margin = Cm(1.5)
    section.right_margin = Cm(1.5)
    section.top_margin = Cm(1.6)
    section.bottom_margin = Cm(1.8)
    # header page number
    header = section.header
    header.is_linked_to_previous = False
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    hp.clear()
    add_page_number(hp)
    set_para_spacing(hp, before=0, after=0)
    # footer
    footer = section.footer
    footer.is_linked_to_previous = False
    fp = footer.paragraphs[0]
    fp.clear()
    # three-part footer via tabs
    tab_stops = fp.paragraph_format.tab_stops
    tab_stops.add_tab_stop(Cm(8.5), WD_TAB_ALIGNMENT.CENTER)
    tab_stops.add_tab_stop(Cm(18.0), WD_TAB_ALIGNMENT.RIGHT)
    r1 = fp.add_run("SACSS Topical Worksheet 2026")
    set_run_font(r1, 8)
    fp.add_run("\t")
    r2 = fp.add_run(footer_centre)
    set_run_font(r2, 8)
    fp.add_run("\t")
    if turn_over:
        r3 = fp.add_run("[Turn over")
        set_run_font(r3, 8, bold=True)
    set_para_spacing(fp, before=0, after=0)


def dotted_line(doc, indent_cm=1.05, mark=None, last=False):
    """Qualitative dotted answer line; if mark given and last, put [n] on same line."""
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Cm(indent_cm)
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY
    pf.line_spacing = Pt(26)
    # right-aligned dot leader to mark or end
    if mark is not None and last:
        tab = pf.tab_stops
        tab.add_tab_stop(Cm(17.0), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        run = p.add_run(f"\t[{mark}]")
        set_run_font(run, 11)
    else:
        tab = pf.tab_stops
        tab.add_tab_stop(Cm(17.0), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        run = p.add_run("\t")
        set_run_font(run, 11)
    return p


def calc_answer(doc, label, unit, mark, indent_cm=1.05):
    """Calculation answer line via fixed-width borderless table (specimen-like columns).

    Page content width ≈ 18.0 cm (A4 21.0 − 1.5 − 1.5).
    Specimen: '=' near mid page (~12.25 cm from page left ⇒ ~10.75 cm into content);
    bracket near right (~19.25 cm from page left ⇒ ~17.75 cm into content).
    Columns: [label=][dotted run][unit [n]]
    """
    # Spacer paragraph for working space
    sp = doc.add_paragraph()
    set_para_spacing(sp, before=8, after=0, exact=14)

    table = doc.add_table(rows=1, cols=3)
    table.autofit = False
    table.allow_autofit = False
    # Fixed layout: total 17.74 cm content width (bracket at specimen x). Col1 ends at specimen '=' (~12.25 cm page).
    # LO calibrate: 11.10→336.6pt, 11.48→357.2pt; target 347.3 → ≈11.30 cm
    widths_cm = [11.13, 4.80, 1.81]
    widths = [Cm(w) for w in widths_cm]
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else OxmlElement("w:tblPr")
    # fixed layout
    tblW = OxmlElement("w:tblW")
    tblW.set(qn("w:w"), str(int(17.74 * 567)))  # dxa ≈ 567 per cm
    tblW.set(qn("w:type"), "dxa")
    # remove old tblW if present
    for child in list(tblPr):
        if child.tag == qn("w:tblW"):
            tblPr.remove(child)
        if child.tag == qn("w:tblLayout"):
            tblPr.remove(child)
    tblPr.append(tblW)
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    # grid
    for child in list(tbl):
        if child.tag == qn("w:tblGrid"):
            tbl.remove(child)
    grid = OxmlElement("w:tblGrid")
    for w in widths_cm:
        gc = OxmlElement("w:gridCol")
        gc.set(qn("w:w"), str(int(w * 567)))
        grid.append(gc)
    tbl.insert(1, grid)

    for cell, w in zip(table.rows[0].cells, widths):
        cell.width = w
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        for child in list(tcPr):
            if child.tag == qn("w:tcW"):
                tcPr.remove(child)
            if child.tag == qn("w:tcBorders"):
                tcPr.remove(child)
        tcW = OxmlElement("w:tcW")
        tcW.set(qn("w:w"), str(int(w.cm * 567)))
        tcW.set(qn("w:type"), "dxa")
        tcPr.append(tcW)
        tcBorders = OxmlElement("w:tcBorders")
        for edge in ("top", "left", "bottom", "right"):
            el = OxmlElement(f"w:{edge}")
            el.set(qn("w:val"), "nil")
            tcBorders.append(el)
        tcPr.append(tcBorders)

    c0, c1, c2 = table.rows[0].cells
    p0 = c0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p0.add_run(f"{label} =")
    set_run_font(r, 11)
    set_para_spacing(p0, before=0, after=0, exact=26)

    p1 = c1.paragraphs[0]
    # dotted leader across cell
    pf = p1.paragraph_format
    pf.tab_stops.add_tab_stop(Cm(5.8), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
    r = p1.add_run("\t")
    set_run_font(r, 11)
    set_para_spacing(p1, before=0, after=0, exact=26)

    p2 = c2.paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p2.add_run(f"{unit} [{mark}]")
    set_run_font(r, 11)
    set_para_spacing(p2, before=0, after=0, exact=26)
    return table


def total_line(doc, n):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    set_para_spacing(p, before=6, after=0, exact=26)
    run = p.add_run(f"[Total: {n}]")
    set_run_font(run, 11)
    return p


def body(doc, text, indent=1.05, bold=False, space_after=6, justify=True):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Cm(indent)
    pf.first_line_indent = Cm(0)
    set_para_spacing(p, before=0, after=space_after, exact=14)
    if justify:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    set_run_font(run, 11, bold=bold)
    return p


def q_stem(doc, number, text):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Cm(1.05)
    pf.first_line_indent = Cm(-0.8)
    set_para_spacing(p, before=8, after=6, exact=14)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(f"{number}\t{text}")
    set_run_font(run, 11)
    return p


def part_label(doc, label, text, indent=1.05):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Cm(indent + 0.8)
    pf.first_line_indent = Cm(-0.8)
    set_para_spacing(p, before=10, after=4, exact=14)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(f"({label})\t{text}")
    set_run_font(run, 11)
    return p


def command(doc, text, indent=1.85):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Cm(indent)
    set_para_spacing(p, before=8, after=4, exact=14)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    set_run_font(run, 11)
    return p


def add_figure(doc, path, width_cm=14.0, caption=None):
    """Insert figure. Captions are usually already burned into the PNG — pass caption=None."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_para_spacing(p, before=4, after=6)
    # Keep figure with following text where possible
    p.paragraph_format.keep_with_next = True
    run = p.add_run()
    run.add_picture(str(path), width=Cm(width_cm))
    if caption:
        cp = doc.add_paragraph()
        cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_para_spacing(cp, before=0, after=6)
        r = cp.add_run(caption)
        set_run_font(r, 11, bold=True)
    return p


def option(doc, letter, text, indent=1.85):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Cm(indent)
    pf.first_line_indent = Cm(-0.6)
    set_para_spacing(p, before=2, after=2, exact=14)
    run = p.add_run(f"{letter}\t{text}")
    set_run_font(run, 11)
    return p


def page_break_before(paragraph):
    pPr = paragraph._p.get_or_add_pPr()
    # remove existing pageBreakBefore if any
    pb = OxmlElement("w:pageBreakBefore")
    # insert into pPr — actually use pageBreakBefore true
    # Better: set via paragraph_format
    paragraph.paragraph_format.page_break_before = True


def build_cover(doc):
    # Cover has no header page number in specimen style sometimes — keep consistent
    p = doc.add_paragraph()
    set_para_spacing(p, before=0, after=0)
    r = p.add_run("SACSS")
    set_run_font(r, 14, bold=True)
    p2 = doc.add_paragraph()
    set_para_spacing(p2, before=0, after=8)
    r = p2.add_run("Topical Worksheet 2026")
    set_run_font(r, 12)

    # Candidate boxes as table
    t = doc.add_table(rows=2, cols=3)
    t.autofit = False
    # Row 0 labels
    cells = [
        (0, 0, "CANDIDATE\nNAME"),
        (0, 1, "CENTRE\nNUMBER"),
        (0, 2, "INDEX\nNUMBER"),
    ]
    for r, c, text in cells:
        cell = t.cell(r, c)
        cell.text = ""
        p = cell.paragraphs[0]
        run = p.add_run(text)
        set_run_font(run, 9, bold=True)
    # Row 1 boxes
    # Name wide
    cell = t.cell(1, 0)
    cell.text = ""
    # draw empty tall box via paragraph border approx — use nested table of squares for centre/index
    # Centre: S + 4 boxes
    cell = t.cell(1, 1)
    cell.text = ""
    inner = cell.add_table(rows=1, cols=5)
    for i, ch in enumerate(["S", "", "", "", ""]):
        ic = inner.cell(0, i)
        ic.text = ""
        ip = ic.paragraphs[0]
        ip.alignment = WD_ALIGN_PARAGRAPH.CENTER
        ir = ip.add_run(ch)
        set_run_font(ir, 14, bold=True)
        # cell width borders
        tc = ic._tc
        tcPr = tc.get_or_add_tcPr()
        tcW = OxmlElement("w:tcW")
        tcW.set(qn("w:w"), "400")
        tcW.set(qn("w:type"), "dxa")
        tcPr.append(tcW)
    cell = t.cell(1, 2)
    cell.text = ""
    inner2 = cell.add_table(rows=1, cols=4)
    for i in range(4):
        ic = inner2.cell(0, i)
        ic.text = ""
        tc = ic._tc
        tcPr = tc.get_or_add_tcPr()
        tcW = OxmlElement("w:tcW")
        tcW.set(qn("w:w"), "400")
        tcW.set(qn("w:type"), "dxa")
        tcPr.append(tcW)

    # Set column widths
    for row in t.rows:
        row.cells[0].width = Cm(9.5)
        row.cells[1].width = Cm(4.5)
        row.cells[2].width = Cm(4.0)

    # borders for name cell
    name_cell = t.cell(1, 0)
    # add empty lines for writing
    for _ in range(2):
        name_cell.add_paragraph("")

    # horizontal line
    line = doc.add_paragraph()
    add_border_bottom(line)
    set_para_spacing(line, before=8, after=8)

    # Title block
    t2 = doc.add_table(rows=3, cols=2)
    left = t2.cell(0, 0).paragraphs[0]
    r = left.add_run("SCIENCE (PHYSICS)")
    set_run_font(r, 16, bold=True)
    right = t2.cell(0, 1).paragraphs[0]
    right.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = right.add_run("5086")
    set_run_font(r, 16, bold=True)
    left = t2.cell(1, 0).paragraphs[0]
    r = left.add_run("Topic: Lenses")
    set_run_font(r, 12)
    right = t2.cell(1, 1).paragraphs[0]
    right.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = right.add_run("Topical Worksheet 2026")
    set_run_font(r, 12)
    right = t2.cell(2, 1).paragraphs[0]
    right.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = right.add_run("1 hour 30 minutes")
    set_run_font(r, 12, bold=True)
    t2.cell(2, 0).text = ""

    p = doc.add_paragraph()
    set_para_spacing(p, before=10, after=2)
    r = p.add_run("Candidates answer on the Question Paper.")
    set_run_font(r, 11)
    p = doc.add_paragraph()
    set_para_spacing(p, before=0, after=6)
    r = p.add_run("No Additional Materials are required.")
    set_run_font(r, 11)

    line = doc.add_paragraph()
    add_border_bottom(line)
    set_para_spacing(line, before=4, after=4)

    p = doc.add_paragraph()
    r = p.add_run("READ THESE INSTRUCTIONS FIRST")
    set_run_font(r, 11, bold=True)

    instructions = [
        "Write your Centre number, index number and name on the work you hand in.",
        "You may use an HB pencil for any diagrams, graphs or rough working.",
        "Write in dark blue or black pen.",
        "Do not use staples, paper clips, glue or correction fluid.",
        "The use of an approved scientific calculator is expected, where appropriate.",
        "You may lose marks if you do not show your working or if you do not use appropriate units.",
        "DO NOT WRITE ON ANY BARCODES.",
    ]
    for t in instructions:
        p = doc.add_paragraph()
        set_para_spacing(p, before=2, after=2, exact=14)
        r = p.add_run(t)
        set_run_font(r, 11)

    p = doc.add_paragraph()
    set_para_spacing(p, before=10, after=2)
    r = p.add_run("Section A")
    set_run_font(r, 11, bold=True)
    r = p.add_run("  (10 marks)")
    set_run_font(r, 11)
    p = doc.add_paragraph()
    set_para_spacing(p, before=0, after=2)
    r = p.add_run("Answer all questions.")
    set_run_font(r, 11)
    p = doc.add_paragraph()
    set_para_spacing(p, before=0, after=6)
    r = p.add_run("For each question choose one answer, A, B, C or D, and write its letter in the answer grid.")
    set_run_font(r, 11)

    p = doc.add_paragraph()
    set_para_spacing(p, before=6, after=2)
    r = p.add_run("Section B")
    set_run_font(r, 11, bold=True)
    r = p.add_run("  (61 marks)")
    set_run_font(r, 11)
    p = doc.add_paragraph()
    set_para_spacing(p, before=0, after=2)
    r = p.add_run("Answer all questions. Each question starts on a new page.")
    set_run_font(r, 11)
    p = doc.add_paragraph()
    set_para_spacing(p, before=0, after=6)
    r = p.add_run("Write your answers in the spaces provided on the question paper.")
    set_run_font(r, 11)

    p = doc.add_paragraph()
    set_para_spacing(p, before=8, after=12)
    r = p.add_run("The number of marks is given in brackets [ ] at the end of each question or part question.")
    set_run_font(r, 11)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_para_spacing(p, before=40, after=0)
    r = p.add_run("This document consists of 17 printed pages and 1 blank page.")
    set_run_font(r, 11)

    # page break to Q
    doc.add_page_break()


def build_section_a(doc):
    p = doc.add_paragraph()
    r = p.add_run("Section A")
    set_run_font(r, 12, bold=True)
    p = doc.add_paragraph()
    set_para_spacing(p, before=4, after=10)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = p.add_run(
        "Answer all the questions. For each question there are four possible answers, A, B, C and D. "
        "Choose the one you consider correct and write its letter in the answer grid at the end of Section A."
    )
    set_run_font(r, 11)

    # Q1
    q_stem(
        doc,
        1,
        "The diagrams show a thin converging lens and three rays of light that are parallel to the principal axis before they reach the lens.",
    )
    body(doc, "Which diagram correctly shows the paths of the rays after they pass through the lens?", indent=1.05)
    add_figure(doc, FIG / "fig_q1_options.png", 11.5)

    # Q2
    q_stem(doc, 2, "What is the focal length of a thin converging lens?")
    option(doc, "A", "the diameter of the lens")
    option(doc, "B", "the distance from the object to the lens")
    option(doc, "C", "the distance from the optical centre of the lens to the principal focus")
    option(doc, "D", "the distance from the principal focus to a point labelled 2F")

    # Q3 — keep stem, figure and options together
    p = doc.add_paragraph()
    page_break_before(p)
    q_stem(doc, 3, "The diagram shows a thin converging lens and two rays of light that are parallel to the principal axis before they reach the lens. Points are labelled A, B, C and D.")
    add_figure(doc, FIG / "fig_q3_labels.png", 11.0)
    body(doc, "Which label marks a principal focus of the lens?", indent=1.05)
    option(doc, "A", "A")
    option(doc, "B", "B")
    option(doc, "C", "C")
    option(doc, "D", "D")

    # Q4
    q_stem(
        doc,
        4,
        "The diagram shows an object O and its image I formed by a thin converging lens. The diagram is drawn to scale.",
    )
    add_figure(doc, FIG / "fig_q4_image.png", 11.5)
    body(doc, "Which row correctly describes the image?", indent=1.05)
    # table options
    table = doc.add_table(rows=5, cols=4)
    headers = ["", "real or virtual", "upright or inverted", "magnified or diminished"]
    data = [
        ["A", "virtual", "upright", "magnified"],
        ["B", "real", "upright", "diminished"],
        ["C", "virtual", "inverted", "diminished"],
        ["D", "real", "inverted", "diminished"],
    ]
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.text = ""
        run = cell.paragraphs[0].add_run(h)
        set_run_font(run, 10, bold=True)
    for i, row in enumerate(data, start=1):
        for j, val in enumerate(row):
            cell = table.cell(i, j)
            cell.text = ""
            run = cell.paragraphs[0].add_run(val)
            set_run_font(run, 10)

    # Q5 — keep all four options with the stem (avoid orphan onto next page)
    p = doc.add_paragraph()
    page_break_before(p)
    q_stem(doc, 5, "What is meant by a real image?")
    option(doc, "A", "an image that is always magnified")
    option(doc, "B", "an image that can be formed on a screen")
    option(doc, "C", "an image that is always upright")
    option(doc, "D", "an image that can only be seen by looking through the lens")

    # Q6 — keep together on a fresh page block
    p = doc.add_paragraph()
    page_break_before(p)
    q_stem(
        doc,
        6,
        "A student uses a thin converging lens as a reading lens to look at a stamp. The image she sees is larger than the stamp and upright.",
    )
    add_figure(doc, FIG / "fig_q6_context.png", 8.0)
    body(doc, "Which type of image does she see?", indent=1.05)
    option(doc, "A", "virtual")
    option(doc, "B", "real")
    option(doc, "C", "inverted and real")
    option(doc, "D", "diminished and real")

    # Q7
    q_stem(
        doc,
        7,
        "A thin converging lens is thicker at its centre than at its edges. A beam of light travelling in air meets the lens.",
    )
    body(doc, "Which statement about the action of the lens is correct?", indent=1.05)
    option(doc, "A", "The lens reflects the whole beam back into the air.")
    option(doc, "B", "Light travels faster in the glass than in air, so the beam spreads out.")
    option(doc, "C", "Different parts of the beam are refracted by different amounts so that a parallel beam can be brought to a focus.")
    option(doc, "D", "The direction of every ray is unchanged because the lens is thin.")

    # Q8
    p = doc.add_paragraph()
    page_break_before(p)
    q_stem(
        doc,
        8,
        "A student forms a sharp image of a distant window on a screen using a thin converging lens. The diagram shows the arrangement. A scale marked in centimetres is drawn along the bench.",
    )
    add_figure(doc, FIG / "fig_q8_scale.png", 12.5)
    body(doc, "What is the focal length of the lens?", indent=1.05)
    option(doc, "A", "5 cm")
    option(doc, "B", "8 cm")
    option(doc, "C", "10 cm")
    option(doc, "D", "15 cm")

    # Q9
    q_stem(doc, 9, "A ray of light is directed towards the optical centre of a thin converging lens.")
    body(doc, "What happens to the ray as it passes through the lens?", indent=1.05)
    option(doc, "A", "It passes through without changing direction.")
    option(doc, "B", "It is reflected back along its original path.")
    option(doc, "C", "It is always refracted through the principal focus.")
    option(doc, "D", "It always emerges parallel to the principal axis.")

    # Q10 — keep stem+figure+options together
    p = doc.add_paragraph()
    page_break_before(p)
    q_stem(
        doc,
        10,
        "The diagram shows an object, a thin converging lens and the paths of three rays of light after they pass through the lens. The rays meet at point P. Four possible positions for a screen are labelled A, B, C and D.",
    )
    add_figure(doc, FIG / "fig_q10_screens.png", 12.5)
    body(doc, "At which screen position can a sharp image of the tip of the object be formed?", indent=1.05)
    option(doc, "A", "A")
    option(doc, "B", "B")
    option(doc, "C", "C")
    option(doc, "D", "D")

    # Answer grid
    p = doc.add_paragraph()
    set_para_spacing(p, before=16, after=8)
    r = p.add_run("Answer grid for Section A")
    set_run_font(r, 11, bold=True)

    grid = doc.add_table(rows=2, cols=10)
    for i in range(10):
        grid.cell(0, i).text = ""
        run = grid.cell(0, i).paragraphs[0].add_run(str(i + 1))
        set_run_font(run, 11, bold=True)
        grid.cell(0, i).paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        grid.cell(1, i).text = ""
        # empty answer box height
        for _ in range(2):
            grid.cell(1, i).add_paragraph("")


def build_section_b(doc):
    # Q11
    p = doc.add_paragraph()
    page_break_before(p)
    r = p.add_run("Section B")
    set_run_font(r, 12, bold=True)
    p2 = doc.add_paragraph()
    set_para_spacing(p2, before=4, after=10)
    r = p2.add_run("Answer all the questions in the spaces provided.")
    set_run_font(r, 11)

    q_stem(
        doc,
        11,
        "Fig. 11.1 shows a thin converging lens. Three rays of light that are parallel to the principal axis are approaching the lens. Point X lies on the principal axis. The grid has squares of side 1.0 cm.",
    )
    add_figure(doc, FIG / "fig_11_1.png", 14.0)
    part_label(
        doc,
        "a",
        "On Fig. 11.1, draw the paths of the three rays after they pass through the lens so that the rays meet at X.",
    )
    # drawing mark below
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    set_para_spacing(p, before=4, after=4)
    r = p.add_run("[2]")
    set_run_font(r, 11)

    part_label(doc, "b", "On Fig. 11.1, label point X with the letter F to show that X is the principal focus of the lens.")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p.add_run("[1]")
    set_run_font(r, 11)

    part_label(doc, "c", "Use Fig. 11.1 to determine the focal length of the lens.")
    calc_answer(doc, "focal length", "cm", 2)

    part_label(doc, "d", "Define the focal length of a thin converging lens.")
    dotted_line(doc, mark=None, last=False)
    dotted_line(doc, mark=2, last=True)
    total_line(doc, 7)

    # Q12
    p = doc.add_paragraph()
    page_break_before(p)
    q_stem(
        doc,
        12,
        "Fig. 12.1 shows a completed ray diagram for an illuminated object and a thin converging lens. The grid has squares of side 1.0 cm.",
    )
    add_figure(doc, FIG / "fig_12_1.png", 14.0)
    part_label(doc, "a", "Use Fig. 12.1 to state three characteristics of the image.")
    dotted_line(doc)
    dotted_line(doc)
    dotted_line(doc, mark=3, last=True)
    part_label(doc, "b", "Use Fig. 12.1 to determine the height of the image.")
    calc_answer(doc, "image height", "cm", 1)
    part_label(doc, "c", "Explain how Fig. 12.1 shows that the image is real.")
    dotted_line(doc)
    dotted_line(doc, mark=2, last=True)
    total_line(doc, 6)

    # Q13
    p = doc.add_paragraph()
    page_break_before(p)
    q_stem(
        doc,
        13,
        "A student determines the focal length of a thin converging lens by forming a sharp image of a distant tree on a white screen. Fig. 13.1 shows the apparatus.",
    )
    add_figure(doc, FIG / "fig_13_1.png", 14.5)
    part_label(
        doc,
        "a",
        "Describe how the student uses the apparatus to obtain a value for the focal length of the lens.",
    )
    dotted_line(doc)
    dotted_line(doc)
    dotted_line(doc, mark=3, last=True)
    part_label(
        doc,
        "b",
        "Explain why the light from the distant tree can be treated as a beam of rays that are parallel when they reach the lens.",
    )
    dotted_line(doc)
    dotted_line(doc, mark=2, last=True)
    part_label(doc, "c", "Fig. 13.1 shows the distance from the lens to the screen when the image is sharp.")
    command(doc, "State the focal length of the lens.")
    calc_answer(doc, "focal length", "cm", 2)
    part_label(doc, "d", "Suggest one precaution that improves the accuracy of the measured focal length.")
    dotted_line(doc, mark=1, last=True)
    total_line(doc, 8)

    # Q14
    p = doc.add_paragraph()
    page_break_before(p)
    q_stem(
        doc,
        14,
        "Fig. 14.1 shows a thin converging lens and an object. Two rays of light leave the lens and diverge. The principal foci F are marked.",
    )
    add_figure(doc, FIG / "fig_14_1.png", 13.5)
    part_label(
        doc,
        "a",
        "On Fig. 14.1, extend the two diverging rays backwards until they meet. Mark the image of the tip of the object with the letter I.",
    )
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p.add_run("[2]")
    set_run_font(r, 11)
    part_label(doc, "b", "Use your completed Fig. 14.1 to state three characteristics of the image.")
    dotted_line(doc)
    dotted_line(doc)
    dotted_line(doc, mark=3, last=True)
    part_label(doc, "c", "Explain why this image cannot be formed on a screen.")
    dotted_line(doc)
    dotted_line(doc, mark=2, last=True)
    total_line(doc, 7)

    # Q15
    p = doc.add_paragraph()
    page_break_before(p)
    q_stem(doc, 15, "Fig. 15.1 shows a thin converging lens. The optical centre O and the principal foci F are marked. A ray of light is approaching the lens.")
    add_figure(doc, FIG / "fig_15_1.png", 12.0)
    part_label(doc, "a", "Define the principal focus of a thin converging lens.")
    dotted_line(doc)
    dotted_line(doc, mark=2, last=True)
    part_label(doc, "b", "State what is meant by the optical centre of a thin lens.")
    dotted_line(doc)
    dotted_line(doc, mark=2, last=True)
    part_label(
        doc,
        "c",
        "The ray shown on Fig. 15.1 is directed towards the optical centre O. On Fig. 15.1, draw the path of the ray after it passes through the lens. Label the principal axis.",
    )
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p.add_run("[2]")
    set_run_font(r, 11)
    total_line(doc, 6)

    # Q16
    p = doc.add_paragraph()
    page_break_before(p)
    q_stem(
        doc,
        16,
        "Fig. 16.1 shows a simple model of a camera. An illuminated object, a thin converging lens and a film are arranged on a bench. A scale marked in centimetres is drawn along the bench. Rays of light from the tip of the object meet on the film.",
    )
    add_figure(doc, FIG / "fig_16_1.png", 14.5)
    part_label(doc, "a", "Use Fig. 16.1 to determine the distance from the object to the lens and the distance from the lens to the film.")
    calc_answer(doc, "object to lens", "cm", 1)
    calc_answer(doc, "lens to film", "cm", 1)
    part_label(doc, "b", "Use Fig. 16.1 to state three characteristics of the image on the film.")
    dotted_line(doc)
    dotted_line(doc)
    dotted_line(doc, mark=3, last=True)
    part_label(doc, "c", "State whether the image on the film is real or virtual.")
    dotted_line(doc, mark=1, last=True)
    total_line(doc, 6)

    # Q17
    p = doc.add_paragraph()
    page_break_before(p)
    q_stem(
        doc,
        17,
        "A student investigates images formed by a thin converging lens. For each arrangement she records whether a sharp image can be obtained on a screen and describes the image. Table 17.1 shows her results.",
    )
    # table
    tbl = doc.add_table(rows=3, cols=5)
    headers = [
        "arrangement",
        "sharp image on a screen?",
        "upright or inverted",
        "larger or smaller than object",
        "real or virtual",
    ]
    rows = [
        ["1", "yes", "inverted", "smaller", ""],
        ["2", "no", "upright", "larger", ""],
    ]
    for j, h in enumerate(headers):
        cell = tbl.cell(0, j)
        cell.text = ""
        run = cell.paragraphs[0].add_run(h)
        set_run_font(run, 9, bold=True)
    for i, row in enumerate(rows, start=1):
        for j, val in enumerate(row):
            cell = tbl.cell(i, j)
            cell.text = ""
            run = cell.paragraphs[0].add_run(val)
            set_run_font(run, 9)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_para_spacing(p, before=4, after=8)
    r = p.add_run("Table 17.1")
    set_run_font(r, 11, bold=True)

    part_label(
        doc,
        "a",
        "For arrangement 1, state whether the image is real or virtual. Justify your answer using Table 17.1.",
    )
    dotted_line(doc)
    dotted_line(doc, mark=2, last=True)
    part_label(
        doc,
        "b",
        "For arrangement 2, use Table 17.1 to complete the last column by stating whether the image is real or virtual. State two other characteristics of this image.",
    )
    dotted_line(doc)
    dotted_line(doc)
    dotted_line(doc, mark=3, last=True)
    body(doc, "Fig. 17.1 shows the arrangement that produced the results in row 1 of Table 17.1.", indent=1.05)
    add_figure(doc, FIG / "fig_17_1.png", 12.5)
    part_label(doc, "c", "Explain how Fig. 17.1 shows that a real image is formed.")
    dotted_line(doc)
    dotted_line(doc, mark=2, last=True)
    total_line(doc, 7)

    # Q18
    p = doc.add_paragraph()
    page_break_before(p)
    q_stem(
        doc,
        18,
        "Fig. 18.1 shows the same parallel beam of light passing separately through two thin converging lenses A and B. The grid has squares of side 1.0 cm.",
    )
    add_figure(doc, FIG / "fig_18_1.png", 15.0)
    part_label(doc, "a", "Use Fig. 18.1 to determine the focal length of lens A and the focal length of lens B.")
    calc_answer(doc, "focal length of A", "cm", 1)
    calc_answer(doc, "focal length of B", "cm", 1)
    part_label(doc, "b", "State which lens, A or B, has the shorter focal length.")
    dotted_line(doc, mark=1, last=True)
    part_label(
        doc,
        "c",
        "Explain what the shorter focal length tells you about the action of that lens on a parallel beam of light.",
    )
    dotted_line(doc)
    dotted_line(doc, mark=2, last=True)
    total_line(doc, 5)

    # Q19 — start final section without [Turn over] for last printed pages
    doc.add_section()
    setup_section(doc.sections[-1], turn_over=False)
    p = doc.add_paragraph()
    q_stem(
        doc,
        19,
        "Fig. 19.1 shows a thin converging lens. The principal foci F and the optical centre O are marked. Three rays of light, labelled 1, 2 and 3, are approaching the lens.",
    )
    add_figure(doc, FIG / "fig_19_1.png", 13.0)
    part_label(doc, "a", "On Fig. 19.1, draw the path of ray 1 after it passes through the lens.")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p.add_run("[2]")
    set_run_font(r, 11)
    part_label(doc, "b", "On Fig. 19.1, draw the path of ray 2 after it passes through the lens.")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p.add_run("[2]")
    set_run_font(r, 11)
    part_label(doc, "c", "On Fig. 19.1, draw the path of ray 3 after it passes through the lens.")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p.add_run("[1]")
    set_run_font(r, 11)
    total_line(doc, 5)

    # Q20
    p = doc.add_paragraph()
    page_break_before(p)
    q_stem(doc, 20, "Thin converging lenses are used in many devices.")
    part_label(
        doc,
        "a",
        "Suggest one device that uses a real image formed by a thin converging lens. Give a reason for your answer.",
    )
    dotted_line(doc)
    dotted_line(doc, mark=2, last=True)
    part_label(
        doc,
        "b",
        "Suggest one device that uses a virtual image formed by a thin converging lens. Give a reason for your answer.",
    )
    dotted_line(doc)
    dotted_line(doc, mark=2, last=True)
    total_line(doc, 4)

    # Blank page in a new section without [Turn over]
    doc.add_section()
    blank_sec = doc.sections[-1]
    setup_section(blank_sec, turn_over=False)
    # Also remove turn over from previous section's last page by leaving as-is;
    # Q20 page still has turn over — fix by configuring section before Q20.
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_para_spacing(p, before=200, after=0)
    r = p.add_run("BLANK PAGE")
    set_run_font(r, 14, bold=True)


def build(out_path: Path):
    doc = Document()
    # default style
    style = doc.styles["Normal"]
    style.font.name = "Arial"
    style.font.size = Pt(11)
    style._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")

    section = doc.sections[0]
    setup_section(section, turn_over=True)

    build_cover(doc)
    build_section_a(doc)
    build_section_b(doc)

    OUT.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_path))
    print("saved", out_path)


if __name__ == "__main__":
    build(OUT / "Draft_01.docx")
