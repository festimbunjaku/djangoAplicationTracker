# Django Application Tracker

A Django REST API backend for tracking job applications. This project provides a robust REST API for managing job applications with user authentication and comprehensive application tracking features.

## Features

- **REST API Backend**: Built with Django REST Framework for a modern API-first approach
- **User Authentication**: 
  - JWT (JSON Web Token) based authentication
  - Email-based registration and authentication
  - Token refresh and blacklisting support
  - Social authentication support (configured but needs provider setup)

- **Application Tracking**:
  - Track job applications with detailed information:
    - Job Title
    - Company Name
    - Location
    - Application Date
    - Application Status (Applied, Interview, Offer Received, Rejected, Accepted)
    - Job Link
    - Notes
    - Resume Version

- **Security Features**:
  - CORS support with configurable origins
  - Secure cookie handling
  - Environment-based configuration
  - Protected API endpoints

## Technical Stack

- **Backend**: Django 5.2
- **API**: Django REST Framework
- **Authentication**: 
  - dj-rest-auth
  - django-allauth
  - Simple JWT
- **Database**: PostgreSQL (configurable through environment variables)
- **CORS**: django-cors-headers

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/festimbunjaku/djangoAplicationTracker.git
cd djangoAplicationTracker
```

2. **Set up environment variables**
Create a `.env` file in the root directory with the following variables:
```
SECRET_KEY=your_secret_key
DEBUG=True
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
EMAIL_HOST=your_email_host
EMAIL_PORT=587
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_email_password
EMAIL_USE_TLS=True
```

3. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run the development server**
```bash
python manage.py runserver
```

## API Endpoints

### Authentication Endpoints
- `POST /api/token/`: Obtain JWT token pair
- `POST /api/token/refresh/`: Refresh JWT token
- `POST /dj-rest-auth/registration/`: Register new user
- `POST /dj-rest-auth/login/`: Login user
- `POST /dj-rest-auth/logout/`: Logout user

### Application Endpoints
- `GET /api/applications/`: List all applications for authenticated user
- `POST /api/applications/`: Create new application
- `GET /api/applications/{id}/`: Retrieve specific application
- `PUT /api/applications/{id}/`: Update specific application
- `DELETE /api/applications/{id}/`: Delete specific application

## Security Considerations

- Debug mode should be disabled in production
- CORS settings should be properly configured for production
- Proper SSL/TLS certificates should be installed for HTTPS
- Environment variables should be properly secured
- Cookie security settings should be adjusted for production

## Development

The project follows Django's standard application structure:
```
djangoAplicationTracker/
├── application/           # Main application module
├── auth/                 # Custom authentication module
├── config/              # Project configuration
├── manage.py
├── requirements.txt
└── .env
```



## License

This project is open source and available under the MIT License.
