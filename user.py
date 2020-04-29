"""
This class implements all the functionality related to User
"""
from typing import List

from custom_exceptions import *


class User(object):
    def __init__(self, user_name: str):
        """Initializes the Library class"""
        self.__name = user_name
        self.__borrowed_list = []

    def request_book(self, book_name: str, library_obj):
        """Adds requested book to user borrowed list"""
        lend_status = library_obj.lend_book(book_name)

        if lend_status and len(self.__borrowed_list) < 2\
                and book_name not in self.__borrowed_list:
            self.__borrowed_list.append(book_name)
            print("Book: {} is borrowed by user: {}".format(book_name, self.__name))
        elif book_name in self.__borrowed_list:
            print("Book: {} already borrowed by User: {}".format(book_name, self.__name))
            raise BookAlreadyBorrowedByUser
        elif len(self.__borrowed_list) >= 2:
            print("Maximum borrow limit reached for user: {}".format(self.__name))
            raise MaximumBookBorrowLimit
        else:
            print("Requested book is not present in Library")
            raise BookNotPresentInLibrary

    def view_borrowed_list(self) -> List:
        """Displays all list of borrowed books for a user"""
        print("User: ({}) borrowed books:{}".format(self.__name, self.__borrowed_list))
        return self.__borrowed_list

    def return_book(self, book_name: str, library_obj):
        """Returns borrowed book to library"""
        if book_name in self.__borrowed_list:
            self.__borrowed_list.remove(book_name)
            library_obj.add_book(book_name)
        else:
            print("Book not in borrowed list")
            raise BookNotBorrowed
