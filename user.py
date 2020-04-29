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
        if len(self.__borrowed_list) < 2\
                and book_name not in self.__borrowed_list:
            lend_status = library_obj.lend_book(book_name)
            if lend_status:
                self.__borrowed_list.append(book_name)
                print("Book: {} is borrowed by user: {}".format(book_name, self.__name))
            else:
                raise BookNotPresentInLibrary
        elif book_name in self.__borrowed_list:
            raise BookAlreadyBorrowedByUser
        elif len(self.__borrowed_list) >= 2:
            raise MaximumBookBorrowLimit

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
            raise BookNotBorrowed
