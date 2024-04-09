# Book Store Django Project

## Overview
This Django project is a simple book store application where users can view a list of books and details of individual books.

## Setup
1. Make sure you have Python and Django installed on your system.
2. Clone this repository.
3. Navigate to the project directory in your terminal.

## Installation
1. Create a virtual environment: `python -m venv myenv`
2. Activate the virtual environment:
    - On Windows: `myenv\Scripts\activate`
    - On macOS and Linux: `source myenv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`

## Usage
1. Start the Django development server: `python manage.py runserver`
2. Navigate to `http://127.0.0.1:8000/books/` to view the list of books.
3. Click on a book to view its details at `http://127.0.0.1:8000/books/<book_id>/`.

## Project Structure
- `market/`: Django application directory.
    - `models.py`: Defines the database models including the `Book` model.
    - `admin.py`: Registers the `Book` model with the Django admin site.
    - `views.py`: Contains view functions for handling HTTP requests related to books.
- `book_store/`: Directory for storing uploaded book images.
- `manage.py`: Django management script.
- `README.md`: Documentation for the project.
- `requirements.txt`: List of Python dependencies for the project.

## Models
- `Book`:
    - `name`: Name of the book (CharField).
    - `page_count`: Number of pages in the book (IntegerField).
    - `category`: Category of the book (CharField).
    - `author_name`: Name of the author (CharField).
    - `price`: Price of the book (DecimalField).
    - `image`: Image of the book (ImageField).

## URLs
- `/books/`: Endpoint to view the list of books.
- `/books/<book_id>/`: Endpoint to view details of a specific book.

## Admin Panel
- Access the Django admin panel at `http://127.0.0.1:8000/admin/`.
- Use admin credentials to login and manage books.

## API Endpoints
- `/books/`: Returns JSON data of all books.
- `/books/<book_id>/`: Returns JSON data of a specific book.

## Credits
This project is created by [Saba Katamadze].

Feel free to reach out with any questions or feedback!
