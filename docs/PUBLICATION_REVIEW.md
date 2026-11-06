# Public Repository — Publication Review

**Repository:** `MR7PRO/WEBC4301-Django-Assignments`\
**Review date:** November 6, 2026\
**Context:** a local Django coursework project, not a hosted production app.

## Owner's publication decision

The coursework author explicitly chose to **retain the original Assignment 01 identity details** rather than replace them with fictional data. The original template/context page contains the author's name, university ID and email. These are intentional coursework values, and will become accessible to anyone while the repository is public. The same source values can also be read directly from `pages/views.py`.

## Verified exclusions

The user's `git check-ignore -v` output confirms that `.venv/`, `db.sqlite3` and `media/` are ignored. A full `git status --short --untracked-files=all` contained the application source, documentation and screenshot evidence, without those excluded local folders. This is a check of **ignore behavior**, not a proof that every source file is safe to publish.

## Verified after first publication

- The published repository contains application source, the README, documented assignment history, and five screenshot paths.
- The local check found no literal `SECRET_KEY`; environment-variable support and a generated development fallback were confirmed.
- `.venv/`, `db.sqlite3`, and `media/` were excluded during staging, and the first push completed with a clean working tree.
- The user approved publishing original Assignment 01 details; the linked GitHub repository remains public.

## Remaining manual confirmations

- **Portrait in Assignment 03 listing:** verify the depicted person's image is self-owned, generated with suitable rights, or otherwise authorized for publication. The demonstration image is separate from `media/` and is visible inside the screenshot.
- **Real contact and ID information:** original Assignment 01 values were intentionally retained, but do not insert real registrant IDs, phone numbers or private third-party data into examples.
- **Development settings:** `DEBUG=True` and the Django development server are intended only for local coursework, not production deployment.
- **Browser screenshots:** visible browser UI/bookmarks may reveal personal information. Confirm that public display is acceptable.
- **Future commits:** continue inspecting `git diff --cached --name-only` and `git diff --cached --check` before pushing new work; do not stage raw uploads, local databases, virtual environments or credentials.

This checklist does **not** assert that every possible security issue has been audited, or that this project is production-safe.
