class Book:
    def __init__(self, title, author, isbn, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.borrowed_copies = 0

    def __repr__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.total_copies - self.borrowed_copies}/{self.total_copies} available"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn, total_copies):
        book = Book(title, author, isbn, total_copies)
        self.books.append(book)
        print(f"Book added: {book}")

    def update_book(self, isbn, title=None, author=None, total_copies=None):
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                if total_copies:
                    book.total_copies = total_copies
                print(f"Book updated: {book}")
                return
        print("Book not found.")

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book deleted: {book}")
                return
        print("Book not found.")

    def search_books(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if results:
            print("Search results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.borrowed_copies < book.total_copies:
                    book.borrowed_copies += 1
                    print(f"You have borrowed: {book.title}")
                else:
                    print("No copies available to borrow.")
                return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.borrowed_copies > 0:
                    book.borrowed_copies -= 1
                    print(f"You have returned: {book.title}")
                else:
                    print("No copies have been borrowed.")
                return
        print("Book not found.")

    def display_books(self):
        if self.books:
            print("Library books:")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")

# Example usage
library = Library()

# Adding books
library.add_book("1984", "George Orwell", "1234567890", 5)
library.add_book("To Kill a Mockingbird", "Harper Lee", "0987654321", 3)

# Display books
library.display_books()

# Update a book
library.update_book("1234567890", title="Nineteen Eighty-Four")

# Search for books
library.search_books("Harper")

# Borrow a book
library.borrow_book("1234567890")

# Return a book
library.return_book("1234567890")

# Delete a book
library.delete_book("0987654321")

# Display updated library
library.display_books()
