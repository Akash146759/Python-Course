class Library:
    def __init__(self, books):
        # Constructor: Initializes the library with a list of books
        self.books = books
        print("Welcome to the Library Management System!")

    def display_books(self):
        # Display the list of available books
        if self.books:
            print("Available books:")
            for book in self.books:
                print("- " + book)
        else:
            print("No books are currently available in the library.")

    def borrow_book(self, book_name):
        # Borrow a book from the library
        if book_name in self.books:
            self.books.remove(book_name)
            print("You have borrowed the book: " + book_name)
        else:
            print("Sorry, the book '" + book_name + "' is not available in the library.")

    def return_book(self, book_name):
        # Return a book to the library
        self.books.append(book_name)
        print("Thank you for returning the book: " + book_name)

    def __del__(self):
        # Destructor: Called when the library object is destroyed
        print("Library system is shutting down. Have a great day!")

# Initializing the library with a list of books
library = Library(["Python Programming", "AI Basics", "Data Science 101", "Machine Learning Mastery"])

# Display available books
library.display_books()

# Borrowing books
library.borrow_book("Python Programming")
library.borrow_book("Deep Learning")

# Returning a book
library.return_book("Python Programming")

# Display the updated list of books
library.display_books()

# Deleting the library object
del library
