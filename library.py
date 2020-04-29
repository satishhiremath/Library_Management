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
            print("Books available in library:", self.__available_books_list)
        return self.__available_books_list

    def lend_book(self, requested_book: List) -> bool:
        """Lends requested book to user"""
        lend_successful = True
        if requested_book in self.__available_books_list:
            self.__available_books_list.remove(requested_book)
        else:
            lend_successful = False
        return lend_successful

    def add_book(self, book_name: str):
        """Adds the returned book to library"""
        self.__available_books_list.append(book_name)
