"""
This class implements all the functionality related to Library
"""
from typing import List


class Library(object):
    def __init__(self, books_list):
        """Initializes the Library class variables"""
        self.__available_books_list = books_list

    def view_and_get_books(self) -> List:
        """Display list of books in Library"""
        if not len(self.__available_books_list):
            print("Library is Empty")
        else:
            print("Books available in library:")
            for book in self.__available_books_list:
                print("----", book)
        return self.__available_books_list


if __name__ == "__main__":
    books = ["book1", "book2", "book3", "book1"]
    library = Library(books)
    library.view_and_get_books()
