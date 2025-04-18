# CircadiaN Blog

A modern blog platform built with Django.

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd BlogWebsite
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate
# OR simply run:
activate.bat

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The site will be available at http://127.0.0.1:8000/

## Features

- User Authentication
- Blog Post Creation and Management
- Categories and Tags
- Rich Text Editor
- Responsive Design
- Search Functionality
- User Profiles

## Project Structure

```
BlogWebsite/
├── venv/                   # Virtual environment
├── apps/                   # Django apps
│   ├── blog/              # Blog app
│   └── users/             # User management app
├── static/                # Static files
├── media/                 # User uploaded files
├── templates/             # HTML templates
├── manage.py             # Django management script
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Development

To contribute to this project:

1. Create a new branch for your feature
2. Make your changes
3. Run tests
4. Submit a pull request

## License

This project is licensed under the MIT License. 