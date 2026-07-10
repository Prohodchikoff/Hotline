# Hotline

## Description

Hotline is a Django project for price comprasion.

## Project structure

- `src/` — main Django project folder.
- `src/core/` — project settings, URL configuration.
- `src/*` — app modules.


## Setup

1. Create a Python virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy the example environment file and update values as needed:

```bash
cp .env.example .env
```

4. Edit `.env` to set your database credentials and secret key.

Example `.env` contents:

```env
SECRET_KEY=django-secret-key
DBNAME=hotline
DBUSER=hotline_user
DBPASSWORD=000000
DBHOST=127.0.0.1
DBPORT=5432
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Database setup

The project uses PostgreSQL. Make sure your database is created and accessible with the credentials from `.env`.

## Run locally

1. Change into the `src` directory:

```bash
cd src
```

2. Apply migrations:

```bash
python manage.py migrate
```

3. Create a superuser:

```bash
python manage.py createsuperuser
```

4. Start the development server:

```bash
python manage.py runserver
```

## Common commands

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`

## Dependencies

See `requirements.txt` for the full list of Python packages.
