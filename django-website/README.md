# README.md

# Django Personal Website

This project is a personal website built using Django. It includes sections for a blog, portfolio, and resume.

## Project Structure

- `manage.py`: Command-line utility for interacting with the Django project.
- `requirements.txt`: Lists the Python packages required for the project.
- `mysite/`: Contains the main Django project settings and configuration.
- `blog/`: Contains the blog application with models, views, and templates for blog posts.
- `portfolio/`: Contains the portfolio application with models, views, and templates for projects.
- `resume/`: Contains the resume application with models, views, and templates for the CV section.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd django-website
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the blog at `/blog/`
- View the portfolio at `/portfolio/`
- Check the resume at `/resume/`

Feel free to customize the models and views as per your requirements.