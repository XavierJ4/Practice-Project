# Django-201 Social Feed

A Django-based social feed web application where users can sign up, create posts, follow others, and manage their profiles.

## Features

- User authentication (sign up, login, logout) with Django Allauth
- Create, view, and manage posts
- Follow/unfollow other users
- Profile page with profile picture
- Edit account info (username, email, password, profile image)
- Responsive UI with Tailwind CSS

## Setup

1. **Clone the repository**
   ```
   git clone <your-repo-url>
   cd django-201
   ```

2. **Install dependencies**
   ```
   pipenv install
   ```

3. **Apply migrations**
   ```
   python manage.py migrate
   ```

4. **Create a superuser**
   ```
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```
   python manage.py runserver
   ```

6. **Access the app**
   - Visit `http://localhost:8000/` in your browser

## Folder Structure

- `feed/` — Post models, views, templates
- `profiles/` — User profile models, views, templates
- `followers/` — Follow system
- `til/templates/` — Main templates
- `til/settings.py` — Project settings

## Customization

- UI styled with [Tailwind CSS](https://tailwindcss.com/)
- Authentication handled by [django-allauth](https://django-allauth.readthedocs.io/en/latest/)

## License

MIT License

---

Feel free to add more sections for API, contributing, or screenshots!