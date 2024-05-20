
# Online Bookstore

## Project Overview

This is an online bookstore web application built using Django. The bookstore allows users to browse, search, purchase, and review books. Users can register, log in, and manage their profiles. The project also includes a shopping cart feature for purchasing books. Admin functionality to manage books, orders, and user accounts is partially implemented.

## Features

- **Browse Books**: Users can browse all available books (Currently 5/6 books are in list)
- **Book Details**: View detailed information about each book.
- **Search Books**: Search for books by title, author.
- **User Authentication**: Users can register, log in and logout.
- **Shopping Cart**: Add books to a cart.
- **Purchase Books**: Only authenticated users can purchase books.
- **Admin Panel**: Manage books, orders, and user accounts (Partially implemented).

## Models

### Book Model
- `title` (CharField)
- `author` (CharField)
- `description` (TextField)
- `price` (DecimalField)
- `publication_date` (DateField)
- `cover_image` (ImageField) - 

## Views

### Book Views
- List all books
- View details of a book
- Search for books by title, author, or keyword

### Book Purchase (Optional)
- Add books to a shopping cart
- View and manage items in the shopping cart

### User Authentication
- Register, log in, and manage user profiles
- Only authenticated users can purchase books and write reviews

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or 4.x
- Git
- Virtualenv (recommended)

### Steps

1. **Clone the repository**
    ```bash
    git clone https://github.com/your-username/online-bookstore.git
    cd online-bookstore
    ```

2. **Create and activate a virtual environment**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run database migrations**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser for the admin panel**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**
    ```bash
    python manage.py runserver
    ```

7. **Access the application**
    - Open your browser and go to `http://127.0.0.1:8000` to access the bookstore.
    - Go to `http://127.0.0.1:8000/admin` to access the admin panel.

## Usage

### Admin Panel
- Use the admin panel to manage books, orders, and user accounts.
- Login with the superuser credentials created during setup.

### Browse and Search Books
- Navigate to the homepage to browse all available books.
- Use the search bar to find books by title, author.

### User Registration and Authentication
- Register a new account to purchase books .
- Log in to manage your profile, add books to the cart.

### Shopping Cart (Optional)
- Add books to the shopping cart.
- View and manage items in the cart.


