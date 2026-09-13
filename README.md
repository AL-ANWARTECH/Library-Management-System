# Library Management System

A console-based **Library Management System** built with Python and Object-Oriented Programming (OOP).

This project was created as a practical OOP project to strengthen Python programming skills through a real-world application.

## Features

* Add books
* Register library members
* Display all books
* Display all members
* Borrow books
* Return books
* Search books by title
* Search books by author
* Search books by ID
* Search members by ID
* Search members by name
* Prevent duplicate book IDs
* Prevent duplicate member IDs
* Validate member email addresses
* Validate numeric IDs
* Handle invalid user input
* Track book availability
* Track books borrowed by members
* Reusable helper functions
* Clean and organized project structure

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Git
* GitHub
* Visual Studio Code

## Project Structure

```text
Library-Management-System/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── book.py
│   └── member.py
│
├── services/
│   ├── __init__.py
│   └── library.py
│
├── exceptions/
│   ├── __init__.py
│   └── errors.py
│
└── README.md
```

## File Responsibilities

### `main.py`

Contains the main application, menu system, user input handling, and helper functions.

### `models/book.py`

Contains the `Book` class.

A book contains:

* Book ID
* Title
* Author
* Availability status

### `models/member.py`

Contains the `Member` class.

A member contains:

* Member ID
* Name
* Email
* Borrowed books

### `services/library.py`

Contains the `Library` class and the main library business logic.

The library manages:

* Books
* Members
* Adding books
* Registering members
* Borrowing books
* Returning books
* Searching books
* Searching members

### `exceptions/errors.py`

Reserved for custom exceptions and future error-handling improvements.

## How to Run

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

### 2. Navigate into the project

```bash
cd Library-Management-System
```

### 3. Run the application

On Windows:

```bash
py main.py
```

You can also use:

```bash
python main.py
```

## Main Menu

When the application starts, the following menu is displayed:

```text
===== LIBRARY MANAGEMENT SYSTEM =====
1. Add Book
2. Register Member
3. Display Books
4. Display Members
5. Borrow Book
6. Return Book
7. Search Book
8. Search Member
9. Exit
```

## Example Workflow

### Add a Book

```text
Enter your choice: 1
Enter book ID: 1
Enter book title: Python Crash Course
Enter book author: Eric Matthes

Book 'Python Crash Course' added successfully.
```

### Register a Member

```text
Enter your choice: 2
Enter member ID: 1
Enter member name: Anwar
Enter member email: anwar@example.com

Member 'Anwar' registered successfully.
```

### Borrow a Book

```text
Enter your choice: 5
Enter member ID: 1
Enter book ID: 1

Anwar borrowed 'Python Crash Course' successfully.
```

### Return a Book

```text
Enter your choice: 6
Enter member ID: 1
Enter book ID: 1

Anwar returned 'Python Crash Course' successfully.
```

## OOP Concepts Practiced

This project demonstrates several important Python Object-Oriented Programming concepts:

* Classes
* Objects
* Constructors (`__init__`)
* Instance attributes
* Instance methods
* Encapsulation
* Composition
* Object relationships
* Lists of objects
* Separation of responsibilities
* Input validation
* Exception handling
* Reusable functions

## Validation and Error Handling

The application handles common input and business-logic errors, including:

* Non-numeric book IDs
* Non-numeric member IDs
* Invalid email addresses
* Duplicate book IDs
* Duplicate member IDs
* Unregistered members
* Unregistered books
* Books that are already borrowed
* Returning a book that the member did not borrow
* Books or members that cannot be found
* Invalid menu options

## Example Error Messages

```text
Invalid book ID. Please enter a number.
```

```text
Invalid ID. Please enter numbers only.
```

```text
Error: Invalid email address.
```

```text
Book 'Python Crash Course' not found.
```

```text
Member not found.
```

```text
'Python Crash Course' is not available.
```

## Learning Goals

The main goal of this project was to strengthen Python OOP skills by building a complete application from scratch.

The project also provided practical experience with:

* Python project organization
* Object-oriented design
* Reusable functions
* Business logic
* Input validation
* Error handling
* Git
* GitHub
* Code refactoring
* Clean Python code

## Future Improvements

Possible future versions of this project could include:

* MySQL database integration
* Persistent data storage
* User authentication
* Admin and member roles
* Book categories
* Book quantities
* Due dates
* Late-return penalties
* Borrowing history
* Django backend
* Django REST Framework API
* JWT authentication
* Swagger API documentation
* React frontend
* Cloud deployment

## Backend Development Roadmap

This project can later be upgraded from a console application into a professional backend system:

```text
Python OOP
    ↓
Django
    ↓
Django REST Framework
    ↓
MySQL
    ↓
JWT Authentication
    ↓
REST API
    ↓
Swagger Documentation
    ↓
Testing
    ↓
Docker
    ↓
Deployment
```

## Author

**Anwar Sagir Mustapha**

Computer Science Student | Python Backend Developer in Training

## License

This project was created for learning, practice, and portfolio development.
