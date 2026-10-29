# Draft_02 spacing measurement table (§9.1.1)

**Specimen:** `references/specimen_5086_P2.pdf` (gold).  
**Draft render:** LibreOffice PDF of `Draft_02.docx` (Word pagination untested).  
**Method:** PyMuPDF glyph/line bbox sampling on selected Sec B pages vs specimen medians from GAUNTLET §9.1.2.

| Gap class | Specimen (pt) | Draft sample (pt) | Location | Result |
|---|---:|---:|---|---|
| Dotted-line pitch | 26.0 | 26.0 (exact line spacing set) | Q11(d), Q12(a) | PASS (style) |
| Text → first dotted line | 26.0 | 24–28 (LO render variance) | Q11(d), Q14(b) | BORDERLINE — recheck in Word |
| Answer → next part | 39.0 | ~36–42 | Q11(b)→(c), Q12(a)→(b) | BORDERLINE |
| Answer → `[Total]` | 26.0 | ~26 | Q11, Q12 | PASS (approx) |
| Calc `=` end x | 347.3 | ~347 (tab at 12.25 cm) | Q11(c), Q16(a) | PASS (designed) |
| Calc bracket right x | 545.4 | ~545 (tab at 19.25 cm) | Q11(c) | PASS (designed) |
| Qualitative `[n]` last-line | 545.7 | designed via right leader tab at 17.0 cm content | Q12(a) | PARTIAL — verify on Word |
| Subpart indent | 1.85 cm class | ~1.85 cm left_indent | Sec B parts | PASS (style) |

**Honest status:** Full automated page-wide ±0.5 pt audit incomplete under LibreOffice; several rows remain **NOT VERIFIED** at Word print fidelity. Builder sets specimen tab targets; Critic must re-measure. Physical print untested.
