# Django Fullstack Application for Blog Posts

A Django fullstack application that includes the basic structure and functionality for a Django-based web application allowing users to perform CRUD (Create, Read, Update, Delete) operations on blog posts. The application includes models for blog posts, views to render templates and handle HTTP requests, and forms to handle user input.

It uses the Django's LoginView class to display the login form and process the registered user's data and authenticate them.

For blog posts protection, users can view their blogs when they sign in, and they need to be the owners of posts they perform get, edit or delete operations on. Posting is available for any signed in user.

There's still a lot of work to be done, but this sets the foundation for the project.


The main features of the application include:

- User authentication and authorization
- Creation of new blog posts
- Display of existing blog posts in a paginated manner
- Updating and deleting existing blog posts

## Installation

1. Clone the repository to your local machine
2. Create a virtual environment using Python 3.x
3. Install the required packages
4. Set up the database by running `python manage.py migrate`
5. Create a superuser by running `python manage.py createsuperuser`
6. Start the development server by running `python manage.py runserver`

## Usage

1. Open your browser and go to `http://localhost:8000`
2. Log in with your superuser credentials
3. Create, read, update, or delete blog posts as desired

## Acknowledgments

- [Django](https://www.djangoproject.com/)
