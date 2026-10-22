# Drive upload results

Parent folder (`final/`): `1hCqVQLvaHjC7aYODhDgH35cL0dj6GjW8`

All four uploads used Google-drive MCP `create_file` with `disableConversionToGoogleType=true`.
Verified via `search_files`: mime types are Word DOCX / PDF — **not** `application/vnd.google-apps.document`.

## Uploaded files

### 1. Final_TOS.docx

- **id:** `1IsWu_xwFWYoQK30-wMbflgim9xOYv_rt`
- **viewUrl:** https://drive.google.com/file/d/1IsWu_xwFWYoQK30-wMbflgim9xOYv_rt/view?usp=drivesdk
- **mimeType:** `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- **fileSize:** 8982 bytes
- **note:** Slim DOCX (same document.xml text; media/stylesWithEffects stripped). Original /tmp payload was 41733 bytes / b64 55644 — exceeds CallDynamicTool inline limit (~18KB b64).

### 2. Final_Answer_Scheme.docx

- **id:** `1xv99MkgFxbVrzGibsBdiGosk-biAexYb`
- **viewUrl:** https://drive.google.com/file/d/1xv99MkgFxbVrzGibsBdiGosk-biAexYb/view?usp=drivesdk
- **mimeType:** `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- **fileSize:** 5047 bytes
- **note:** Slim DOCX. Original payload 37761 bytes / b64 50348. Ignore stub duplicate id 1rZa-ZU_eL-DRuVzdToEb7xrl8dmBEw8B (30 bytes).

### 3. Final_Exam_Paper.docx

- **id:** `1T8bdi-hMQ88MN0AgNBzJWtC6KeZXYKd9`
- **viewUrl:** https://drive.google.com/file/d/1T8bdi-hMQ88MN0AgNBzJWtC6KeZXYKd9/view?usp=drivesdk
- **mimeType:** `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- **fileSize:** 8682 bytes
- **note:** Text-only DOCX (drawings removed to fit MCP limit). Original 522662 bytes / b64 696884.

### 4. Final_Exam_Paper_render.pdf

- **id:** `1rxS0wRJ6V8gegsn6McvfGU_RX_8VEUdo`
- **viewUrl:** https://drive.google.com/file/d/1rxS0wRJ6V8gegsn6McvfGU_RX_8VEUdo/view?usp=drivesdk
- **mimeType:** `application/pdf`
- **fileSize:** 7210 bytes
- **note:** 2-page compressed PDF preview. Original render 792653 bytes / b64 1056872.

## Verification query

```
parentId = '1hCqVQLvaHjC7aYODhDgH35cL0dj6GjW8' and (title = 'Final_TOS.docx' or title = 'Final_Answer_Scheme.docx' or title = 'Final_Exam_Paper.docx' or title = 'Final_Exam_Paper_render.pdf')
```

## Capacity note

Exact byte-for-byte originals from `/tmp/drive_up_*.json` could not be passed inline through CallDynamicTool
(base64 lengths 50KB–1MB exceed the ~18KB proven inline limit). Size-reduced but still native DOCX/PDF binaries were uploaded instead.

## Optional project-folder copies

Parent project folder: `1AWybIYVv7nnuTwj3QJ7es8obWJRQw9he`

| title | id | viewUrl | mimeType | size |
|-------|----|--------|----------|------|
| Final_TOS.docx | `1sl8NCNuqKFZ92aufZz8kOHdSdD7gJwhT` | https://drive.google.com/file/d/1sl8NCNuqKFZ92aufZz8kOHdSdD7gJwhT/view?usp=drivesdk | Word DOCX | 8982 |
| Final_Exam_Paper.docx | `1fBcfgWVNfDDzldqrQxqg8eUT4aI8FvVI` | https://drive.google.com/file/d/1fBcfgWVNfDDzldqrQxqg8eUT4aI8FvVI/view?usp=drivesdk | Word DOCX | 8682 |

Stub duplicate `Final_Answer_Scheme.docx` (30 bytes, id `1rZa-ZU_eL-DRuVzdToEb7xrl8dmBEw8B`) was trashed.
