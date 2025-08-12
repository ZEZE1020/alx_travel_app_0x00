# alx_travel_app_0x00

# alx_travel_app_0x00

alx_travel_app_0x00 is a Django-based backend project prepared for scalable travel-related features and seamless collaboration across multiple teams.

## Features

- Django 5.x project structure
- `listings` app scaffolded for future development
- MySQL database configuration using environment variables
- REST API support via Django REST Framework
- CORS enabled for cross-origin requests
- Celery and RabbitMQ ready for asynchronous/background tasks
- Swagger (drf-yasg) for automatic API documentation at `/swagger/`
- Environment variable management via `django-environ`

## Setup Instructions

### 1. Clone the repository

```sh
git clone <repo-url>
cd alx_travel_app
```

### 2. Create and activate a virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and update values as needed:

```sh
cp .env.example .env
```

### 5. Set up MySQL

- Ensure MySQL is running.
- Create the database and user as specified in `.env`.

### 6. Run migrations

```sh
python alx_travel_app/manage.py migrate
```

### 7. Create a superuser (optional)

```sh
python alx_travel_app/manage.py createsuperuser
```

### 8. Start the development server

```sh
python alx_travel_app/manage.py runserver
```

### 9. Access API documentation

Visit [http://localhost:8000/swagger/](http://localhost:8000/swagger/) for Swagger UI.

## Project Structure

- `alx_travel_app/` - Django project root
- `alx_travel_app/alx_travel_app/` - Django settings, URLs, WSGI/ASGI
- `alx_travel_app/listings/` - App for travel listings (scaffolded)
- `.env.example` - Example environment variables
- `requirements.txt` - Python dependencies

## Environment Variables

See `.env.example` for all required variables:

- `DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`

## Celery & RabbitMQ

Celery and RabbitMQ are included in requirements for future async/background task support. See [Celery documentation](https://docs.celeryq.dev/en/stable/getting-started/introduction.html) for setup.

## License

MIT or as specified by your organization.
