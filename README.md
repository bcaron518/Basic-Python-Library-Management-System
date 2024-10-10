# Library Management System

A simple Python-based Library Management System that allows you to manage books in a library, including adding, updating, and deleting books, as well as borrowing and returning books.

## Features

- **Add a Book**: Add a new book to the library with its title, author, ISBN, and total copies available.
- **Update a Book**: Update the details of an existing book using its ISBN.
- **Delete a Book**: Remove a book from the library by its ISBN.
- **Search for a Book**: Search for books by title or author.
- **Borrow a Book**: Borrow a book if available copies exist.
- **Return a Book**: Return a borrowed book to the library.
- **Display Available Books**: Show all books currently in the library along with the available copies.

## Getting Started

### Prerequisites

- **Python 3.x**: Make sure Python is installed on your machine. You can download it from [here](https://www.python.org/downloads/).

### Installation

1. Clone the repository or download the project files.

```bash
git clone https://github.com/yourusername/library-management-system.git
```

2. Navigate to the project directory.

```bash
cd library-management-system
```

3. Run the script `library_system.py`.

```bash
python library_system.py
```

### Usage

1. **Add a Book**
   - Add a new book to the library by providing the title, author, ISBN, and total copies.

```python
library.add_book("1984", "George Orwell", "1234567890", 5)
```

2. **Update a Book**
   - Update book details using its ISBN. You can modify the title, author, and total copies.

```python
library.update_book("1234567890", title="Nineteen Eighty-Four")
```

3. **Delete a Book**
   - Remove a book from the library using its ISBN.

```python
library.delete_book("0987654321")
```

4. **Search for a Book**
   - Search for a book by entering a keyword from its title or author.

```python
library.search_books("Orwell")
```

5. **Borrow a Book**
   - Borrow a book by its ISBN, if copies are available.

```python
library.borrow_book("1234567890")
```

6. **Return a Book**
   - Return a previously borrowed book by its ISBN.

```python
library.return_book("1234567890")
```

7. **Display All Books**
   - View all books in the library, including how many copies are available.

```python
library.display_books()
```

### Example

Here’s a quick example of how the library system works:

```python
library = Library()

# Add books
library.add_book("1984", "George Orwell", "1234567890", 5)
library.add_book("To Kill a Mockingbird", "Harper Lee", "0987654321", 3)

# Display books
library.display_books()

# Search for books by author
library.search_books("George Orwell")

# Borrow a book
library.borrow_book("1234567890")

# Return a book
library.return_book("1234567890")

# Delete a book
library.delete_book("0987654321")

# Display updated library
library.display_books()
```

### Customization

You can extend the system by adding features like:
- User management (register users, track borrowed books per user).
- Book categories or genres.
- Handling overdue returns and late fees.
- Tracking book reservations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you’d like to contribute to this project, please fork the repository and create a pull request with your changes. 

## Contact

For any issues or suggestions, please contact `caron518@gmail.com`.
