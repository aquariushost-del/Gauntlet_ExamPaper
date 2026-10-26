# Exam Paper Gauntlet — Master Instructions

**Version:** 1.6.1 — §7.1 Cambridge archive inspiration search DISABLED (teacher request); all v1.5.0 rules unchanged
**Updated:** 27 October 2026 (teacher disabled the Cambridge archive inspiration search because of token cost)\
**Workflow:** Builder AI ↔ Independent Critic AI  
**Reference files:** original specimen PDFs for the selected paper: `references/specimen_5086_P1.pdf`, `references/specimen_5086_P2.pdf`, and `references/specimen_5086_P5.pdf` (Physics section only). Each is the gold standard for its own paper type. The P2 Word specimen is secondary for text and structure. The syllabus Markdown remains authoritative for content.

### Changelog

- **v1.6.1:** §7.1 Cambridge archive inspiration search DISABLED by teacher (token cost). Agents must not search, list or open the archive folders. Section kept for possible re-enable. Teacher request.

- **v1.6.0:** Added optional §7.1, inspiration search in the teacher's Cambridge archive. Run it on demand only, as Drive full-text keyword searches scoped to the two folders' year subfolders. Open 3–8 hits per topic, with a hard cap on time and tokens. Never bulk-download, index, OCR or read the archive wholesale. Skip it entirely if the AI cannot search inside those folders. Questions are never copied, content stays inside 5086, diagrams are redrawn under §6, and Critic review is unchanged. Sources may be noted in the build log only. Teacher request.

- **v1.5.0:** Added the supplied original P1 and P5 PDFs and paper-specific requirements (§2.2, §14). P1 Physics scope is questions 1–20; P5 Physics scope is question 1, printed pages 2–7. Added essential visual interpretation quotas and a representation audit, stronger MCQ distractor checks, practical feasibility and data-integrity checks, and specimen comparison notes. Diagram weight increases from 25% to 35%, with creativity 15%, phrasing 10%, science 15%, formatting 15%, syllabus/structure 10%. Overall target remains 99; Diagram quality now requires 99, every individual figure 98 and every figure subcriterion 96. Added failure caps, hard gates and mandatory same-size specimen comparisons. Image generation is an expected route for complex illustrations when it produces closer specimen fidelity; all scientific geometry/readouts remain independently verified. Replaced the universal one-question-per-page rule with paper-specific pagination. Existing P2 answer-space rules and the two-agent/two-loop architecture remain in force for P2.

- **v1.4.3:** For qualitative (written) answers, the mark bracket `[n]` ends the last dotted answer line, on the same line and right-flush at the specimen's x. It is never a separate paragraph below the lines. `[Total: n]` stays on its own right-aligned line below. The reference for this is the specimen PDF as printed (§9.1.2, §9.2). Teacher ruling after the 5086/02 v4 review. Follow-up: the teacher's **original specimen PDF is now the gold standard** for layout, spacing and mark-bracket placement, and the specimen DOCX is secondary, kept for text and structure (§2, §9.1). The 5086 line-end values were corrected from that PDF: lines end 544.9 pt, the last line's dots stop at 529.6 pt with `[n]` ending 545.7 pt, and the subpart line start is 117.6 pt. A labelled answer group puts `[n]` on its own line below (§9.1.2, §9.2). The PDF is committed as `references/specimen_5086_P2.pdf`.
- **v1.4.2:** Calculation answer lines follow the specimen's measured geometry: label right-aligned so the equals sign ends at one fixed x, dotted run filling from the equals sign to the unit, then a space and the mark bracket right-flush at one fixed x, built with a right tab and a right-aligned dot-leader tab (§9.1.2, §9.2). Context or data comes first and the command sentence starts on its own new line at the same indent, with the specimen's spacing (§9.1.2, §9.2). Teacher request after the 5086/02 v3 review.
- **v1.4.1:** People, animals and everyday objects in figures must be recognisable, specimen-accurate line art, never placeholder shapes. Image generation is allowed but must be cleaned up to black-and-white exam line art, and physics-relevant geometry stays vector-drawn (§6.1). Realistic line art is now an explicit scored criterion in the Diagram quality category (25% at that version): placeholder shapes are a scored defect, and the Critic checks it per figure (§5, §6.1, §10). Teacher request after the 5086/02 Q3 slide figure.
- **v1.4:** Added the strict specimen spacing gold standard (never below the specimen; at most 0.5 pt above) with a measured style sheet and a 5086 worked example (§9.1.1–9.1.2), working space from specimen medians per mark (§9.1.3), dotted-line start/end rules, justified text, every question on a new page (universal) and even page count (§9.2), school branding as a project setting with cover effort deprioritised (§2.1, §9.4), cover/header/footer checks from Draft_01 (§9.3, §10), editable stacked notation (§9.5), generator hygiene with schema order, XSD validation and pixel diffs (§9.6), the Word-pagination disclosure (§12) and teacher-authorised rounds beyond the limit (§4, §10, §12, §13). Lessons from the 5086/02 SACSS Preliminary 2026 project.
- **v1.3:** 99/96 acceptance thresholds, mandatory specimen-formatting verification and Google Drive output.

## 1. Mission

Create a **complete, original, syllabus-compliant examination paper** that closely matches the supplied specimen's professional examination style and formatting. Particularly prioritise **exceptional diagrams**, **creative and original questions**, and **authentic specimen-style phrasing**.

Deliver three editable Microsoft Word documents: the approved Table of Specifications (TOS), the final examination paper, and the final answer scheme; also retain a documented review trail and numbered drafts. The answer scheme is created **after** the paper passes Loop 2, not within its Gauntlet.

**Acceptance target:** overall weighted quality score **≥ 99/100**, Diagram quality **≥ 99/100**, every other category **≥ 96/100**, every individual figure **≥ 98/100** with every figure subcriterion **≥ 96/100**, **zero unresolved critical or major diagram defects**, and all required checks verified. These rubric scores are internal evidence-based assessments, **not** a scientifically calibrated percentage of quality or a guarantee of perfection. Final teacher moderation remains necessary.

## 2. Inputs and precedence

1. **Explicit user instructions and approved paper specification** define the requested paper, structure, sections, marks, topics to include or exclude, and other constraints.
2. **Syllabus Markdown (`.md`)** is authoritative for examinable knowledge, skills, learning outcomes and topic boundaries. Read the **entire file**, including tables and nested lists. Do not invent syllabus requirements.
3. **Original specimen PDF for the selected paper (as printed)** is the **gold standard for layout, spacing, diagrams and the applicable answer/option conventions**. Measure that paper’s geometry and relevant layout classes, including line/mark-bracket positions for structured/practical answers and A–D arrangements for P1. Where its PDF and a converted DOCX disagree, the PDF wins. Never use P2 as the sole reference for P1 or P5.
4. **Specimen Word (`.docx`)** is **secondary**: the backup source for text, structure where consistent with the requested specification, wording, command words, diagram conventions and editable structure. It is often a PDF-to-Word conversion, so its layout values (indents, tabs, line ends, bracket paragraphs) and any LibreOffice render of it can be distorted. Keep it; never use it to override the PDF on layout.

When sources conflict, honour explicit user constraints on the intended paper and the syllabus on examinable content; document any unresolved conflict. Do not assume the specimen's exact question content or contexts should be reused.

### 2.1 Project settings

Record these settings in `Blueprint_Notes.md` at the start of Loop 1, and apply them throughout:

| Setting | Meaning | Example (5086/02, 2026) |
|---|---|---|
| `SCHOOL_NAME` | Short school name, printed on the cover and in every footer | `SACSS` |
| `EXAM_TITLE` | Examination title, printed on the cover and in every footer | `Preliminary Examination 2026` |
| `PAPER_CODE` | Syllabus/paper code shown in the footer and on the cover | `5086/02` |
| `PAPER_PROFILE` | Applicable rules and reference pages; set separately for mixed sections | `P1`, `P2`, `P5_PHYSICS`, `MIXED_REVISION` |
| `VISUAL_PLAN` | Planned essential/contextual visuals and their allocation by topic | 40 MCQs: at least 16 figure-based, including at least 12 essential-reading items |
| `TEACHER_DEVIATIONS` | Deliberate, teacher-requested departures from the specimen, recorded as they are made | SACSS cover lines in place of the MOE/Cambridge lines |

A teacher-requested deviation is not a defect. Builder records it in the Builder notes, and Critic verifies that it was applied as requested rather than scoring it against the specimen. List all deviations in the final quality report.

### 2.2 Select the paper profile before planning

Read §14 before writing the TOS. Record `PAPER_PROFILE` as `P1`, `P2`, `P5_PHYSICS`, or `MIXED_REVISION`, and record the applicable specimen pages. For mixed revision, apply P1 to MCQs and P2 to structured questions; include P5 only when practical tasks are requested. User topic/count/mark instructions take precedence over official-paper structures.

**Profile-specific rules override P2-specific examples and legacy universal wording elsewhere in this file.** Never transfer P2 dotted answer spaces, calculation-line coordinates, section choices, mark totals, or one-question-per-page pagination to P1. Never transfer P2 answer-space allowances or forced page breaks between every part to a P5 procedural investigation. Measure the selected paper's PDF directly. The 0.5 pt one-sided spacing rule applies to the matching layout class in that paper, not to an unrelated P2 example.

For each paper or section, compare the planned balance of text, essential visual interpretation, contextual figures, graphs, tables and diagram options with the appropriate specimen. An attractive figure does not prove that students must read it. Absence of an official quota is not permission to produce a text-only Physics MCQ paper.

## 3. Exactly two AI roles

### Agent 1 — Builder AI

- Extract a paper blueprint from the supplied materials before writing questions.
- Analyse specimen wording, command words, mark brackets, sections, fonts, spacing, headers, footers, tables, diagrams and answer spaces.
- Inspect converted DOCX for fragmented paragraphs, floating text boxes, misplaced images and other conversion artifacts; repair these rather than reproducing errors.
- Create genuinely original, engaging and fair questions aligned with syllabus outcomes and the requested assessment objectives/difficulty.
- Create technically precise, examination-grade diagrams and integrate them into questions.
- Produce the TOS and examination paper as editable DOCX documents. **Only after Loop 2 is complete**, produce the final detailed answer scheme in DOCX; there is no answer-scheme Gauntlet.
- Correct Critic findings while retaining approved content and preserving earlier drafts.
- Never grade or approve its own submission.

### Agent 2 — Independent Critic AI

- Examine the actual paper, reference materials and approved TOS, **not just the Builder's claims**. The final answer scheme is not a Loop 2 deliverable.
- Independently solve questions during the examination-paper quality review to verify question validity and correct marks, and trace every question to syllabus outcomes. This is not a review of a separately authored answer scheme.
- Challenge creativity, originality, difficulty, clarity, fairness and specimen-style phrasing.
- Inspect **each diagram individually** for accuracy, legibility, convention, quality and print suitability.
- Render DOCX pages, inspect every page and compare its conventions and appearance with the specimen.
- Score using the rubric and issue actionable, location-specific defect reports.
- Recheck the **entire** revised set after each round and look for regressions.

**Agent separation:** In ChatGPT Work, delegate the Critic to a genuine specialist subagent with its own context when available; give it the specimen, syllabus, quality rubric, approved TOS and actual draft, not the Builder's self-evaluation. A coordinating workflow does not count as a third specialist role. If delegation is unavailable, use clearly separated build/review passes and explicitly report that this is **not fully independent agent review**. Never claim two independent agents ran unless they really did. Do not fabricate tests or tool use.

## 4. Mandatory two-loop architecture (same two agents)

There are **exactly two AI roles**, Builder AI and Independent Critic AI, operating in **two sequential Gauntlet Loops**. Do not invent a third manager, approver, diagram agent or specialist agent. Ordinary scripts may validate totals, manage filenames and render documents; they are not AI agents.

### LOOP 1 — TOS / Examination Blueprint Gauntlet (before writing questions)

**Hard gate:** The Builder must **not draft the examination questions** until the Critic has approved the TOS. Planning short question descriptions is permitted; writing fully developed question stems or producing the finished paper is not.

1. Builder reads the complete applicable specimen and syllabus references and extracts subject, level, duration, section structure, choice rules, attempted vs authored marks, topic exclusions, specimen question conventions and relevant learning outcomes.
2. Builder creates a **question-by-question and, where useful, sub-question-by-sub-question TOS** with these fields: section; question/part number; topic/subtopic; exact syllabus learning-outcome ID or text; planned marks; assessment objective and cognitive demand; intended difficulty; one-line question concept and proposed real-world context; intended data/table/graph/diagram; response type; specimen phrasing conventions to emulate. Add `representation` (text, instrument reading, diagram, graph, data table, diagram options), `visual role` (essential, contextual, none), the exact information a student must extract, and the relevant specimen comparison. For P1 add a planned distractor misconception for each wrong option; for P5 add the assessed practical skill, apparatus, controlled variables and practical feasibility status. Show marks by topic and assessment objective, plus actual visual counts by section and topic; do not combine P1 and P2 counts to disguise a text-only MCQ section.
3. Builder verifies mathematical totals, including **authored marks vs candidate-attempted marks when optional questions exist**, per-section totals, choice rules, mark distributions, syllabus coverage and reasonable paper duration. Distinguish must-cover requirements from discretionary topic selection.
4. Save the initial blueprint as `TOS_Draft_01.docx` (and a concise `Blueprint_Notes.md` if useful). The Critic reviews **against the actual specimen, syllabus and explicit user constraints**, not the Builder's claims. It checks learning outcomes, balance, originality of intended contexts, difficulty, paper structure, feasibility of diagram plans, assessment objectives, marks and choice arithmetic.
5. Critic produces `TOS_Draft_01_Review.md` listing each issue by row/question, evidence, severity, precise correction, and decision `APPROVED`, `REVISE` or `NOT VERIFIED`. Builder corrects and saves `TOS_Draft_02.docx`, etc.; Critic rechecks the complete blueprint.
6. **Loop 1 passes only with 100% compliance with all mandatory blueprint checks, including the profile-specific representation audit, zero critical defects and no unresolved mandatory NOT VERIFIED items.** This is a hard checklist gate, not the 99%-weighted paper score. Maximum **three TOS review rounds**.
7. When approved, preserve the TOS as `TOS_Approved.docx` and record `TOS_Approval_Report.md` with the approval round and evidence. The approved TOS becomes the **locked blueprint** for Loop 2. If three rounds do not pass, stop paper production and return the latest TOS and review reports for teacher decision; do not silently move to Loop 2.

### LOOP 2 — Complete Exam Paper Gauntlet (only after Loop 1 approval)

1. Builder works from `TOS_Approved.docx`, creating a fully editable paper and professionally drawn, scientifically correct diagrams based on the approved TOS. It must independently check the intended answers while drafting, but **must not produce the formal answer scheme until Loop 2 has met its quality target**.
2. Critic independently reviews the examination paper against the **weighted quality bar in Section 5**, approved blueprint, syllabus and specimen. It independently works every question to detect invalid or ambiguous questions, checks all figures and mark totals, and visually inspects each rendered page. No formal answer scheme is required at this stage.
3. Save each paper iteration as `Draft_01.docx`, `Draft_02.docx` and so on with its corresponding reviewed TOS-alignment record and Critic report. Revise and reassess the full deliverable package in each round, checking for regressions.
4. Loop 2 achieves its target only at **≥99/100 overall, Diagram quality ≥99/100, every other category ≥96/100, every figure ≥98/100 with each figure subcriterion ≥96/100, zero unresolved critical or major diagram defects, and all mandatory checks verified**. Maximum **five full-paper review rounds**. If not achieved, deliver the best verified draft and honest outstanding-issues report. **Exception:** if the teacher explicitly asks to continue past the limit (for example, "loop until everything's perfect"), further rounds are allowed. Each extra round keeps the same thresholds, never overwrites drafts, and is recorded in the Builder notes, the Critic report and the final quality report as beyond the limit at the teacher's instruction. Builder and Critic must never extend the limit on their own initiative.
5. If drafting exposes a need to change the **approved topics, question marks, assessment-objective distribution, section structure or choice rules**, update the TOS and **return to the Loop 1 Critic for renewed approval before making that substantive paper change**. Minor wording, diagram placement and formatting changes that preserve the locked blueprint do not require TOS reapproval.
6. Keep the TOS aligned with the paper and reapprove any substantive blueprint changes. **After Loop 2 concludes successfully**, Builder alone creates `Final_Answer_Scheme.docx`, with full model answers, calculations, units, marks per part, acceptable alternatives and partial-credit guidance as appropriate. No third Gauntlet loop, quality score, or independent Critic review of the answer scheme is required. If Loop 2 does not pass, the answer scheme may be produced only if the user explicitly requests it, and it must be labelled draft.

**Loop 1 does not consume the five full-paper rounds.** Both loops run autonomously without routine user approval; teacher/moderator sign-off remains the final human step.

## 5. Weighted quality bar

| Category | Weight | Core evidence |
|---|---:|---|
| Diagram quality | **35%** | Every figure separately scored against an adjacent same-size specimen crop; scientific geometry, professional illustration, labels and print clarity; worst-figure gate (§6) |
| Creativity and originality | **15%** | Distinct contexts and reasoning; no superficial specimen rewrites |
| Question phrasing and exam style | **10%** | Command words, precision, concision, scaffolding, figure references |
| Scientific accuracy and question validity | **15%** | Independently worked answers, correct data/units, unambiguous solvability and defensible mark allocation |
| Specimen formatting fidelity | **15%** | Measured DOCX properties, direct rendered specimen comparison, and all Section 9 mandatory checks passed |
| Syllabus and paper structure | **10%** | Outcome mapping, exclusions, section/mark totals, blueprint compliance |
| **Total** | **100%** | |

For each category, Critic must use explicit subchecks, cite question/page/figure locations, and give a category score from 0–100. Calculate:

`Overall score = Σ(category score × category weight / 100)`

**Required to meet target:** weighted total ≥99; Diagram quality ≥99; all other categories ≥96; every individual figure ≥98 and all its subcriteria ≥96; no unresolved critical or major diagram defects; all mandatory checks completed. High scores elsewhere cannot compensate for a weak figure or missing essential-visual coverage. A `NOT VERIFIED` mandatory check blocks acceptance, however high the numeric score. Never manipulate scores to reach the threshold.

### Severity

- **Critical:** out-of-syllabus content; scientifically incorrect or misleading essential figure; invalid or unanswerable question or materially incorrect mark allocation; broken section/mark totals; ambiguity preventing fair marking; missing essential question/figure.
- **Major:** substantially weak figure, unclear question, significant style/layout deviation, poor assessment balance, serious TOS inconsistency.
- **Minor:** small typographic, stylistic or alignment inconsistency with no material impact.

All critical defects must be resolved; address major/minor defects according to the scoring rubric and documented acceptance rules.

## 6. Diagram standard — highest priority (35%)

Create diagrams **comparable to or better than the matching specimen in illustration quality, clarity and technical accuracy**. Merely being recognisable and scientifically readable is insufficient. A generic rectangle with circles is not automatically an acceptable laboratory trolley; a few arbitrary lines are not an acceptable stand, clamp, stopwatch or everyday machine.

Before rendering the paper, create a figure register: ID, question, visual role, assessed extraction, comparable specimen figure/page, production method, intended print size, and source file. Every essential figure and every diagram option must be present in the TOS. Then apply these requirements:

- Prefer precise **editable vector graphics** where practical, otherwise high-resolution print-safe PNG; avoid full-page rasterisation.
- Black/greyscale lines on white; clean sans-serif labels; consistent stroke weight; accurate leaders, arrows and arrowheads. No unnecessary colours, gradients, shadows or decoration.
- Scientific conventions must be correct: e.g. circuit symbols and connections; physically consistent rays, normals and angles; correct forces/arrows; appropriately labelled axes, units, scales and graphs; credible apparatus geometry.
- Keep label positions, line intersections, page size and printed readability under control; no overlapping text, cropped figures or blurry edges.
- Figures must serve the assessment, be properly referenced/numbered, and must not inadvertently reveal the answer.
- Critic must check **every** figure at actual rendered/printed size and record issues per figure. A scientifically wrong essential figure is **critical**.

### 6.1 People, animals, apparatus and everyday objects (scored criterion)

- People, animals and everyday objects in a figure (a child on a slide, a fish on a hook, a cooler box, a hand holding apparatus) must be drawn as **recognisable, accurate line art in the style of the specimen's figures**. Correct proportions and pose for the situation, thin uniform black outlines, white fill, no shading or colour. **Never use simple placeholder shapes**, for example a circle on a rectangle standing in for a person.
- **Use image generation when it can produce a closer match to the specimen than the available manual illustration.** For complex real objects, people, recognisable laboratory apparatus or commercial instruments, explicitly consider it; if the deterministic sketch looks crude, use image generation or a properly drawn vector illustration rather than repeatedly approving the same weak sketch. Prompt with a relevant specimen crop as a style reference when available and appropriate, requesting original technical line art, accurate structure/proportions, white background, controlled greyscale and no decorative effects. Record the method and why it meets the specimen. Image generation is not required for an exact circuit, graph, scale or simple abstract physical model that is better drawn deterministically.
- Generated artwork must be inspected and corrected using image editing/regeneration or vector redrawing. Remove false labels, invented parts, broken outlines, accidental textures and decorative effects. Add verified labels separately in editable Word/vector text wherever practical. Retain the source and version history. A generated image is never accepted merely because the tool succeeded.
- All assessment-bearing geometry, instrument digits/ticks/menisci/pointers, graph coordinates, circuit topology, rays, dimensions and force/field arrows must be constructed or independently checked against exact intended values. Prefer deterministic overlays for these features. Do not rely on generated text or an approximately correct scale. A convincing-looking but numerically wrong readout is a critical defect.
- Use native vector geometry or a print-safe raster of at least 600 dpi at its final placed size for line art. Resolution is a floor, not evidence of good drawing. Check line weights, recognisability and labels at the final printed size. Do not thicken or enlarge artwork merely to hide poor linework.
- **Physics-relevant geometry stays vector-drawn**: slopes, heights, distances, angles, rays, force arrows, circuits, scales and dimension lines. A drawn or generated figure must sit on that geometry at the stated position. It must not change the geometry or overlap any label, arrow or dimension line.
- **Critic scoring guidance:** professional illustration fidelity is an explicit requirement of the Diagram quality category (35%). Record a PASS/FAIL comparison for every depicted person, animal, apparatus or everyday object. Apply the stricter per-figure scoring, caps and acceptance blocks in §6.2; a placeholder is never downgraded to a harmless minor observation.

### 6.2 Individual figure scoring and non-negotiable gates

Critic scores **every figure separately**, including the members of a multi-panel figure and all four diagram options in an MCQ. Record scores, defects, comparison page/crop and evidence, then compute a figure score:

| Figure subcriterion | Weight | Evidence required |
|---|---:|---|
| Scientific correctness and exact geometry | 30% | Independently verify every value, mark, connection, scale, direction and relevant proportion. |
| Specimen illustration fidelity and completeness | 25% | Compare actual object/apparatus structure, recognisable components, natural proportions, linework and abstraction level with a relevant specimen figure. |
| Labels, leaders and conventions | 20% | Correct sans-serif labels, units, symbols, arrowheads, leaders and legible positions; no answer leakage. |
| Printed clarity and reproduction | 15% | Final-size greyscale page inspection and 100% crop; adequate resolution/line weight; no clipping or merged details. |
| Integration and visual consistency | 10% | Balanced placement, consistent scale across options, coherent stroke/label styles, no accidental visual cues. |

`Figure score = sum(subcriterion score × weight / 100)`.

Acceptance requires **each figure ≥98/100**, **each subcriterion ≥96/100**, and the paper's Diagram quality category **≥99/100**. Report the minimum individual figure score as well as the category score. The category score is the unweighted mean of individual figure scores (all figures count); simple or excellent figures cannot rescue a figure below its minimum. For a wholly text-only, teacher-authorised assessment, mark the criterion N/A with a documented rationale and explicitly report how the remaining weights are normalised. Do not mark it N/A to evade §14.1 in a Physics MCQ paper.

Apply these caps before calculating totals:

- Wrong scientific geometry, incorrect assessment-bearing readout, missing essential information, or more than one defensible MCQ option because of a figure: **critical**, acceptance blocked regardless of numeric score; Scientific correctness cannot be marked PASS.
- Placeholder objects, distorted/missing functional apparatus parts, conspicuously crude drawing, or obvious mismatch to specimen illustration standard: **major**, figure score capped at **89**, acceptance blocked. If the figure is misleading, classify it as critical instead.
- A drawing that is recognisable and readable but plainly rougher or more schematic than the matched specimen: figure score capped at **95**; redraw it. A “not to scale” label does not excuse weak illustration or wrong relationships.
- Any unresolved visible cosmetic defect (stray mark, inconsistent arrowhead, awkward leader, label collision or uneven option layout): figure score capped at **97** until corrected. Label collisions affecting interpretation are major/critical rather than cosmetic.
- Missing actual-size inspection or missing direct specimen comparison: **NOT VERIFIED**, acceptance blocked. Do not invent a score in place of inspection.

A simple block, point mass, ray diagram or schematic circuit is legitimate when that is the intended scientific representation and its simplicity matches an appropriate specimen convention. Calling a crude real-world object a “schematic” does not waive the gate.

### 6.3 Mandatory comparison and print inspection

For **each figure**, place a crop of the produced page beside a relevant specimen crop at comparable physical size. Compare technical finish, components, proportions, line density, labels and leaders; document specific similarities/differences. For a new subject/context absent from the specimen, select the closest apparatus/illustration class and explain the comparison; do not claim the specimen contains a figure that is not there. Contact sheets are navigation aids only; they cannot replace readable per-figure inspection.

Inspect the source asset, its placement in the rendered DOCX page and its final-size greyscale output. Test that any instrument reading, graph or option difference remains unambiguous after ordinary greyscale printing. Where access to an actual printer is unavailable, state that physical print reproduction is untested; do not describe a screen preview as a physical print test. Check inline-image paragraph height so exact text line spacing cannot clip the figure. Recheck every changed figure and its page after each revision and inspect unchanged pages or establish that their renders are identical.

Distinguish **E: essential extraction**, **C: contextual illustration**, and **N: no visual**. An E item requires a student to obtain a number, relationship, orientation, connection, pattern or reading from the image or its diagram options. If the text supplies all the same information and the student can answer unchanged with the image removed, it does not count as E. A text description of an absent graph never counts as a graph-reading question. A supplied blank graph grid counts as a construction task, not as an interpretation item.

## 7. Creativity (15%) and question phrasing (10%)

**Creativity:** Invent new syllabus-appropriate tasks and varied scenarios, including simplified real-world applications when genuinely useful. Avoid substituting only names, objects or numeric values into specimen questions. Keep contexts concise, fair and age-appropriate; creativity must not push content beyond the syllabus or introduce gratuitous reading load.

**Phrasing:** Match the specimen's formal tone, language economy, command-word usage (`state`, `describe`, `explain`, `calculate`, `determine`, `suggest`, etc.), sentence structure, scaffolding, multipart organisation, numerical symbols/units and references to figures/tables. Match **style**, not exact wording. Avoid ambiguous pronouns, chatter and overlong narratives.

Critic assesses representative phrasing against the specimen and checks for repetition and shallow modifications across **all** questions.

### 7.1 Optional: Inspiration search in the Cambridge archive — DISABLED

**STATUS: DISABLED (v1.6.1, teacher request). Do NOT search, list, open or reference the Cambridge archive folders or any 2002–2026 past papers. Skip this section entirely. Only the teacher can re-enable it.**

The teacher keeps two Google Drive folders of thousands of text-searchable Cambridge (non-5086) physics papers (e.g. 0625, 5054): [Folder 1](https://drive.google.com/drive/folders/1vQAkb8fLgZ7PhFG8axvUo15BidlKCEIA) (`1vQAkb8fLgZ7PhFG8axvUo15BidlKCEIA`) and [Folder 2](https://drive.google.com/drive/folders/1bjXoxLw_sxlpI-lHEObO3wFgmQNfxX-i) (`1bjXoxLw_sxlpI-lHEObO3wFgmQNfxX-i`), both accessible to `imran.skadir@gmail.com` (the Drive account connected to the Builder). Use them **only for inspiration**: fresh real-life contexts, diagram ideas and question angles. This step is **optional and must never block the Gauntlet.**

**Capability check first.** If you cannot run Drive full-text search scoped to these folders (no Drive connector, no `fullText contains` with a parent filter, no access to the account), **skip §7.1 entirely**. Do not work around it by downloading, crawling or listing files. Note "§7.1 skipped: no scoped search" in `Blueprint_Notes.md` and continue.

**Query syntax (tested 25 Oct 2026).** Papers sit in **year subfolders** (2002–2026), and `parentId` matches direct children only, so a search on the top folder returns nothing. Once per project, list the year subfolders (`mimeType = 'application/vnd.google-apps.folder' and (parentId = '<FOLDER_1_ID>' or parentId = '<FOLDER_2_ID>')`), then search 2–4 chosen years:
`fullText contains 'acceleration' and title contains '_qp_' and (parentId = '<YEAR_FOLDER_ID>' or parentId = '<YEAR_FOLDER_ID>')`
(`_qp_` keeps question papers and drops mark schemes `_ms_` and examiner reports `_er`.)

**On demand, per topic, small sample:**
1. Search only when planning a specific topic in Loop 1 (TOS contexts) or drafting it in Loop 2. Never pre-scan the archive.
2. Run 1–3 keyword queries. Example keyword sets:
   - Kinematics: `'velocity-time graph'`, `'stopping distance'`, `'terminal velocity'`
   - Moments/pressure: `'moment' and 'pivot'`, `'hydraulic'`
   - Thermal: `'specific heat capacity'`, `'thermal conduction'`
   - Waves/light: `'critical angle'`, `'converging lens'`
   - Electricity/magnetism: `'potential divider'`, `'electromagnetic induction'`
3. Open **3–8 hits** in total and skim only the relevant questions, not whole papers.
4. **Stop** once you have 2–4 usable ideas, or after about 10 minutes / one modest token budget per topic, whichever comes first.

**Never:** bulk-download, export, index, OCR, summarise or read the archive wholesale; page through all results or folder listings; or search topics not currently being set.

**Use rules:**
- Never copy questions, stems, data sets or diagrams verbatim or near-verbatim. Rewrite in a fresh context with new numbers and structure (§7).
- Keep everything strictly within the 5086 syllabus (§2). Drop out-of-syllabus content even if the source includes it.
- Redraw any diagram idea from scratch under §6. Critic review and all gates are unchanged; inspired questions get no allowance.
- Optionally record in the Builder notes/build log which source paper inspired which question, for originality checks. **Never** put this on the student paper or answer scheme.

## 8. Scientific accuracy, question validity, syllabus and structure

- Critic independently solves **every question and part**; checks formulas, numbers, units, assumptions, scientific principles, diagrams and graph interpretations.
- During Loop 2, validate question answers and the marks available, without creating a separate formal answer-scheme document. After paper acceptance, Builder prepares the full answer scheme with every mark, clear working, units, acceptable alternatives and partial-credit guidance where appropriate.
- Verify every question's learning-outcome mapping, permitted knowledge/skills, difficulty/assessment objectives and required exclusions.
- Check section totals, choice rules, question numbering, time suitability, paper total and full TOS consistency.
- Never assume a creative context justifies out-of-syllabus science.

## 9. Specimen formatting fidelity — mandatory gate (15%)

A readable paper is not sufficient evidence of specimen fidelity. The Builder must reproduce the specimen's layout conventions, and the Critic must verify them directly. **Formatting retains its 15% weight and must score at least 96/100. Every mandatory formatting check must also pass independently of the numeric score.**

### 9.1 Establish the specimen layout before drafting

Use the selected profile (§2.2, §14). Numerical values in the P2 worked example below are **P2 only**. Measure P1 option arrangements and item spacing from P1, and P5 procedural/result/graph layouts from P5. Mark genuinely inapplicable checklist items N/A with reasons; never treat them as automatically passed.

Measure the original specimen PDF (the gold standard, §2). Read the specimen DOCX for text and structure only; a render of it may shift line ends and mark brackets. A supplied specimen screenshot can support visual comparison, but differently scaled screenshots cannot establish exact font sizes or dimensions.

Record a specimen style sheet with evidence: page size and margins; font family and size; line and paragraph spacing; question-number, stem, subpart and nested-part positions; answer-line start/end positions; calculation-answer alignment; unit and mark-bracket positions; figure/caption conventions; headers, footers and page numbers. Record measured values where available and identify any uncertain conventions. Repair conversion artifacts rather than copying them.

#### 9.1.1 Spacing gold standard: measure the specimen first

The specimen is the **gold standard for vertical and horizontal spacing**. Before Draft_01, Builder measures the **original specimen PDF** (§2), using text, line and character bounding boxes. Do not use DOCX values or a LibreOffice render of the specimen DOCX as the reference: on the 5086 specimen that render moved line ends by up to 15 pt and the subpart line start by 2.4 pt. Builder records the results in the specimen style sheet, giving the median for each gap and the pages sampled:

- question text (last line) to the first dotted answer line;
- dotted-line pitch (line to line);
- answer area (last dotted line or answer group) to the next part;
- answer area to the next subpart, or to `[Total: n]`;
- section heading, section instruction and first question stem positions on a section's first page;
- dotted-line start and end x-positions for each indent level;
- header and page-number position and body start;
- calculation working space for each mark value (§9.1.3).

**Spacing rule (strict, one-sided):** no gap or space in any draft may be **below the specimen value, by any amount**. Each measured gap must be **at least the specimen value and no more than 0.5 pt above it** (specimen ≤ draft ≤ specimen + 0.5 pt). The 0.5 pt tolerance applies on the loose side only. A gap 0.1 pt smaller than the specimen is a FAIL. If content does not fit, move it to the next page; never compress it. Builder checks every part, not a sample, with a scripted measurement table (one row per gap: specimen value, draft value, PASS/FAIL), and submits the table with each draft. Critic re-measures independently.

#### 9.1.2 Worked example: 5086 Science (Physics) Paper 2 specimen

Horizontal answer-line and bracket values were measured on the original specimen PDF (`references/specimen_5086_P2.pdf`, v1.4.3). Pitch, text→first line, answer→part and answer→`[Total]` were re-verified on that PDF (26.0 / 26.0–26.2 / 38.8–38.9 / 26.0 pt; the 39 pt part target is kept because it is not below the PDF). The remaining rows come from the earlier LibreOffice render of the specimen DOCX; re-check them on the PDF when next used. Use these values only for that specimen. Measure any other specimen afresh.

| Property | Specimen value |
|---|---|
| Page and margins | A4; 1.50 cm left and right margins |
| Font | Arial 11 pt |
| Indents (question number, stem / part / subpart / nested) | 0.25 / 1.05 / 1.85 / 2.65 cm |
| Dotted-line pitch | 26 pt |
| Question text to first dotted line | 26 pt |
| Answer to next part | 39 pt |
| Answer to next subpart or `[Total]` | 26 pt |
| Section heading / instruction / first stem (text top from page top) | 62.5 / 88.5 / 114.5 pt |
| Calculation working space for [1] / [2] / [3] (medians) | 52 / 78 / 105 pt |
| Dotted-line start x (part / subpart) | 95.0 / 117.6 pt |
| Dotted-line end x (every line except the last line of a plain written answer, including every line of a labelled answer group) | 544.9 pt |
| Header page number (bold, start x, text top) | x 291.6 pt, 37.2 pt; body starts at 62.5 pt |
| Calculation answer line (page x) | `=` right edge 347.3 pt (label start varies with label length); dots from the `=` to the unit; unit right edge 530.2 pt; one space; mark bracket 533.2–545.4 pt; with no printed unit the dots run to the bracket |
| Qualitative answer: last dotted line and `[n]` (page x) | Earlier lines end at 544.9 pt. On the last line the dots stop at 529.6 pt and `[n]` follows at 533.4–545.7 pt on the **same line**, as printed in the gold specimen PDF (e.g. p.8 Q5(b) "State two characteristics …": two dotted lines, `[2]` ending the second; all 13 plain written answers in the PDF do this) |
| Labelled answer group (`wave 1 …`, `use …`) and drawing/graph items | Every labelled line runs to 544.9 pt; `[n]` is on its **own right-aligned line** directly below (glyph top 13.0 pt below the last line, right edge 545.7 pt), then `[Total: n]` 26 pt below that (gold PDF p.4 `[4]`, p.7 `[2]`, p.12 `[2]`) |
| `[Total: n]` right edge (page x) | 545.7 pt |
| Command sentence after context/data | New line at the part's text indent (x 95.1 pt for a part); glyph-top to glyph-top pitch 26.1 pt from the last context line (one blank line) |

#### 9.1.3 Calculation working space

Working space is the blank space between the end of the question text and the calculation answer group. It is **at least the specimen median for the part's mark value** (measured as in §9.1.1) and no more than 0.5 pt above it, except for the multi-step allowance below. In the 5086 example these are [1] 52 pt, [2] 78 pt and [3] 105 pt. Add extra space only for a genuine multi-step chain, for example three dependent calculation steps; record the reason for each such part, and keep the addition small (5086/02 used 118 pt for its three-step [3] parts). Do not add space generally, and never set it below the median, by any amount, to save a page.

Use the uploaded DOCX as the starting template when technically practical. Otherwise recreate its verified conventions using Word paragraph styles, hanging indents, tab stops or borderless tables. Do not rely on repeated spaces for alignment. Preserve editable Word text and tables; retain editable diagrams where feasible without reducing quality. Different content may require different pagination, but must retain the specimen's layout conventions.

### 9.2 Mandatory Builder and Critic checklist

| Check | Required formatting and verification |
|---|---|
| Question-number column and hanging indent | Place the question number in its own left position and the stem at the specimen's indented position. All continuation lines align with the stem, not the number. Check every question. |
| Subpart and nested-part alignment | Align `(a)`, `(b)`, etc. with the specimen's subpart position and indent their text consistently farther right. Apply the specimen's separate hierarchy to `(i)`, `(ii)`, etc. Check wrapped lines as well. |
| Calculation answer placement | Measure every calculation answer line in the specimen first (label start, `=` end, dotted run start and end, unit, bracket x0/x1) and copy its geometry exactly. Where the specimen uses a right-side answer group (as 5086 does): **(1)** the label is right-aligned so the **equals sign ends at one fixed x on every line**, so the label's start varies with its length; **(2)** the dotted run starts immediately after the `=` and **fills to the unit**, so its length depends on the unit's width, never on the label's; **(3)** the unit is followed by one (no-break) space and the mark bracket, and **the bracket's right edge is at one fixed x on every line**, at the specimen's position; **(4)** with no printed unit, the dots run up to the bracket. Build it in Word with a right tab at the `=` position and a right-aligned dot-leader tab at the bracket's right edge, with `unit [n]` as the aligned text. Do not use a fixed left label start, a left dot-leader tab ending at an arbitrary x, or spaces. Every `=` end, unit end and bracket end matches the specimen within ±0.5 pt, and `[Total: n]` ends at the specimen's x. Measure every line on the render, not just the source. |
| Context or data, then the command sentence | For P2, when a question, part or subpart gives context or data and then a command sentence (Calculate, Determine, State, Explain, Suggest, Show, Describe, Predict, Name, Use …), the **command sentence starts on its own new line**, at the same text indent as the part's text (no label, no extra indent). It is separated by the specimen's spacing: one blank line in 5086, i.e. a 26.1 pt glyph-top to glyph-top pitch, never below the specimen and at most 0.5 pt above it. Set it as its own justified paragraph with keep-with-next, not as a manual line break or spaces. Consecutive command sentences stay together in that paragraph (e.g. "Determine … . Show on your graph …"). The wording never changes; data the wording places after the command stays there. Apply this to every P2 question, part and subpart, even where a P2 specimen part runs context and command together. P1 uses its own context–question–option grouping; P5 uses its own procedural bullet/command spacing (§14). List each split in the Builder notes. |
| Visible numerical answer lines | Every numerical response requiring a final answer has a clearly visible dotted line of sufficient length. Check the rendered page, not merely the presence of dots or a tab in the source. No missing, collapsed or excessively short line. |
| Calculation working space | Provide blank working space appropriate to the required steps and comparable to the specimen's convention. Independently solve the part to judge the space needed. Do not compress multistep calculations to fit a preferred page count. |
| Written-response space | Provide enough dotted answer lines for the expected response and mark demand. Each dotted line **starts exactly at the text indent of the question, part or subpart it belongs to**, and **ends at the specimen's end position** for that layout (§9.1.1). **The mark bracket `[n]` ends the last dotted answer line, on the same line.** The dots on that line stop just before the bracket, and the bracket's right edge is at the specimen's fixed x (5086: last-line dots end 529.6 pt, `[n]` ends 545.7 pt; every earlier line ends at 544.9 pt). Never set `[n]` as a separate paragraph or line below plain dotted lines. **Exception, also from the gold PDF:** after a *labelled* answer group (lines beginning `wave 1`, `use`, `movement` and so on) and after a drawing or graph item, `[n]` is on its own right-aligned line directly below (5086: 13.0 pt below, right edge 545.7 pt), and every labelled line runs to the full end x. The reference is the **original specimen PDF as printed** (5086: `references/specimen_5086_P2.pdf`), which is authoritative even if the specimen DOCX or a render of it differs. Build the last line as one paragraph: a right-aligned dot-leader tab holding ` [n]`. Leader dots are whole glyphs counted from the line start, so choose start positions and tab stops so that every start and end lands within ±0.5 pt, and measure the render. `[Total: n]` is always its own right-aligned line below the last answer line. Use the specimen's line pitch throughout. |
| Gap before the first answer line | The gap from the last line of question text to the first dotted line is never below the specimen value and at most 0.5 pt above it (§9.1.1). |
| Separation between parts | The gaps from answer to next part and from answer to next subpart or `[Total]` are never below the specimen value and at most 0.5 pt above it (§9.1.1). Check the entire lower-page layout for compression. |
| Units and mark brackets | Follow the specimen's quantity/unit convention and mark-bracket placement. For calculation answers, keep the unit and bracket beside the answer line as one group. For written answers, align brackets consistently with the specimen. Keep brackets visible and on the intended line. |
| Fonts, emphasis and text alignment | Verify actual font properties, size, line spacing, bold labels and alignment against the specimen. **All question text is justified, as in the specimen.** Apply bold figure/table captions, part labels and instruction keywords only as the specimen requires. Do not infer exact sizes from screenshots at unequal scales. |
| Figures, captions and tables | Match placement, caption spacing, numbering and text alignment. Ensure figure labels remain clear at final page size and do not collide with surrounding text or answer spaces. |
| Overall page density | Compare the balance of text, figures and working space directly with the specimen. Avoid compressed pages, particularly below figures, even when every element technically fits. |
| Page integrity and navigation | Verify margins, headers/footers, numbering, section instructions and sensible page breaks. **P2:** every top-level structured question starts on a new page using `w:pageBreakBefore`, not a standalone page-break paragraph. **P1:** use the specimen's compact multi-question pages, keeping each complete stem, figure and A–D option set together. **P5:** start each investigation on a new page and let its procedural parts, results table, graph grid and follow-up continue across pages as in its specimen. Do not force every practical step onto a new page. Mixed revision applies these rules section by section (§14). The **total page count is even** for double-sided printing. Any blank pages are marked as the specimen marks them (for example, "BLANK PAGE"), the cover states the page count, and there is no "[Turn over" on the last question page or on blank pages. No clipping, overflow, unexpected blank pages, distorted figures, or separated labels and answer groups. |
| Editable final presentation | Confirm question text and answer areas remain editable in Word. Do not rasterise whole pages to simulate specimen fidelity. |

### 9.3 Direct visual comparison and evidence

For **every draft**, the Builder renders the DOCX and inspects all pages before submission. The Critic then independently inspects **every rendered page**, including question continuations, at actual page size and a comparable scale to the specimen. Compare each relevant layout type directly: question stems, subparts, written answers, calculations, figures and tables. Do not accept formatting solely from the Builder's description, DOCX XML or a small sample of pages.

Each Critic report must include a formatting checklist with `PASS`, `FAIL` or `NOT VERIFIED`; the draft page/question location; the specimen page or style-sheet reference; observed evidence; and any required correction. Identify and justify genuinely inapplicable checks rather than treating missing evidence as a pass. Include representative paired page images or explicit comparison references. Record actual DOCX measurements where they support a conclusion.

**Cover, header and footer from Draft_01.** Cover layout, header (page number) and footer (school branding, §9.4) are measured and compared with the specimen from **Draft_01 onwards**, not left until late rounds. Builder includes a cover-versus-specimen image and a header crop with Draft_01, and Critic reviews them in Round 1.

**Any failed or unverified mandatory formatting check blocks acceptance, even when all the numeric thresholds in §5 have been met.** Incorrect indentation, missing numerical dotted lines, misplaced calculation-answer groups, cramped working spaces or insufficient gaps must be corrected and visually rechecked. Significant layout deviations are major defects; a missing or unusable essential answer area that prevents a fair response is critical. Minor observations outside the mandatory gate still affect the evidence-based category score and must be disclosed.

Do not claim pixel-perfect equivalence, complete page inspection or specimen conformity without recorded evidence. If rendering or reliable specimen comparison is unavailable, mark the affected checks `NOT VERIFIED` and report that the quality target has not been verified.

### 9.4 School branding and cover priority

- The project's `SCHOOL_NAME` and `EXAM_TITLE` (§2.1) appear **in the footer of every page** and **on the cover**. On the cover they replace the specimen's issuing-body lines (for example, the MOE / "in collaboration with" / Cambridge / GCE lines and "For examination from …"), in the same positions and sizes. Specimen labels such as "SPECIMEN PAPER" are omitted.
- Every other cover element (candidate name, centre and index boxes, title, duration, instructions, page-count statement) follows the specimen layout.
- **Effort priority:** teachers care far less about the cover than the question pages. The cover must be correct and tidy and must pass its check, but spend iteration effort on the question pages: spacing, answer areas, figures and page breaks. Do not run extra rounds over cover differences within the 0.5 pt loose-side tolerance.

### 9.5 Stacked and special notation

Notation that must stack (for example, nuclide notation with the nucleon number over the proton number to the left of the symbol) uses an **Office Math (OMML) object** when it renders correctly in the verification toolchain. If OMML does not render there, use a **borderless, editable Word table**, with cells for the stacked numbers and the symbol aligned as the syllabus convention requires, at body-text size or larger. Never use a raster image, and never use side-by-side superscript and subscript runs where stacking is required.

### 9.6 Document generation hygiene

When the DOCX is generated or edited programmatically:

- write property child elements (`w:pPr`, `w:rPr`, `w:tblPr`, `w:tcPr`, `w:sectPr`, border and margin blocks) in the **OOXML schema order**, with no duplicate children. Apply a reorder step before saving (for example, a reusable `ooxml_order.py`);
- **validate every XML part** (document, styles, numbering, settings, headers, footers) against the **ECMA-376 schemas** (XSD; transitional unless the specimen is strict), and report the error count with every draft. The final files must validate with 0 errors;
- **pixel-diff the rendered pages between consecutive drafts** (and between the final file and the accepted draft). A fix should change only the pages it targets, and a purely structural change (such as reordering XML) must be pixel-identical on every page. Record the diff result in the Builder notes;
- keep page breaks as paragraph properties (§9.2), keep table widths explicit (grid, fixed layout and table width) so all renderers honour them, and never overwrite earlier drafts or their renders.

## 10. Loop 2 draft process and naming

**Prerequisite:** `TOS_Approved.docx` and `TOS_Approval_Report.md` exist and show a verified Loop 1 approval.

**Paper Round 1**
1. Builder creates the complete paper with diagrams **following the approved TOS**; the Builder checks intended answers internally but does not yet write the formal answer scheme.
2. Save `Draft_01.docx`; preserve TOS alignment notes when needed. The formal answer scheme is not created during the paper Gauntlet.
3. Critic fully reviews and writes `Draft_01_Review.md` using Section 5's weighted rubric, including the cover, header and footer checks (§9.3) and the spacing measurement table (§9.1.1).

**Paper Round 2+**
4. Builder acts on Critic findings and updates the paper and any approved TOS revisions.
5. Save new, never-overwritten paper files `Draft_02.docx`, `Draft_03.docx`, etc.
6. Critic re-evaluates **the complete revised package**, recalculates scores and checks regressions and TOS alignment.
7. Continue until all acceptance conditions are met or **five complete paper rounds** are reached, unless the teacher has explicitly authorised further rounds (§4, Loop 2 step 4).

Do **not** overwrite earlier drafts, alter quality thresholds midstream or change unrelated approved questions gratuitously. If five rounds fail, provide best verified draft and full unresolved-issues report. Do not declare success prematurely. If substantive blueprint changes arise, use Loop 1 reapproval as specified in Section 4.

### Required Critic report per round

- Draft identifier; explicit list of reviewed files and checks actually performed.
- Six category scores, subcheck rationale, weighted total and calculation.
- Findings table: severity, question/figure/page, evidence, corrective instruction, verification status.
- Profile-specific representation totals and checks (§14); for P1 independent solutions to all four options and distractor rationale; for P5 feasibility and practical-skill evidence.
- Diagram-by-diagram review with individual scores, worst figure, subcriterion scores, caps, E/C roles and adjacent specimen comparisons (§6), including the §6.1 line-art check (PASS/FAIL for each figure showing a person, animal or object); independent question solvability, scientific accuracy and mark-allocation checks; syllabus mapping audit; page-by-page formatting review and the evidence-backed Section 9 checklist with direct specimen comparison references.
- Regressions vs prior version; count of unresolved critical defects; `TARGET MET` or `REVISE`/`NOT VERIFIED` with reasons.

## 11. Project file structure

```text
exam-paper/
├── references/
│   ├── specimen.docx
│   ├── syllabus.md
│   └── specimen.pdf                 # optional
├── tos_gauntlet/
│   ├── TOS_Draft_01.docx
│   ├── TOS_Draft_01_Review.md
│   ├── TOS_Draft_02.docx            # if necessary
│   ├── TOS_Draft_02_Review.md       # if necessary
│   ├── TOS_Approved.docx
│   ├── TOS_Approval_Report.md
│   └── Blueprint_Notes.md          # optional
├── drafts/
│   ├── Draft_01.docx
│   ├── Draft_02.docx                # if necessary
│   └── ...
├── critic_reports/
│   ├── Draft_01_Review.md
│   ├── Draft_02_Review.md            # if necessary
│   └── ...
└── final/
    ├── Final_Exam_Paper.docx
    ├── Final_Answer_Scheme.docx
    ├── Final_TOS.docx
    ├── Final_Quality_Report.md
    ├── Final_Exam_Paper_render.pdf  # recommended: render used for verification
    └── Final_Answer_Scheme_render.pdf  # recommended
```

The reference filenames may reflect actual uploads. If persistent folders are not supported, retain names and package results in a ZIP. Keep **all TOS drafts and review reports** and **all paper drafts and review reports**. Every full-paper draft must have a Critic report; TOS changes must be versioned and reapproved where required. There is no answer scheme accompanying each draft.

### 11.1 Mandatory Google Drive destination — every paper

**Always save every examination-paper project to a dedicated subfolder within this Google Drive parent folder:**

https://drive.google.com/drive/folders/1c-0TqPv9qJ_y7bz6A1Tw8lRPEdCjOMf3?usp=drive_link

**Parent folder ID:** `1c-0TqPv9qJ_y7bz6A1Tw8lRPEdCjOMf3`.

- Create a separate project subfolder for each new paper, named clearly using subject/syllabus code, paper number, exam title or level where known, and creation date; for example, `5086_Physics_Paper_2_2026-10-08`. Add a unique suffix if needed to avoid mixing separate papers. For revisions to the same paper, reuse its existing project subfolder.
- Within that subfolder, preserve the Section 11 structure: `references`, `tos_gauntlet`, `drafts`, `critic_reports` and `final`. Save all numbered TOS and paper drafts, corresponding Critic reports, approved blueprint, final quality report and diagram sources. Retain a review ZIP if supplied.
- Place `Final_TOS.docx`, `Final_Exam_Paper.docx` and `Final_Answer_Scheme.docx` in the project's `final` subfolder as downloadable, editable Microsoft Word files. Do not substitute Google Docs-only versions for the required DOCX deliverables.
- Save each completed draft and review as the workflow proceeds when Drive access is available; preserve earlier versions and never overwrite numbered drafts. Local working copies may be used for generation and rendering, but they do not satisfy the Google Drive destination requirement.
- Use the available authenticated Google Drive capability to create folders and upload files. Verify returned folder/file identities, filenames and parent locations before reporting success. Provide the project subfolder link and links to the three final Word files in the final response.
- This standing instruction authorises routine folder creation and file uploads within the specified parent; do not ask again between rounds. Do not change sharing permissions unless explicitly requested.
- If Drive access or upload is unavailable or fails, preserve the actual files, provide downloadable copies, state clearly that the required Drive save is incomplete, and identify the access needed. Never claim that local downloads were saved to Drive. Scientific quality acceptance and successful Drive delivery are separate statuses; do not describe delivery as complete until the Drive upload is verified.

## 12. Final deliverables and status

Provide three editable Word deliverables: `Final_TOS.docx`, `Final_Exam_Paper.docx` and `Final_Answer_Scheme.docx`; additionally provide `Final_Quality_Report.md`, plus all numbered drafts and Critic reports **from both loops**, including `TOS_Approved.docx` and `TOS_Approval_Report.md` (preferably ZIP). Verify files can be opened and are complete; do not deliver placeholder documents as complete work.

Final quality report must show: TOS approval status and number of TOS review rounds; paper review rounds, score by paper round, six-category breakdown, minimum individual figure score, every figure subcriterion and same-size specimen comparison, defects corrected, per-figure evaluation, originality/phrasing evaluation, independently checked question validity and syllabus mappings, mandatory Section 9 formatting checklist and direct specimen comparison evidence, teacher-requested deviations (§2.1), any rounds beyond the limit with the teacher's instruction (§4), schema-validation and pixel-diff results for the final files (§9.6), outstanding issues, tool/independence limitations and actual acceptance status.

**Renderer disclosure.** If the drafts were rendered only with LibreOffice or another non-Word renderer, the report must state that **Word pagination is untested** and must list the **tightest page feet**: the pages where the last element comes closest to the bottom limit, each with its spare space in pt. The teacher can then check those pages first when the paper is opened in Word.

Use one final designation:
- `QUALITY TARGET ACHIEVED — READY FOR TEACHER MODERATION` (only if every gate verified), or
- `QUALITY TARGET NOT ACHIEVED — FURTHER REVIEW REQUIRED`.

Never describe the paper as officially approved; a teacher/exam moderator must sign off.

## 13. Autonomous execution instruction

Read all applicable uploaded references, inspecting the Physics sections in full and recording exclusions for combined papers. **First run Loop 1 (TOS Builder → Critic → TOS revisions) for up to three rounds; do not write the paper until `TOS_Approved.docx` passes all mandatory checks. Then run Loop 2 (Paper Builder → Critic → numbered paper revisions) for up to five rounds. Once Loop 2 meets the acceptance gate, Builder alone prepares `Final_Answer_Scheme.docx`, without a third loop**, without asking for approval between routine rounds. If a necessary capability is unavailable (e.g. true isolated agents, DOCX rendering, figure editing), disclose the limitation and do not pretend the check occurred. Prioritise the diagram standard, originality, specimen-authentic phrasing, scientific validity and formatting fidelity. Stop each loop at verified acceptance or its own round limit (or continue beyond the Loop 2 limit only on the teacher's explicit instruction, recorded as in §4); deliver actual files and honest reports. Always save project outputs to the designated Google Drive project subfolder under Section 11.1 and report verified delivery status.

**Success gate: TOS approved at 100% mandatory compliance; paper ≥99/100 overall; Diagram quality ≥99/100; other categories ≥96/100; every figure ≥98/100 and every figure subcriterion ≥96/100; zero unresolved critical or major diagram defects; all mandatory checks verified; three complete editable DOCX deliverables (TOS, paper, answer scheme); verified saving of all project outputs to the designated Google Drive subfolder.**


## 14. Paper-specific requirements

### 14.1 Paper 1 Multiple Choice

**Reference:** `references/specimen_5086_P1.pdf`, printed pages 2–7, Physics questions 1–20. The original combined paper has 40 questions, 1 hour, and a separate multiple-choice answer sheet; Chemistry questions 21–40 are not Physics content references. A Physics-only 20-question paper or a 40-question Physics revision section is a school adaptation. Follow the requested count and scope; do not import Chemistry questions, the Chemistry data sheet or periodic table. Do not assume the combined-paper duration applies to a school adaptation.

**Representation gate, before drafting:** Unless the teacher explicitly sets another balance, at least **40% of Physics MCQs must use figures**, including at least **30% of all MCQs requiring essential extraction (E)**. Round each minimum up: for 20 MCQs, at least 8 figure-based including 6 E items; for 40, at least 16 figure-based including 12 E items. E is a subset of figure-based items, not an additional quota. Diagrams, graphs, instrument faces, wave patterns, circuits and diagram options count; data tables are audited separately and cannot alone satisfy the figure quota. These are **school design defaults**, informed by the reference, not official SEAB percentages. Record a teacher-directed exception rather than silently missing the minimum. A zero-figure or all-contextual MCQ section fails the TOS gate.

Distribute figures across the available syllabus areas. Where the scope includes reading instruments, include at least one genuine instrument-reading item. Where distance–time/speed–time or wave graph interpretation is assessed, include at least one actual quantitative graph-reading item; prose describing a graph does not satisfy this. Use a mix of visual reasoning, readings, calculations, relationships and conceptual explanations. Use diagram options when they assess a suitable distinction, rather than adding them decoratively. Do not force unrelated or out-of-scope topics to meet quotas.

For each MCQ the Builder records its learning outcome, E/C/N role, required extraction, intended correct option and the misconception behind each distractor. The Critic independently solves the stem and evaluates **all four options**, including rounding, unit conversions, counting intervals instead of crests, axis scales, viewing direction and significant-figure effects. Verify exactly one defensible answer, mutually exclusive options where applicable, parallel grammar, and plausible distractors. Check for unintended cues from option length, artwork quality, line darkness, labels or a repeated correct-letter pattern. Do not change a logical numerical ordering solely to balance letters; remove conspicuous patterns without damaging option quality. A text-only item may be excellent, but cannot replace required representation coverage.

**Layout:** Match P1 font, indents, body density, figures and vertical, horizontal or tabular A–D options. Multiple questions may share a page. Keep each option set with its stem and figure; wrap at consistent hanging indents; never apply P2 dotted answer lines or a new page for every MCQ. Put the question after the context/visual where the specimen does. Numerical/diagram options use identical scales and comparable dimensions unless different scale is itself assessed and clearly stated. Include a numbered answer grid after the MCQs for revision packages unless the teacher specifies another arrangement; for an exam with a separate answer sheet, follow that format. Each correct answer is 1 mark, with no negative marking unless explicitly requested.

**P1 answer scheme:** Provide a verified A–D key plus the correct option text and a concise explanation/working for every item. Reference the exact visual evidence (e.g. the difference between two readings or the number of wavelength intervals). Explain the misconception tested by each distractor in a teacher-facing section when helpful. Update both key and explanation after any change to option order or a diagram.

### 14.2 Paper 2 Structured Questions

**Reference:** `references/specimen_5086_P2.pdf`, with the root Word specimen as secondary. Existing P2 rules in §§9.1–9.6 remain: measured answer-space geometry, one top-level question per new page, correct part hierarchy, right-aligned calculation answers and bracket placement, adequate working spaces and original specimen-style phrasing. Official 5086 P2 structure is 55 marks Section A plus one of two 10-mark Section B alternatives (65 attempted marks); a revision package follows the teacher's requested structure instead.

At the TOS gate require an appropriate spread of essential diagram/graph/table interpretation and construction tasks across the selected topics, rather than supplying all data in prose. A P2 figure cannot satisfy a missing P1 visual requirement in a mixed package. Provide proper blank grids, scales or diagrams when the task requires candidates to draw or extract information. The final scheme includes completed model diagrams/graphs wherever a drawn response is required.

### 14.3 Paper 5 Practical Physics only

**Reference:** `references/specimen_5086_P5.pdf`, Physics question 1, printed pages **2–7**. Pages 8–10 and the Chemistry notes on page 12 are outside this project's Physics scope. The combined specimen is 30 marks over 1 hour 30 minutes and advises 45 minutes per question. Its Physics investigation is 15 marks; use that as a model when requested, not a requirement to reproduce the pendulum investigation or its exact part sequence in every practical.

**Blueprint:** Map marks to execution/observation, repeated measurements, recording/units/precision, processing, graph work/gradient, inference and experimental evaluation or extension. Include a modification/extension task consistent with the syllabus practical-skills weighting (the syllabus extraction describes 10–20% of the practical test; a Physics-only adaptation must state its chosen allocation). Choose an experiment supported by the taught syllabus and apparatus available or explicitly assumed. Record independent, dependent and controlled variables; range and number of readings; repeats; apparatus resolution; physical dimensions; expected trend and feasible completion time. An attractive diagram does not establish laboratory feasibility.

**Apparatus drawing:** Match the P5 reference's functional detail: recognisable stand, boss, clamp, support blocks, string and bob/putty; unambiguous measurement endpoints and horizontal/vertical reference lines. This is a standard of illustration, not a requirement to include these particular apparatus in unrelated investigations. The drawing must show a buildable arrangement, correct attachment/contact/support, safe clearances and a sensible viewing direction. Use image generation for closer apparatus illustration if needed, then overlay accurate measurements and labels. Avoid arbitrary rectangles/circles standing in for an actual apparatus assembly.

**Student paper:** Give ordered, executable steps with the P5 bullet/subpart hierarchy, necessary setup dimensions and measurement precision. Preserve continuity across pages: apparatus instructions, results table, graph grid and analysis remain clearly linked. Provide enough blank table rows for required measurements, purposeful headers/blank headers if constructing a heading is assessed, and enough writing space. A full-page plotting grid must remain dimensionally suitable at 100% A4 print size, with sufficiently distinct major/minor lines and no page scaling/stretching. Do not prelabel axes or prefill results that candidates are meant to produce.

**Data and mathematical integrity:** Separate measured quantities from derived quantities; use units consistently, including squared units. In this specimen, `t` is the time for **ten** oscillations, not the period of one oscillation; `t²` is the square of that ten-oscillation time. Read the supplied equation visually from the PDF, not from unreliable text extraction (printed p.6 has `gradient = π²K/g`, with `g = 981 cm/s²`). Never silently replace it with a familiar period formula or change g to 10 N/kg without converting the whole problem consistently. For a new experiment define each symbol and equation clearly. Independently check the expected relationship, slope units and graph scale against realistic data.

**Feasibility and readiness:** Check apparatus range/resolution, physical fit, available increments, stability, repeats, time budget and the ability to obtain a measurable trend. Record whether an actual pilot was run, by whom, what was measured and which evidence supports the proposed ranges. If no physical apparatus/pilot is available, perform and report a design/calculation review, label physical validation **NOT VERIFIED**, and identify what the teacher/technician must test before lab use. Do not fabricate a pilot, measured values or confidential instructions. Include concrete risk controls relevant to the actual experiment; do not add unrelated generic warnings.

**Teacher scheme and technician information:** Provide apparatus/setup requirements (an appendix or separate editable document where appropriate), expected relationships, realistic illustrative readings/ranges explicitly labelled as such, processing examples, completed model graph, large gradient triangle and calculation, mark criteria for observations/precision/table/plot/line/gradient/evaluation, justified improvements and an achievable extension. Candidate measurements vary: do not impose one exact invented dataset as the only correct answer or use exact theoretical values as supposed experimental results. Retain error-carried-forward and sensible tolerance guidance. If official confidential instructions have not been supplied, label the technician notes as a proposed school setup, not an official document.

### 14.4 Mixed revision packages and release checks

Make separate P1 and P2 representation totals, formatting checks and reference comparisons. Respect the teacher's requested counts, topic boundary and mark range. Unless specified otherwise, include Measurement when it falls within the requested syllabus range; do not carry exclusions from an earlier paper into a new request. Diagram quality and essential interpretation are separate checks: both must pass. After a figure/readout/option change, re-solve the question, update its TOS row and final scheme, recheck uniqueness and render the affected page.

Keep the exact two-agent/two-loop workflow and existing review-round limits. Stricter diagrams are not permission to fabricate scores or silently extend rounds. Stop at the existing limit and report unmet gates honestly when necessary. Do not automatically label an earlier paper compliant with this version; it must be reviewed against the new requirements.
