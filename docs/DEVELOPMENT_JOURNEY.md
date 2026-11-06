# Development Journey — WEBC4301

This log distinguishes **historical GitHub commits** from **locally observed progress**. It is a narrative of coursework, not a rewritten or backdated Git history.

## Oct 16, 2026 — Assignment 01: Templates, Context, and DTL

- Created a Django project (`project`) and app (`pages`).
- Added a view that passes personal-study example values as a context dictionary to the template.
- Practiced DTL filters `capfirst`, `add`, `stringformat`, `upper`, `default`, `timesince`.
- Practiced template inheritance with `base.html` and shared `footer.html`.
- Built a gold/white presentation and recorded desktop/mobile previews.

**Evidence:** [initial commit](https://github.com/MR7PRO/django-templates-context-assignment-/commit/3db68836bc), [README/screenshot commit](https://github.com/MR7PRO/django-templates-context-assignment-/commit/ce33340fd5).

## Oct 27, 2026 — Assignment 02: Models, SQLite, Admin

- Introduced `StudentProfile` with name, university ID, age, date of birth, address, salary and image.
- Created and applied Django migrations.
- Registered the model in the Django Admin and added student-profile records.
- Queried records with `objects.all()` and rendered their fields/images in `/home/`.
- Preserved the original `/` template/context assignment.

**Evidence:** [Models, Admin, UI commit](https://github.com/MR7PRO/django-templates-context-assignment-/commit/711b95fdd9).

## Nov 6, 2026 — Assignment 03: Student Form and Validation

- Added a separate `Student` model to preserve the previous `StudentProfile` model.
- Created and applied `pages/migrations/0002_student.py`.
- Added a `StudentForm(forms.ModelForm)` with field-specific `clean_...` methods.
- Wired `/add-student/` and `/students/`, enabling POST, CSRF protection, image upload, validation, save, redirect and table output.
- Adapted only the student table page to a wider layout, preserving prior page styling.
- Added Django-side address-length feedback by removing the form widget's browser `maxlength` while keeping `max_length=150` in the model/form validation.

### Manual QA observations

| Check | Observed outcome |
|---|---|
| Django system check | No issues reported |
| Migration `0002_student` | Applied successfully |
| Student Admin | Both `StudentProfile` and `Student` visible |
| Successful form submission | Redirect to `/students/`, record and image rendered |
| Duplicate university ID | Rejected with field error |
| University/national/mobile ID lengths | Wrong lengths rejected |
| Prefix validations | Invalid prefixes rejected |
| Name containing numbers | Rejected |
| GIF image | Rejected, JPG/PNG requirement shown |
| 151-character address | Rejected with Django field error |
| Empty required form | Browser required-field warning observed |

**Evidence:** local screenshots reviewed during the assignment walkthrough. Screenshots should be copied into reviewed documentation folders before publication, with personal data and real faces removed/redacted. The code was still uncommitted in the original local working tree at the time of this review.

## November 6, 2026 — New repository and clean local verification

- Created [WEBC4301-Django-Assignments](https://github.com/MR7PRO/WEBC4301-Django-Assignments) independently of the earlier repo.
- Copied the Django source, `Templates/`, migrations and pinned requirements, omitting prior `.git`, uploaded images, SQLite database and virtual environment.
- Created a new Python virtual environment and installed dependencies from the copied `requirements.txt`.
- Verified `pip check`, `manage.py check`, full migrations, and HTTP 200 for the registration and listing pages.
- Completed an invalid form POST returning HTTP 200, then a valid registration POST returning HTTP 302; confirmed `/students/` and a saved image loaded with HTTP 200.
- Added and visually reviewed three Assignment 03 screenshots (form, saved listing, 151-character address validation). The length-error screenshot confirms the actual Django error message.
- Opened and visually reviewed Assignment 01 route `/` with its existing context values and styling.
- Opened Assignment 02 route `/home/`; the fresh database first had no profiles, then a local `Demo Profile` entry was created in `StudentProfile` and shown successfully (without an uploaded photo).
- Added screenshots for Assignment 01, Assignment 02, and Assignment 03 to the documentation package.
- **Still pending:** final source/settings check, publisher confirmation about third-party portraits, Git stage/commit, and GitHub publication.

See [Fresh Setup Verification](FRESH_SETUP_VERIFICATION.md) for detailed command outputs.

## Remaining release tasks

1. Confirm publication of the original identity details and right to display any portrait in screenshots.
2. Check the local `project/settings.py` for a non-hardcoded secret key and verify the app is for local development only.
3. Stage only reviewed source and documentation; inspect `git diff --cached --name-only` and `git diff --cached --check`.
4. Commit and push with the real November 2026 commit timestamp.
5. Verify the GitHub README, screenshot links, and project paths.
