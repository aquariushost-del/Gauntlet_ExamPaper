Exam Paper Gauntlet — Project Instructions

This project is dedicated to creating professional, original examination papers using a 2-Agent, 2-Loop Gauntlet workflow.

Master Instructions

The uploaded GAUNTLET_INSTRUCTIONS.md is the authoritative workflow document.

Before starting any examination-paper development task, read and follow this file in full.

Reference Documents

* Specimen Paper (.docx): Master reference for examination structure, formatting, question phrasing, difficulty and diagram quality.
* Syllabus (.md): Authoritative reference for examinable content and learning outcomes.

Workflow

Loop 1 — TOS Gauntlet

Builder AI creates the Table of Specifications. Independent Critic AI reviews and requires corrections until the blueprint meets all mandatory requirements.

The Builder must not proceed to question writing until the TOS is approved.

Loop 2 — Examination Paper Gauntlet

Builder AI creates the examination paper based on the approved TOS. Independent Critic AI evaluates it against the quality rubric, focusing particularly on diagram quality, question creativity, specimen-style phrasing, formatting and scientific accuracy.

Each iteration must be saved as a numbered draft, with a corresponding Critic report.

The specimen is the gold standard for spacing. Measure it before drafting. No gap may ever be below the specimen value; each gap is at the specimen value or up to 0.5 pt above it (GAUNTLET §9.1). Every question starts on a new page, in every paper, using page-break-before (GAUNTLET §9.2). Question pages take priority over the cover. Record the school name and other project settings at the start (GAUNTLET §2.1).

Quality target: as defined in GAUNTLET_INSTRUCTIONS.md (currently at least 99/100 overall, at least 96/100 in every category, zero critical defects, and every mandatory check verified). If this summary ever differs from GAUNTLET_INSTRUCTIONS.md, the master instructions prevail.

Final Stage — Answer Scheme

Once the examination paper has met the quality requirements, Builder AI creates the complete answer scheme. No additional Gauntlet Loop is required.

Final Deliverables

All three main deliverables must be editable Microsoft Word documents:

1. Final_TOS.docx
2. Final_Exam_Paper.docx
3. Final_Answer_Scheme.docx

Preserve numbered drafts and quality review reports.

Execution Rules

* Use genuinely separate Builder and Critic agents where supported.
* If separate agents are unavailable, disclose this and use separate review passes.
* Execute review iterations autonomously within the limits stated in the master instructions. Go beyond the round limit only when the teacher explicitly asks, and record it.
* Do not fabricate quality scores or claim checks were completed without evidence.
* Prioritise exceptional diagram quality, creative questions, accurate scientific content and faithful specimen formatting.
* Draw people, animals and objects in figures as recognisable, specimen-accurate black-and-white line art, never placeholder shapes. Image generation is allowed if cleaned up to exam line art; physics geometry stays vector-drawn. This is a scored Diagram quality criterion, and placeholders are a scored defect (GAUNTLET §6.1).
* Calculation answer lines copy the specimen's measured geometry: the `=` ends at one fixed x (label right-aligned), the dots fill from the `=` to the unit, then a space and the mark bracket right-flush at one fixed x. Build with a right tab plus a right-aligned dot-leader tab, never a fixed left label start (GAUNTLET §9.2).
* Context or data first, then the command sentence on its own new line at the same indent, with the specimen's spacing (5086: 26.1 pt pitch, one blank line). Wording unchanged; consecutive commands stay together (GAUNTLET §9.2).
* Do not declare the examination paper ready until the quality criteria are met or clearly report any outstanding limitations.
* Disclose when Word pagination is untested (non-Word renderer), and list the tightest page feet.

Always follow the latest uploaded version of GAUNTLET_INSTRUCTIONS.md.
