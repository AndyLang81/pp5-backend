# PP5 Task Manager - Backend

## Overview

This is the **backend** of the PP5 Task Manager, built with **Django** and **Django REST Framework**. It handles API endpoints for user authentication and task CRUD operations. The API supports token-based authentication using **Simple JWT**.

## Live API

[Render Backend Deployment](https://pp5-backend.onrender.com/api/)

## Features

- Token-based authentication (JWT)
- Create, Read, Update, Delete task endpoints
- Secure, permission-based access
- CORS enabled for frontend integration
- PostgreSQL-compatible configuration
- Whitenoise static file handling

## Technologies Used

- Django
- Django REST Framework
- Simple JWT
- Gunicorn
- Render for deployment

## Setup Instructions

1. Clone the backend repo:
   ```bash
   git clone https://github.com/yourusername/pp5-backend.git
   cd pp5-backend
   ```

2. Create a `.env` file:
   ```
   SECRET_KEY=your_secret_key
   DEBUG=False
   ALLOWED_HOSTS=pp5-backend.onrender.com,localhost,127.0.0.1
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the server locally:
   ```bash
   python manage.py runserver
   ```

## Endpoints

- `POST /api/token/` - Login and obtain JWT
- `POST /api/token/refresh/` - Refresh token
- `GET /api/tasks/` - List user’s tasks
- `POST /api/tasks/` - Create new task
- `PUT /api/tasks/<id>/` - Edit task
- `DELETE /api/tasks/<id>/` - Delete task

## User Stories

- As a developer, I want secure endpoints for users and their tasks.
- As a developer, I want to verify and authorize users using JWT tokens.
- As a developer, I want full CRUD operations on tasks.
- As a developer, I want the backend to be easy to connect to from a React frontend.

## Testing

- Manual testing using Postman and curl
- Tested endpoint responses, authentication headers, and error handling
- Admin panel used for data verification

## Deployment

- Deployed using Render
- Environment variables securely set in Render dashboard
- Static files collected using `whitenoise`
- `Procfile` used to launch gunicorn server

## Author

- Your Name