# Hotline

API backend for comparing product prices across online stores (Hotline/Rozetka-style). No purchases — catalog, offers, and price comparison only.

## Project structure

```
Hotline/
├── docker-compose.yml    # PostgreSQL for local development
├── .env.example          # Environment variable template
├── requirements.txt
└── src/
    ├── manage.py
    ├── core/             # Settings, URLs, WSGI/ASGI
    ├── product/          # Products and images
    ├── categories/       # Category tree (MPTT)
    └── attributes/       # Product attributes (EAV)
```

## Prerequisites

- Python 3.12+
- Docker and Docker Compose
- Git

## Quick start

### 1. Clone and set up Python

```bash
git clone <repo-url>
cd Hotline

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### 2. Configure environment

```bash
cp .env.example .env
```

Edit `.env`. When using Docker Compose, **set the host port to `5432`** — the container maps `5432:5432`:

```env
SECRET_KEY=change-me
DEBUG=True

DBNAME=hotline
DBUSER=hotline_user
DBPASSWORD=000000
DBHOST=127.0.0.1
DBPORT=5432

ALLOWED_HOSTS=localhost,127.0.0.1
```

`DBUSER`, `DBPASSWORD`, and `DBNAME` must match the values used by Docker Compose (`POSTGRES_*`).

### 3. Start PostgreSQL

```bash
docker compose up -d
```

Check that the container is healthy:

```bash
docker compose ps
```

### 4. Run Django

```bash
cd src
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 5. Open in browser

| URL | Description |
|-----|-------------|
| http://127.0.0.1:8000/admin/ | Django admin |

REST API and Swagger docs will be added in later phases.

## Environment variables

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | random string |
| `DEBUG` | Debug mode | `True` |
| `DBNAME` | PostgreSQL database name | `hotline` |
| `DBUSER` | PostgreSQL user | `hotline_user` |
| `DBPASSWORD` | PostgreSQL password | `000000` |
| `DBHOST` | Database host (`127.0.0.1` when Django runs on host) | `127.0.0.1` |
| `DBPORT` | Database port (`5432` with Docker Compose) | `5432` |
| `ALLOWED_HOSTS` | Comma-separated hostnames | `localhost,127.0.0.1` |

## Common commands

All Django commands are run from the `src/` directory:

```bash
cd src

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py test
```

Docker:

```bash
docker compose up -d      # start database
docker compose down       # stop database (data kept)
docker compose down -v    # stop and delete all database data
```
