# Saba Space

A personal website to gather all of my curiosities, built with Django REST Framework backend and React/Vite frontend.

## Project Overview

This project is a personal website that includes:
- A portfolio section to showcase projects
- A blog for writing articles
- A resume/CV section
- A home page with personal information

The project is split into two main parts:
1. **Backend**: A Django REST Framework API (`django-website` directory)
2. **Frontend**: A React application built with Vite (`frontend` directory)

## Directory Structure

```
saba-space/
├── django-website/      # Django backend API
│   ├── blog/            # Blog app
│   ├── home/            # Home page app  
│   ├── mysite/          # Django project settings
│   ├── portfolio/       # Portfolio app
│   ├── resume/          # Resume app
│   ├── manage.py        # Django management script
│   └── requirements.txt # Python dependencies
└── frontend/            # React frontend
    ├── public/          # Static assets
    ├── src/             # Source code
    │   ├── components/  # React components
    │   ├── pages/       # Page components
    │   ├── services/    # API services
    │   └── ...          # Other source files
    ├── package.json     # Node.js dependencies
    └── ...              # Other configuration files
```

## Prerequisites

- Python 3.6+ with pip
- Node.js 18+ with npm or bun
- Git

## Setup Instructions

### Backend Setup (Django)

1. Navigate to the Django project directory:
```bash
cd django-website
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run the migrations:
```bash
python manage.py migrate
```

5. Create a superuser to access the admin panel:
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

The Django API will be running at http://localhost:8000/

### Frontend Setup (React/Vite)

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install the dependencies:
```bash
npm install
# or if you use bun
bun install
```

3. Start the development server:
```bash
npm run dev
# or if you use bun
bun run dev
```

The frontend application will be running at http://localhost:8080/

## Usage

Once both servers are running:

- Access the frontend application: http://localhost:8080/
- Access the Django admin panel: http://localhost:8000/admin/ (using the superuser credentials)
- Access the API endpoints: http://localhost:8000/api/

### API Endpoints

- `/api/home/` - Home page data
- `/api/posts/` - Blog posts
- `/api/projects/` - Portfolio projects
- `/api/education/` - Education information
- `/api/experience/` - Work experience
- `/api/skills/` - Skills
- `/api/certifications/` - Certifications

## Building for Production

### Backend

For deploying the Django backend to production, follow Django's deployment guide: https://docs.djangoproject.com/en/3.2/howto/deployment/

### Frontend

To build the frontend for production:

```bash
cd frontend
npm run build
# or if you use bun
bun run build
```

This will generate a production build in the `dist` directory, which can be served by any static file server.

## Technologies Used

### Backend
- Django 3.2
- Django REST Framework
- SQLite (default, can be changed in settings)

### Frontend
- React
- TypeScript
- Vite
- TanStack Query (formerly React Query)
- Tailwind CSS
- shadcn/ui components
- React Router

## License

This project is open-sourced under the MIT license.
