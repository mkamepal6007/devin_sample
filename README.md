# devin_smaple

A minimal Python "Hello World" web stack built with Flask.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python wsgi.py            # dev server on http://localhost:8000
gunicorn wsgi:application  # production-style server
```

## Endpoints

| Path | Description |
| --- | --- |
| `/` | HTML page rendering "Hello, World!" |
| `/api/hello` | JSON `{"message": "Hello, World!"}` |
| `/health` | JSON `{"status": "ok"}` |

## Test

```bash
pytest
```
