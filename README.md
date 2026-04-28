# Daloopa Backend Coding Challenge

Starter project for Daloopa's backend coding challenge.

**Stack:** Django + Django REST Framework

This is the starter for a **live coding session** during the technical interview — you'll clone this repo and work in it with your interviewer.

## Setup

Requires Python 3.11+.

```bash
python3 -m venv .venv
source .venv/bin/activate         # macOS/Linux
# .venv\Scripts\activate          # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The dev server runs at http://localhost:8000.

## What's in the box

- `config/` — Django project (settings, root URL conf).
- `api/` — empty Django app where you'll work. `models.py`, `views.py`, and `urls.py` are bootstrapped empty.
- `api/seed.py` — pre-written `generate_company_data()` helper. Returns a flat list of ~4,000 dicts (500 companies × 8 quarters), with company info (`ticker`, `name`) repeated across each company's records. Use it as input to your seeding routine.

That's it — your interviewer will share the full task at the start of the session.
