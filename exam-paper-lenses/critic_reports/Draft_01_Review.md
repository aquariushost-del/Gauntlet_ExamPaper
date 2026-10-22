# Independent Critic Review — Draft_01 (Loop 2, Round 1)

**Role:** Independent Critic AI (not Builder)  
**Gauntlet:** v1.5.0  
**Paper:** SACSS Topical Worksheet 2026 — Topic: Lenses (`MIXED_REVISION`)  
**Decision:** **REVISE**  
**Overall weighted score:** **87.6 / 100**  
**Independence:** Genuine separate Critic pass on locked TOS + rendered draft; Builder intended-answer table used only for conflict notes, not as the key.

---

## 1. Files reviewed (actually inspected)

| File | Use |
|---|---|
| `/workspace/GAUNTLET_INSTRUCTIONS.md` §§5, 6, 9, 14 | Scoring gates |
| `/workspace/AGENTS.md` | Profile rules |
| `/workspace/5086_Physics_Key_Syllabus_2026.md` | Light 11(f)–(h); exclusions |
| `/workspace/exam-paper-lenses/tos_gauntlet/TOS_Approved.md` | Locked blueprint |
| `/workspace/exam-paper-lenses/tos_gauntlet/Blueprint_Notes.md` | Settings / visual plan |
| `/workspace/exam-paper-lenses/drafts/Draft_01.docx` | Source text / structure |
| `/workspace/exam-paper-lenses/renders/draft_01/Draft_01.pdf` | LibreOffice render |
| `/workspace/exam-paper-lenses/renders/draft_01/pages/page_01.png` … `page_16.png` | Every page at render size |
| `/workspace/exam-paper-lenses/figures/*.png` | Every figure source |
| `/workspace/exam-paper-lenses/drafts/Draft_01_Builder_Notes.md` | Disclosures only |
| `/workspace/references/specimen_5086_P1.pdf` | P1 comparison |
| `/workspace/references/specimen_5086_P2.pdf` | P2 spacing / construction class |
| `/workspace/references/specimen_5086_P5.pdf` | Apparatus class for Fig.13.1 |
| `/workspace/references/SPECIMEN_COMPARISON_NOTES.md` | Class mapping |
| `/workspace/exam-paper-lenses/references/grokbot_refraction_example.pdf` | Cover precedent (teacher deviation) |
| Evidence crops | `/workspace/exam-paper-lenses/critic_reports/draft_01_evidence/` |

**Disclosures (mandatory):** LibreOffice render used → **Word pagination untested**. Physical print untested. Lab pilot of Q13 **not performed**. §9.1.1 full spacing measurement table **not present** in Builder package → Critic marks spacing checks **NOT VERIFIED** (acceptance blocked). XSD validation of DOCX parts **not verified**.

---

## 2. Category scores and weighted total

| Category | Weight | Score | Rationale (summary) |
|---|---:|---:|---|
| Diagram quality | 35% | **91.4** | Mean of 18 scored figures; three **critical** geometry defects (Fig.12.1, 14.1, 15.1); Fig.13.1 & Q6 **major** illustration caps at 89; worst-figure gate fails |
| Creativity and originality | 15% | **93** | Reasonable topical contexts; repeated focal-length definitions (Q2 / Q11d / Q15b); Q6 option set mixes categories |
| Question phrasing and exam style | 10% | **94** | Largely specimen tone; orphaned MCQ option blocks harm P1 style; duplicate Fig captions |
| Scientific accuracy and question validity | 15% | **76** | Independent solve finds Q3 non-unique; Fig.12/14/15 scientifically wrong for assessed tasks; Q6/Q3/Q10 stem–option/figure splits |
| Specimen formatting fidelity | 15% | **71** | Multiple §9 FAILs + mandatory **NOT VERIFIED** spacing; calc-line geometry not specimen; `[Turn over` on pp.15–16 |
| Syllabus and paper structure | 10% | **96** | 11(f)–(h) scope held; no thin-lens equation; Sec A visual quotas met; marks 10+61=71; Sec B one-Q-per-page |
| **Overall** | 100% | **87.6** | \(0.35\times91.4 + 0.15\times93 + 0.10\times94 + 0.15\times76 + 0.15\times71 + 0.10\times96 = 87.55\) |

**Gates:** overall ≥99? **NO**. Diagram ≥99? **NO**. Others ≥96? **NO** (science 76, formatting 71, creativity 93, phrasing 94). Every figure ≥98 with every subcriterion ≥96? **NO**. Zero unresolved critical/major diagram defects? **NO**. All mandatory checks verified? **NO**.

→ **TARGET NOT MET — REVISE**

---

## 3. Section A — independent key (all four options evaluated)

| Q | Critic answer | Option audit | Visual role (from paper) | Notes |
|---:|---|---|---|---|
| 1 | **B** | A diverge; B meet at F; C meet at lens; D undeviated | E (4 diagram options) | Unique correct |
| 2 | **C** | A diameter; B object distance; C O→F; D F→2F | N | Unique correct |
| 3 | **NOT UNIQUELY SOLVABLE** | A & D both on principal axis; B = O; C = rim | E | **Critical:** stem asks for “a principal focus”; figure gives no ray/f cue. A at 2.5 cm from O, D at 4.5 cm. Both A and D are defensible without knowing \(f\). Builder intends A |
| 4 | **D** | From figure: far-side inverted shorter image → real, inverted, diminished | E | Unique; rays slightly miss marked F (see figure scores) but characteristics unambiguous |
| 5 | **B** | Screen test | N | Unique |
| 6 | **A** | Stem: larger + upright → virtual. B real; C inverted; D diminished contradict stem | C | Options **orphaned** to top of p.4 (see formatting). Option set not parallel (type vs size/orientation) |
| 7 | **C** | Mechanism / refraction of converging lens | N | Distinct from Q1; unique |
| 8 | **C** | Lens at 5 cm, screen at 15 cm → \(f=10\) cm. A reads lens mark; D reads screen mark; B distractor | E | Unique |
| 9 | **A** | Undeviated through O | N | Unique |
| 10 | **B** | Meeting point P on screen B; A object-side; D before meet; C after diverge | E | Stem on p.4, figure on p.5 — split. Answer unique from figure |

**Letter pattern of Critic key (where unique):** B, C, *(ambiguous)*, D, B, A, C, C, A, B — no single-letter domination among unique items.

### Sec A representation audit (from rendered paper, not Builder claims)

| Item | Figure present? | Essential extraction? |
|---:|---|---|
| 1 | Y | E |
| 2 | N | N |
| 3 | Y | E |
| 4 | Y | E |
| 5 | N | N |
| 6 | Y | C (stem supplies size/orientation) |
| 7 | N | N |
| 8 | Y | E |
| 9 | N | N |
| 10 | Y | E |

**Totals:** figure-based **6/10 (60%)** ≥4; essential **5/10 (50%)** ≥3. **PASS** quotas.

Answer grid present after Q10 on p.5. **PASS** (revision-package expectation).

---

## 4. Section B — independent worked outline

| Q | Marks | Critic outline | Validity |
|---|---:|---|---|
| **11** | 7 | (a) Continue three parallel rays to meet at X. (b) Label X as F. (c) Measure lens→X = **4.0 cm**. (d) Focal length = distance from optical centre to principal focus | Valid; grid readable |
| **12** | 6 | Intended: real, inverted, diminished; \(h_i=1.5\) cm; real because rays meet / can form on screen. **Figure rays do not pass through marked F or O** (see §5) → construction invalid; characteristics from arrow sizes still readable if geometry trusted, but figure fails science gate | **Critical figure** |
| **13** | 8 | (a) Aim at distant tree; adjust screen to sharp; measure lens–screen. (b) Distant object → rays approximately parallel. (c) **15.0 cm**. (d) e.g. repeat / ensure tree truly distant / measure to lens centre | Content OK; apparatus drawing crude vs P5 |
| **14** | 7 | (a) Extend emergent rays back; mark I. (b) virtual, upright, magnified (from correct construction). (c) Rays do not actually meet / cannot catch on screen. **As drawn, upper “parallel” ray bends away from axis** (diverging-lens behaviour) → student construction from figure is scientifically wrong | **Critical figure** |
| **15** | 6 | (a)(b) Standard definitions. (c) Continue ray undeviated through O; label principal axis. **Incident ray is not directed at O** (terminates on lens well above O) | **Critical figure** vs stem |
| **16** | 6 | Object→lens **12 cm**; lens→film **6 cm**; real, inverted, diminished; real | Valid from scale |
| **17** | 7 | (a) Real — sharp image on screen (table). (b) Virtual; upright; larger. (c) Rays meet on screen in Fig.17.1 | Valid; anti-case-recall lock held |
| **18** | 5 | From Fig.18.1 source geometry: \(f_A=4.0\) cm, \(f_B=2.5\) cm; **B** shorter; parallel beam meets closer to lens | Valid if half-square for B is clear at print size |
| **19** | 5 | (a) Ray 1 → through F after lens. (b) Ray 2 through F before → emerges parallel. (c) Ray 3 through O undeviated | Valid construction task |
| **20** | 4 | (a) Camera/projector + real-image reason. (b) Magnifying glass / reading lens + virtual reason | Valid; text-only OK per TOS |

**Mark sum check:** 7+6+8+7+6+6+7+5+5+4 = **61**. Sec A 10. **Total 71**. **PASS** arithmetic.

**Syllabus exclusions:** No \(1/u+1/v=1/f\). Image characteristics tied to figures/tables, not rote object-distance cases (Q12/14/16/17 locks held in wording). **PASS** exclusion intent. Q3/Q12/Q14/Q15 figure defects are validity failures, not exclusion breaches.

**Primary-LO partition:** Matches locked TOS attribution at paper level (not re-derived mark-by-mark beyond spot checks).

---

## 5. Per-figure scores (§6.2)

Subcriteria: Sci 30% | Fidelity 25% | Labels 20% | Print 15% | Integration 10%.  
Caps applied before category mean. Specimen comparison evidence under `critic_reports/draft_01_evidence/`.

| Figure | Role | Specimen class | Sci | Fid | Lab | Print | Int | Raw | Cap / defect | **Final** | Line-art objects (§6.1) |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|
| Q1-A | E opt | P1 Q18/19 | 98 | 96 | 97 | 98 | 97 | 97.2 | — | **97** | N/A schematic |
| Q1-B | E opt | P1 Q18/19 | 99 | 96 | 98 | 98 | 98 | 97.9 | — | **98** | N/A |
| Q1-C | E opt | P1 Q18/19 | 98 | 96 | 97 | 98 | 97 | 97.2 | — | **97** | N/A |
| Q1-D | E opt | P1 Q18/19 | 98 | 96 | 97 | 98 | 97 | 97.2 | — | **97** | N/A |
| Q3 labels | E | P1 Q8 schematic | 88 | 96 | 95 | 98 | 94 | 93.5 | Ambiguous focus points | **94** | N/A |
| Q4 O/I | E | P1 Q9 geometry | 90 | 95 | 94 | 97 | 95 | 93.6 | Rays miss F (~0.4 unit) | **94** | N/A |
| Q6 stamp/eye | C | P1 Q5 everyday | 96 | 72 | 90 | 95 | 88 | 87.6 | **Major** crude objects → cap 89 | **89** | **FAIL** (box stamp; circle eye) |
| Q8 scale | E | P1 Q1 scale | 99 | 95 | 96 | 97 | 96 | 96.8 | Rougher than specimen instruments → soft | **97** | N/A apparatus simple |
| Q10 screens | E | P1 Q18/19+rays | 98 | 95 | 92 | 96 | 90 | 95.0 | Label overlap “lens”/A–D; cosmetic → cap 97 | **97** | N/A |
| Fig.11.1 | E | P2 construction | 99 | 96 | 97 | 97 | 97 | 97.4 | — | **98** | N/A |
| Fig.12.1 | E | P2 ray diagram | **40** | 94 | 95 | 97 | 90 | 77.6 | **Critical** rays miss F & O; inconsistent with lens laws | **58**† | N/A |
| Fig.13.1 | E | P5 Fig.1.1 | 97 | 68 | 88 | 94 | 90 | 86.3 | **Major** crude stand/boss/holder vs P5 → cap 89 | **89** | **FAIL** apparatus fidelity |
| Fig.14.1 | E | P2 virtual construction | **35** | 92 | 94 | 96 | 90 | 74.9 | **Critical:** post-lens “parallel” ray diverges from axis | **55**† | N/A |
| Fig.15.1 | E | P2 simple lens | **30** | 94 | 95 | 97 | 88 | 74.4 | **Critical:** stem says ray toward O; drawn ray not aimed at O | **52**† | N/A |
| Fig.16.1 | E | P2 scaled | 98 | 95 | 96 | 97 | 96 | 96.5 | — | **97** | N/A |
| Fig.17.1 | E | P2 table+figure | 97 | 95 | 94 | 96 | 92 | 95.2 | Duplicate caption | **96** | N/A |
| Fig.18.1 | E | P2 paired | 98 | 95 | 96 | 96 | 95 | 96.3 | Missing ray arrowheads | **97** | N/A |
| Fig.19.1 | E | P2 ray construction | 98 | 96 | 97 | 97 | 97 | 97.1 | — | **98** | N/A |

† Critical geometry: Scientific correctness cannot be marked PASS; figure fails acceptance regardless of mean; numeric score retained for category mean honesty.

**Category Diagram = unweighted mean = 91.4.**  
**Minimum individual figure = 52 (Fig.15.1).**  
**Figures below 98:** Q1-A/C/D, Q3, Q4, Q6, Q8, Q10, F12, F13, F14, F15, F16, F17, F18 (most of register).

**Same-size comparison evidence saved:**  
`cmp_q1_vs_p1q18.png`, `cmp_q6_vs_p1q5.png`, `cmp_q8_vs_p1q1.png`, `cmp_fig13_vs_p5.png`, `cmp_fig12_vs_p2.png`, `orphan_q3_options.png`, `orphan_q6_options.png`, `crop_fig15_ray.png`, plus specimen page greyscales.

---

## 6. Findings table

| ID | Sev | Location | Evidence | Required Builder fix | Status |
|---|---|---|---|---|---|
| F1 | **Critical** | Fig.12.1 / Q12 | Parallel-then-F ray misses F; centre ray misses O (source coords: y@F=5.3 vs 5; y@O=5.75 vs 5). Assessment-bearing geometry wrong | Redraw with exact F/O intersections; re-verify heights (object 3.0 cm, image 1.5 cm) on grid | Open |
| F2 | **Critical** | Fig.14.1 / Q14 | Upper emergent ray from parallel incidence goes **away** from axis (code (7,6.5)→(12.5,8.2)); converging lens must send it through F | Redraw correct emergent rays (parallel→F; through O undeviated); keep student back-extension task | Open |
| F3 | **Critical** | Fig.15.1 / Q15(c) | Stem: ray directed at O; drawn arrow ends on lens **above** O (extend to x=6 → y≈5.13, O at y=3.5) | Redraw incident ray aimed at O; student continues undeviated | Open |
| F4 | **Critical** | Q3 | A and D both on principal axis; no cue for \(f\); more than one defensible MCQ answer | Relabel so only one focus is on-axis at ±f (e.g. mark one off-axis “axis tick”, or show parallel rays meeting at A only) | Open |
| F5 | **Major** | Q3 options pp.2–3 | Options B–D orphaned at top of p.3 (`orphan_q3_options.png`) | Keep stem+figure+A–D together (P1 §14.1) | Open |
| F6 | **Major** | Q6 options pp.3–4 | Stem+figure on p.3; A–D only at top of p.4 (`orphan_q6_options.png`) | Keep stem+figure+options on same page | Open |
| F7 | **Major** | Q10 pp.4–5 | Stem ends p.4; figure+options on p.5 | Keep stem+figure+options together | Open |
| F8 | **Major** | Fig.13.1 | Crude stand/boss/holder vs P5 Fig.1.1 (`cmp_fig13_vs_p5.png`); Builder disclosed risk | Upgrade apparatus illustration (image-gen + verified overlays) to P5 fidelity | Open |
| F9 | **Major** | Fig Q6 | Stamp = labelled box; eye = two circles — below P1 Q5 class (`cmp_q6_vs_p1q5.png`) | Recognisable stamp + eye line art | Open |
| F10 | **Major** | Calc answer lines (e.g. Q11c, Q12b) | `focal length =…cm [2]` left-run; bracket x1≈524.5 pt vs specimen ≈545.7; `=` not at specimen fixed x≈347.3 | Rebuild with specimen right-tab / dot-leader geometry (§9.1.2) | Open |
| F11 | **Major** | §9.1.1 spacing | No scripted specimen↔draft gap table; Builder notes admit unmeasured | Measure P2 gaps; submit PASS/FAIL table; Critic re-measure | Open — **NOT VERIFIED** |
| F12 | **Major** | pp.15–16 footers | `[Turn over` on last printed Q page and BLANK PAGE | Remove on final question page and blank pages | Open |
| F13 | **Minor** | Fig.13.1, 15.1, 17.1, 18.1 | Duplicate “Fig. n.1” (in-image + caption) | Single caption | Open |
| F14 | **Minor** | Q4 / Q10 / Q18 | Missing or inconsistent ray arrowheads; Q10 label collision | Clean labels/arrowheads | Open |
| F15 | **Minor** | Cover | Candidate boxes simplified vs grokbot (Builder disclosed) | Optional tidy; low priority vs Q pages | Open |
| F16 | **Minor** | Creativity | Focal length defined in Q2, Q11(d), Q15(b) | Diversify one definition item | Open |

**Unresolved critical diagram/science defects:** F1–F4 (and F2/F3 are diagram-critical). **Unresolved major diagram:** F8–F9.

---

## 7. §9 Formatting checklist

Renderer: **LibreOffice** → **Word pagination untested**. Tightest page feet (body to footer zone ≈780 pt): **p.2 ≈4.6 pt**, **p.3 ≈6.4 pt**, **p.12 ≈38.7 pt**.

| Check | Result | Evidence / note |
|---|---|---|
| Question-number column / hanging indent | **FAIL** | Orphaned MCQ options (Q3, Q6); Q10 stem/figure split |
| Subpart / nested-part alignment | **PASS** (visual) | Sec B (a)(b)(c) hierarchy present; not ±0.5 pt measured |
| Calculation answer placement | **FAIL** | Not specimen right-tab geometry (F10) |
| Context then command sentence | **PASS** (spot) | e.g. Q11/Q12 command lines separate |
| Visible numerical answer lines | **PASS** | Dotted calc lines visible on render |
| Calculation working space | **NOT VERIFIED** | No §9.1.3 measurement vs specimen medians |
| Written-response space / `[n]` on last dotted line | **FAIL** / partial | `[n]` often on same dotted run but bracket x ≠ specimen 545.7; drawing `[n]` on own line OK |
| Gap text→first answer line | **NOT VERIFIED** | No measurement table |
| Separation between parts | **NOT VERIFIED** | No measurement table |
| Units and mark brackets | **FAIL** | Calc unit/bracket geometry off specimen |
| Fonts / justified text | **PASS** (visual) | Arial-like 11 pt; body generally justified |
| Figures, captions, tables | **FAIL** | Duplicate captions; Q6/Q10 pagination; Table 17.1 OK |
| Overall page density | **FAIL** | p.2–3 cramped (orphan options; ~5 pt foot); p.15 sparse |
| Page integrity / navigation | **FAIL** | `[Turn over` on pp.15–16; even page count 16 OK; BLANK PAGE present; cover page count statement OK |
| Editable Word presentation | **PASS** | DOCX text editable (not full-page raster) |
| Cover / header / footer from Draft_01 | **PASS** with teacher deviation | Strings match TOS (`Topic: Lenses`, `SACSS Topical Worksheet 2026`, `5086 Lenses`); candidate boxes simpler than grokbot |
| XSD / schema hygiene §9.6 | **NOT VERIFIED** | Not reported |

**Any FAIL or NOT VERIFIED mandatory check blocks acceptance.**

---

## 8. Profile / TOS alignment summary

| Check | Result |
|---|---|
| `PAPER_PROFILE` MIXED_REVISION | PASS |
| Sec A ≥40% figures & ≥30% E | PASS (6 & 5) |
| Sec B one top-level Q per new page | PASS (Q11–20) |
| Topic 11(f)–(h) only; no thin-lens equation; no case-table recall as assessed knowledge | PASS (wording); figure defects separate |
| Cover/footer exact strings | PASS |
| Q7 distinct from Q1 | PASS |
| Locked TOS marks / part structure | PASS |
| Pilot / print honesty | PASS (disclosed) |

---

## 9. Decision

### **REVISE**

**Overall: 87.6 / 100.** Diagram 91.4 (gate fail). Science 76. Formatting 71 with **NOT VERIFIED** spacing. Multiple figures below 98; critical geometry on Fig.12.1, 14.1, 15.1; Q3 non-unique.

### Required Builder fixes before Draft_02 (priority order)

1. **Redraw Fig.12.1, Fig.14.1, Fig.15.1** with verified ray geometry; re-solve Q12/Q14/Q15 from the new figures.  
2. **Fix Q3** so exactly one option is a principal focus.  
3. **Keep each MCQ stem + figure + A–D on one page** (Q3, Q6, Q10).  
4. **Upgrade Fig.13.1 and Q6** to specimen-class illustration fidelity.  
5. **Implement specimen calculation-line geometry and `[n]` x-positions**; submit §9.1.1 spacing measurement table; remove `[Turn over` from pp.15–16.

Do **not** produce `Final_Answer_Scheme` until Loop 2 target is met.

---

*Critic evidence directory: `/workspace/exam-paper-lenses/critic_reports/draft_01_evidence/`*  
*End of Draft_01 review.*
