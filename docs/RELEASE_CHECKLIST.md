# Release and Submission Checklist

Status as observed November 6, 2026. A checked item is supported by the user-provided local terminal output; unchecked items are not yet verified in this clean copy.

- [x] Create a new, separate GitHub repository: [`MR7PRO/WEBC4301-Django-Assignments`](https://github.com/MR7PRO/WEBC4301-Django-Assignments).
- [x] Clone an empty new repository without reusing old Git history.
- [x] Copy Django project and templates without transferring old database, media or virtual environment.
- [x] Include `pages/migrations/0001_initial.py` and `0002_student.py`.
- [x] Include pinned Django 6.1.2 and Pillow 13.0.0 in `requirements.txt`.
- [x] Create and activate a new `.venv` within the new repository.
- [x] Run `python -m pip check` with no broken requirements.
- [x] Run `python manage.py check` with zero reported issues.
- [x] Run all migrations in a new database; both app migrations applied successfully.
- [x] Serve `/students/` and `/add-student/` with HTTP 200.
- [x] Complete registration with test data and verify uploaded image, redirect and saved table in the **new** clone (HTTP 302 + 200 responses).
- [x] Re-run an invalid input submission in the new clone (HTTP 200, no redirect; exact validation error depends on screenshot review).
- [x] Open root `/` and earlier `/home/`; check rendering, including an inserted demonstration `StudentProfile`.
- [x] Place three Assignment 03 screenshot files in `docs/screenshots/assignment-03/`.
- [x] Visually inspect all three Assignment 03 screenshots for expected validation and registration output.
- [x] Add visual evidence for Assignment 01 and Assignment 02 (profile from a local test record).
- [ ] Final publisher confirmation regarding visibility of original personal data and right to share portrait imagery.
- [x] Verify `.gitignore` excludes `.venv/`, `db.sqlite3`, and `media/` via `git check-ignore -v`; inspect full untracked file list.
- [ ] Inspect final staged files before commit; verify source/settings and README links.
- [ ] Commit only source, migrations, docs and reviewed test assets to `main`.
- [ ] Verify the README and links after publishing to GitHub.
- [x] Confirm repository is public and the owner chose to retain original coursework identity details.
- [ ] Confirm that third-party portraits, if any, are authorized for public display.
- [ ] Submit the repository link and any screenshots required by the instructor.

**Academic transparency:** older assignment commits are linked as historical evidence; the new repository should use its actual commit dates, without recreating false historical history.
