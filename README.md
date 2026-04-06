# Blogging Platform API

A production-grade RESTful API built with Django & Django REST Framework for managing blog posts, users, categories, and tags.

## Features

- JWT Authentication
- Full CRUD for Posts, Users, Categories, Tags
- Filter by Author, Category, Tags, Published Date
- Full-text search across Title, Content, Tags, Author
- Pagination & sorting
- Stretch: Comments, Drafts/Publishing, Post Likes, User Profiles

## Tech Stack

- Python 3.11+
- Django 4.2
- Django REST Framework 3.15
- SimpleJWT
- PostgreSQL (production) / SQLite (dev)
- django-filter
- whitenoise (static files)
- gunicorn (production server)

## Quick Start

```bash
git clone https://github.com/yourname/blogging-platform-api
cd blogging-platform-api
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env         # fill in your values
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API Endpoints Summary

| Method         | Endpoint                    | Description                     |
| -------------- | --------------------------- | ------------------------------- |
| POST           | /api/auth/register/         | Register user                   |
| POST           | /api/auth/login/            | Obtain JWT tokens               |
| POST           | /api/auth/token/refresh/    | Refresh token                   |
| GET/POST       | /api/posts/                 | List / create posts             |
| GET/PUT/DELETE | /api/posts/{id}/            | Retrieve / update / delete post |
| GET            | /api/posts/?category=tech   | Filter by category slug         |
| GET            | /api/posts/?author=username | Filter by author                |
| GET            | /api/posts/?search=django   | Search posts                    |
| GET/POST       | /api/posts/{id}/comments/   | List / add comments             |
| POST           | /api/posts/{id}/like/       | Like a post                     |
| GET/POST       | /api/categories/            | List / create categories        |
| GET/POST       | /api/tags/                  | List / create tags              |
| GET/PUT        | /api/users/{id}/            | User profile                    |

## Deployment (Heroku)

```bash
heroku create your-app-name
heroku addons:create heroku-postgresql:mini
heroku config:set DJANGO_SETTINGS_MODULE=blogging_platform.settings.production
heroku config:set SECRET_KEY=your-secret-key
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
git push heroku main
heroku run python manage.py migrate
```
