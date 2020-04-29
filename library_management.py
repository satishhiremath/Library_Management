"""
This file has implementation for Library Management
"""

from library import Library
from user import User


def main():
    """Main function for library management"""
    books_list = ["book1", "book2", "book3"]
    library = Library(books_list)
    user = User("Satish Hiremath")
    library.view_and_get_books()
    user.request_book("book1", library)
    library.view_and_get_books()
    user.view_borrowed_list()
    user.return_book("book1", library)
    user.view_borrowed_list()
    library.view_and_get_books()


if __name__ == "__main__":
    main()
