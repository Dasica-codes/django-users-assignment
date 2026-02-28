# Django Users Assignment

## Setup Instructions

1. Create virtual environment:
   python -m venv venv

2. Activate:
   venv\Scripts\activate

3. Install dependencies:
   pip install django mysqlclient

4. Create MySQL database:
   CREATE DATABASE users;

5. Configure database in settings.py

6. Run migrations:
   python manage.py migrate

7. Start server:
   python manage.py runserver

---

## Routes

- /users/hello/ → Hello World
- /users/ → List all users
- /users/new_user/ → Add new user
- /users/<id>/ → Get specific user

---

## Database Schema

Table: users_user

- id (Primary Key)
- name (varchar)
- email (varchar)
- role (varchar)
