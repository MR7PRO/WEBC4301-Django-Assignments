# Fresh Setup Verification — November 6, 2026

**Target:** `MR7PRO/WEBC4301-Django-Assignments`\
**Environment:** Windows, Python 3.14, a new `.venv`, Django 6.1.2, Pillow 13.0.0, SQLite.\
**Scope:** Local setup verification; no production deployment or automated end-to-end test is implied.

## Commands and observed results

| Action | Evidence from local terminal |
|---|---|
| `git clone https://github.com/MR7PRO/WEBC4301-Django-Assignments.git` | Empty repo cloned; expected `No commits yet` |
| Source copy | `project/`: 5 files, `pages/`: 11 files, `Templates/`: 6 files, plus `manage.py`, `.gitignore`, `requirements.txt` |
| `.venv\Scripts\activate` and `where python` | First Python path pointed to new repository `.venv` |
| `python -m pip install -r requirements.txt` | Installed Django 6.1.2, Pillow 13.0.0, asgiref 3.12.1, sqlparse 0.6.0, tzdata 2026.5 |
| `python -m pip check` | `No broken requirements found.` |
| `python manage.py check` | `System check identified no issues (0 silenced).` |
| `python manage.py migrate` | All built-in app and `pages` migrations applied successfully |
| `python manage.py showmigrations pages` | `[X] 0001_initial`, `[X] 0002_student` |
| `python manage.py runserver 8001` | Server started normally |
| `GET /students/` | HTTP 200 |
| `GET /add-student/` | HTTP 200 |
| First `POST /add-student/` | HTTP 200, form re-rendered; reason not visible in server log |
| Second `POST /add-student/` | HTTP 302 redirect after valid submission |
| `GET /students/` after submission | HTTP 200 |
| `GET /media/student_photos/...png` | HTTP 200; 1,746,215-byte image response in log |
| `python manage.py check` after submission | `System check identified no issues (0 silenced).` |

### Additional browser checks

| URL | Observed result |
|---|---|
| `/` | Earlier context/template page rendered; owner details and template filters displayed |
| `/home/` (clean database) | Page rendered, initially without `StudentProfile` rows |
| `/home/` after a demo profile was created | `Demo Profile` card displayed name, ID, age, date, address, salary and no-photo placeholder |

### Notes

- `GET /favicon.ico` returned 404; the project does not currently provide a favicon. This does not affect the assignment pages.
- The standard warning about Django's development server is expected. These instructions are for **local coursework only**.
- A fresh local database was created from migrations. Database rows and uploaded files from the old project were not included.
- The clean copy **has now completed** a student submission with redirect, table rendering, and image HTTP 200, as reported in the November 6 terminal log.
- The first POST returned HTTP 200, which is compatible with form validation preventing a redirect, but the precise reason cannot be established from HTTP status alone.
- All three Assignment 03 screenshots were visually reviewed in the walkthrough: the 151-character address produces the expected Django field error; the student listing shows the saved demonstration record; and the registration form displays all seven fields. The screenshot directory and filenames were also confirmed by `dir`. The owner is retaining original identity information for the earlier coursework; see the separate publication review.
