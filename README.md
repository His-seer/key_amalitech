
Key Manager Web Application

This Django-based web application serves as a key manager for a school management platform.
It allows administrators to manage access keys and provides users with a secure way to access various services.

Table of Contents

- [Features]
- [Installation]
- [Usage]
- [Running Tests]
- [Folder Structure]
- [Contributing]
- [License]

Features

- Admin panel for managing access keys.
- User authentication and authorization.
- API endpoints for key status checks.
- Automated tests for key functionalities.

Installation

Prerequisites

- Python 3.6+
- Django 3.2+
- PostgreSQL or any other supported database.

Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/key_manager.git
    cd key_manager
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure the database:
    Update the `DATABASES` setting in `key_amalitech/settings.py` with your database credentials.

5. Run migrations:
    ```sh
    python manage.py migrate
    ```

6. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

7. Start the development server:
    ```sh
    python manage.py runserver
    ```

Usage

- Access the admin panel at `http://127.0.0.1:8000/admin` to manage access keys.
- Users can log in and view their key status at `http://127.0.0.1:8000/`.

Running Tests

To run the automated tests, use the following command:

```sh
python manage.py test
```

Folder Structure

```
key_manager/
├── key_amalitech/         # Main project directory
│   ├── __init__.py
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL configurations
│   ├── asgi.py
│   └── wsgi.py
├── key/                   # Key management app
│   ├── __init__.py
│   ├── admin.py           # Admin configurations
│   ├── apps.py
│   ├── models.py          # Data models
│   ├── tests.py           # Automated tests
│   ├── urls.py            # URL configurations for the app
│   └── views.py           # View functions
├── manage.py              # Django management script
└── requirements.txt       # Project dependencies
```

Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.


