# Independent Critic Review — TOS Draft 01 (Loop 1)

**Role:** Independent Critic AI (not Builder)  
**Gauntlet:** v1.5.0 Loop 1 — Table of Specifications only  
**Draft under review:** `TOS_Draft_01`  
**Date:** 2026-10-22  
**Decision:** **REVISE**

Independence note: This review was performed as a separate Critic pass against the syllabus, master instructions, Blueprint Notes, TOS draft (MD + DOCX), and the teacher cover precedent PDF. No paper stems were drafted. Checks not performed are marked NOT VERIFIED; none were invented.

---

## Files reviewed

| File | Use |
|---|---|
| `/workspace/GAUNTLET_INSTRUCTIONS.md` (v1.5.0) | Loop 1 gate, §2.1 settings, §14 MIXED_REVISION / P1 / P2 |
| `/workspace/AGENTS.md` | Project authority and profile gates |
| `/workspace/5086_Physics_Key_Syllabus_2026.md` | Light 11(a)–(h), exclusions (thin-lens equation; no recall of image characteristics for specific object distances; no Pure-Physics TIR import) |
| `/workspace/exam-paper-lenses/tos_gauntlet/Blueprint_Notes.md` | Project settings, VISUAL_PLAN, exclusions, representation audit |
| `/workspace/exam-paper-lenses/tos_gauntlet/TOS_Draft_01.md` | Primary TOS content reviewed |
| `/workspace/exam-paper-lenses/tos_gauntlet/TOS_Draft_01.docx` | Confirmed same content as MD (extracted Word text) |
| `/workspace/exam-paper-lenses/references/grokbot_refraction_example.pdf` | Teacher cover/structure precedent (cover page text rendered via PyMuPDF) |
| `/workspace/exam-paper-lenses/references/SPECIMEN_COMPARISON_NOTES.md` | Representation / illustration class support |
| `/workspace/references/specimen_5086_P1.pdf`, `specimen_5086_P2.pdf` | Profile reference existence confirmed (full page-by-page layout measurement not required at TOS gate beyond profile citation) |

**Not reviewed (out of Loop 1 scope):** any examination stems, figures, or answer scheme (none should exist yet).

---

## Mandatory Loop 1 checklist

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | `PAPER_PROFILE` recorded; MIXED_REVISION with P1/P2 refs and scope | **PASS** | Blueprint §2.1: `MIXED_REVISION` (A=P1, B=P2); TOS header matches. Refs: P1 pp. 2–7; P2 answer-space rules; cover = grokbot topical. |
| 2 | Teacher deviations recorded and match request | **PASS** | Blueprint `TEACHER_DEVIATIONS`: grokbot cover with topic → **Lenses**; 10 MCQ + 61 structured = 71; 1 h 30 min. Cover PDF verified: “Section A (10 marks)”, “Section B (61 marks)”, “1 hour 30 minutes”, answer-grid instruction, SACSS branding. |
| 3 | Topic boundary / syllabus mapping to 11(f)–(h) | **PASS** (with findings) | TOS maps every item to 11(f)/(g)/(h) and/or practical investigation 8. Supporting refraction only where stated. No EM/motor content planned. |
| 4 | Explicit exclusions respected in plan (thin-lens formula; object-distance image-case recall; TIR; diverging-lens theory beyond syllabus) | **FAIL** | Exclusions are *stated* (Blueprint + TOS self-check), but **Q10 concept framing** uses “Object beyond 2F arrangement” in a way that risks testing excluded 11(h) case recall unless rewritten. Q14/Q17 also need explicit anti-case-recall locks (see Findings). No TIR/diverging/thin-lens formula planned elsewhere — those parts OK. |
| 5 | Sec A representation audit (≥40% figure-based; ≥30% E); separate from Sec B | **PASS** | Independent recount: figure-based Q1,3,4,6,8,10 → **6/10 (60%)**; E Q1,3,4,8,10 → **5/10 (50%)**. Thresholds for n=10: ≥4 figures, ≥3 E. Q6 correctly tagged **C** (stem states larger/upright). |
| 6 | Sec B representation audit (essential diagram/measure/construct spread; not satisfied by Sec A) | **PASS** | Blueprint + TOS: Q11–19 carry draw/measure/read/construct tasks; Q17 table+figure; Q20 contextual/optional only. Spread across lens action, focal length, and evidence-based characteristics. |
| 7 | Mark arithmetic (authored = attempted; section totals) | **PASS** | Sec A 10×1=10. Sec B 7+6+8+7+6+6+7+5+5+4 = **61** (recomputed). Paper **71**. All compulsory; no choice arithmetic. |
| 8 | Marks-by-outcome table internally consistent | **FAIL** | Table claims ~28 + ~20 + ~23 = **71** while also stating LO shares *overlap*. Overlapping attributions cannot honestly sum to 71. Primary-LO partition (or a dual-count table without a false total) required. |
| 9 | Duration stated and consistent with teacher precedent | **PASS** | 1 h 30 min for 71 marks; matches grokbot cover. |
| 10 | AO / difficulty balance reasonable for topical worksheet | **PASS** | Indicative KU 32 / HI 39 (~45/55). Difficulty mix E/M present. Acceptable for school topical; not official full-syllabus AO audit. |
| 11 | Diagram / apparatus feasibility; pilots disclosed | **PASS** (disclosed limits) | Vector rays/grids planned; image-gen considered for Q13 apparatus. Blueprint honesty: physical print and lab pilot **not performed**. Acceptable at TOS if carried into later reports. |
| 12 | Per-item specimen comparison cited for planned visuals | **FAIL** | Loop 1 requires relevant specimen comparison with planned visuals. TOS/Blueprint give profile refs only; no per-figure specimen page/class (e.g. P1 option panels; P2 construction; P5-class apparatus for Q13). |
| 13 | Sec B part-level mark / response blueprint where useful | **FAIL** | Q11–20 are 4–8 mark multi-response items (draw + measure + define + explain, etc.) but TOS gives **whole-question marks only**—no (a)/(b)/(c) mark splits. Insufficient to lock mark allocation before drafting. |
| 14 | Revision-package answer grid planned (teacher cover + §14.1) | **FAIL** | Grokbot cover: “write its letter in the answer grid”; §14.1 expects numbered answer grid after MCQs for revision packages. Neither TOS nor Blueprint lists the grid. |
| 15 | Q19 scoped to 11(f) ray action (not full image-case construction) | **PASS** | TOS Q19: three incident rays (parallel / through F / through O); “draw each refracted path using lens action rules (**not** case-recall of image type)”. Syllabus-aligned with 11(f). |
| 16 | DOCX ↔ MD consistency | **PASS** | DOCX text extraction matches `TOS_Draft_01.md` content. |

**Mandatory gate:** any FAIL on the above blocks approval. Critical/major findings below must be cleared.

---

## Findings

| ID | Severity | Location | Evidence | Precise correction required |
|---|---|---|---|---|
| F1 | **Critical** | Sec A **Q10** | Concept: “Object **beyond 2F** arrangement drawn; four screen positions.” Syllabus 11(h): *“Recall of image characteristics for specific object distances is not required.”* Framing embeds a named object-distance case. If the stem asks where the image/screen is from “beyond 2F” without forcing extraction from fully drawn converging-ray geometry, the item tests excluded case recall. Distractor note (“beyond where rays diverge”) is salvageable only if rays uniquely show the meeting point. | **Rewrite Q10 concept.** Remove reliance on “beyond 2F” as assessed knowledge. Require a figure (or diagram options) in which ray paths visibly determine the only screen position that can catch a sharp real image. Stem must be answerable by reading the drawing, not by recalling the standard object-distance table. Re-tag LO emphasis as 11(f)/(h) from evidence. |
| F2 | **Major** | Sec B **Q14** | Concept opens “Magnifying glass: object **inside F**…”. Task includes “state characteristics from evidence” with emergent rays supplied—acceptable **if** locked. Risk: Builder writes a stem that awards marks for recalling inside-F → virtual/magnified/upright without using the figure. | Add explicit blueprint lock: characteristics marks **only** from completed ray evidence on Fig.14.1 (extend back, mark I, then describe). Prohibit stems of the form “Object inside F; state three characteristics…” with no construction/evidence step. |
| F3 | **Major** | Sec B **Q17** | “Two object positions” + table + “complete characteristic descriptions”. Blueprint says no thin-lens formula—good—but positions could still be taught/tested as named cases (e.g. at 2F). | Lock: Table 17.1 / Fig.17.1 must supply all evidence (screen catchable or not, relative sizes/orientation observations). Do **not** require recall of characteristics from named object-distance cases. Do **not** ask candidates to compute \(f\) via \(1/u+1/v=1/f\). Lengths may be measured/stated only. |
| F4 | **Major** | Sec B Q11–Q20 rows | Multi-part response types listed without part marks (e.g. Q11 draw + mark F + measure + define = 7 with no split). | Add sub-question rows (or nested mark columns) with planned marks summing to each question total, AO per part, and response type per part. |
| F5 | **Major** | Marks-by-outcome table | “~28 / ~20 / ~23” summed to 71 while “shares overlap by design.” | Provide a **primary-LO partition** of all 71 marks (each mark counted once), or a dual-count matrix that does **not** claim an overlapping sum equals 71. |
| F6 | **Major** | Planned figures (Sec A + Sec B) | No per-item “relevant specimen comparison” field. | For every planned figure / diagram-option set, cite specimen class + page (e.g. P1 diagram-options ≈ specimen Q18/19 class; Q13 apparatus ≈ P5 Fig.1.1 class / closest P2 apparatus; ray grids ≈ P2 construction). |
| F7 | **Major** | Paper structure / Sec A end | Teacher cover requires answer grid; §14.1 expects it for revision packages. Absent from TOS. | Add blueprint row: numbered A–D answer grid after Section A (page placement per grokbot precedent). |
| F8 | **Minor** | Sec A Q1 vs Q7 | Both assess converging-lens action on a parallel beam (diagram vs text). | Differentiate contexts or cognitive demand so Q7 is not a text paraphrase of Q1; keep both only if clearly distinct. |
| F9 | **Minor** | Cover topic string | Precedent footer/topic: “5086 Refraction of Light”. Deviation correctly plans Lenses, but exact cover/footer strings not listed. | Record exact replacement strings, e.g. cover “Topic: Lenses” and footer “5086 Lenses” (or teacher-preferred wording), mirroring grokbot layout. |

### Q19 special check (requested)

| Aspect | Verdict | Evidence |
|---|---|---|
| Drawing refracted paths for parallel / through-F / through-O rays | **Allowed** | Syllabus 11(f): action of a thin converging lens on a light beam. |
| Full image construction from object-distance case recall | **Not present in plan** | TOS explicitly: “not case-recall of image type.” |
| Residual risk | Low if Builder keeps three independent ray-action tasks and does **not** add “object at …; construct the image and state characteristics” without supplied evidence | Keep Q19 = 11(f) action only; image-characteristic marks belong on evidence-based items (Q12, Q14, Q16, Q17) only. |

### Out-of-syllabus challenge summary

| Risk area | Planned? | Critic call |
|---|---|---|
| Thin-lens equation \(1/u+1/v=1/f\) | Explicitly excluded (Q16, Q17, Blueprint) | OK if F3 lock enforced |
| Rote image characteristics vs object distance | **Q10 framing fails**; Q14/Q17 need locks | Must revise |
| TIR / critical angle | Not planned | OK |
| Diverging-lens theory / case tables | Not planned; converging only | OK |
| Full refraction (Snell calculations) as assessed core | Not planned; lenses boundary | OK |

---

## What already meets the gate (do not regress)

- Profile `MIXED_REVISION` and school settings (`SACSS`, `Topical Worksheet 2026`, `5086`).
- Sec A visual quotas met with honest C tagging on Q6.
- Sec B essential-visual spread across Q11–19.
- Section mark totals 10 + 61 = 71.
- Duration and section structure match teacher cover precedent.
- Q19 correctly scoped to 11(f) ray rules.
- Thin-lens formula and diverging/TIR content not invited (except Q10/Q14/Q17 case-recall risks above).
- Pilot/print limits disclosed.

---

## Decision

# REVISE

Loop 1 does **not** pass. Critical defect F1 and mandatory checklist FAILs (exclusions integrity, LO mark table, specimen comparisons, Sec B part marks, answer grid) block approval. Builder must produce `TOS_Draft_02` addressing **all** Critical and Major findings; Critic will re-check the **complete** blueprint.

### Exact required changes for Builder (acceptance criteria for Draft 02)

1. **Rewrite Q10** so assessment is essential visual extraction from ray/screen geometry, with **no** dependence on memorised “beyond 2F” (or other object-distance) image rules; update concept, extraction, distractors, and LO tags accordingly.
2. **Add anti-case-recall locks** on Q14 and Q17 (and any similar item): characteristics only from supplied figure/table evidence; no thin-lens formula.
3. **Add part-level mark rows** for every Sec B question, summing to the question totals.
4. **Replace** the overlapping ~28/~20/~23 “Sum 71” presentation with a verifiable primary-LO mark partition (or a non-summing dual-count matrix).
5. **Cite specimen comparison class/page** for every planned figure and diagram-option set.
6. **Plan the Section A answer grid** per teacher cover / §14.1.
7. Address Minor F8–F9 if practical in the same round (recommended).

Do **not** begin full stem drafting or paper production until `TOS_Approved.docx` exists after a Critic **APPROVED** decision.

---

## Checks explicitly NOT VERIFIED (honest limits)

| Item | Reason |
|---|---|
| Final cover pixel layout vs grokbot | Cover not yet built; only deviation *plan* reviewed. |
| Actual drawn figures / scientific geometry | No figures exist at TOS stage. |
| Word pagination / XSD / print pilot | N/A until paper drafts; Blueprint disclosure noted. |
| Laboratory pilot of lens practical | Disclosed unperformed — remains NOT VERIFIED for later P2/practical fidelity, not a TOS arithmetic fail. |
| Independent solve of finished items | No stems yet (correct for Loop 1). |
