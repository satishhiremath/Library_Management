"""
This class has implementation for Library Management functions
"""
import sys

from library import Library
from user import User
from custom_exceptions import *


class LibraryManagement(object):
    def __init__(self, name):
        self.__library_name = name
        self.__user_dict = {}
        self.__library_obj = Library(["book1", "book2", "book3"])

    def display_library_menu(self):
        """Displays library menu"""
        print("------------LIBRARY MENU -------------")
        print("1. Display all books available")
        print("2. Create new user")
        print("3. Request book/lend book")
        print("4. Return book")
        print("5. Display borrowed books")
        print("6. Exit")

    def create_user(self, user_name):
        """Creates new user and returns user and Object key-val pair"""
        print("User: {} created!".format(user_name))
        return {user_name: User(user_name)}

    def main(self):
        """Main function for library management"""

        while True:
            self.display_library_menu()
            choice = int(input("Enter choice: "))
            if choice == 1:
                self.__library_obj.view_and_get_books()
            elif choice == 2:
                user_name = input("Enter user name: ")
                if user_name not in self.__user_dict.keys():
                    self.__user_dict.update(self.create_user(user_name))
            elif choice == 3:
                user_name = input("Enter user name: ")
                book_name = input("Enter book to request: ")
                try:
                    self.__user_dict[user_name].request_book(book_name, self.__library_obj)
                except KeyError:
                    print("Invalid User name, Please enter valid username")
                except MaximumBookBorrowLimit:
                    print("Maximum borrow limit reached for User: {}".format(user_name))
                except BookAlreadyBorrowedByUser:
                    print("Book: {} already borrowed by User: {}".format(book_name, user_name))
                except BookNotPresentInLibrary:
                    print("Requested book is not present in Library")

            elif choice == 4:
                user_name = input("Enter user name: ")
                book_name = input("Enter book to return: ")
                try:
                    self.__user_dict[user_name].return_book(book_name, self.__library_obj)
                except KeyError:
                    print("Invalid User name, Please enter valid username")
                except BookNotBorrowed:
                    print("Book: {} not in borrowed list of user: {}".format(book_name, user_name))
            elif choice == 5:
                user_name = input("Enter user name: ")
                try:
                    self.__user_dict[user_name].view_borrowed_list()
                except KeyError:
                    print("Invalid User name, Please enter valid username")
            elif choice == 6:
                sys.exit()


if __name__ == "__main__":
    library_management = LibraryManagement("Developer's Library")
    library_management.main()
