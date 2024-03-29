"""
This file has all unit test for Library Management application
"""
import unittest

from library import Library
from user import User
from custom_exceptions import *
from library_management import LibraryManagement


class TestLibraryManagement(unittest.TestCase):

    def test_view_books_empty(self):
        """Tests Empty library when asked by user"""
        books = []
        library_obj = Library(books)
        books_in_lib = library_obj.view_and_get_books()
        self.assertEqual(len(books_in_lib), 0)

    def test_view_books_not_empty(self):
        """Tests display list of books when Library not empty"""
        books = ["book1", "book2", "book3"]
        library_obj = Library(books)
        books_in_lib = library_obj.view_and_get_books()
        self.assertNotEqual(len(books_in_lib), 0)

    def test_request_book_1(self):
        """Tests requested book is added to user borrowed list"""
        books = ["book1", "book2", "book3", "book4"]
        library_obj = Library(books)
        user = User("Satish Hiremath")
        len_bef_request = len(library_obj.view_and_get_books())
        user.request_book("book2", library_obj)
        b_lst_after_req = library_obj.view_and_get_books()
        self.assertEqual(len(b_lst_after_req), len_bef_request - 1)

    def test_request_max_books_limit(self):
        """Tests maximum limit of books borrowed by user"""
        books = ["book1", "book2", "book3", "book4"]
        library_obj = Library(books)
        user = User("Satish")
        user.request_book("book1", library_obj)
        user.request_book("book2", library_obj)
        self.assertRaises(MaximumBookBorrowLimit, user.request_book, "book3", library_obj)

    def test_request_book_not_present(self):
        """Tests scenario where requested book is not in Library"""
        books = ["book1", "book2", "book3", "book4"]
        library_obj = Library(books)
        user = User("Satish Hiremath")
        self.assertRaises(BookNotPresentInLibrary, user.request_book, "book6", library_obj)

    def test_request_book_more_than_1_copy_in_library(self):
        """Tests scenario where more than one copy of book is present and user requests for it"""
        books = ["book1", "book2", "book2", "book2"]
        library_obj = Library(books)
        user = User("Satish")
        user.request_book("book2", library_obj)
        desired_books_after_request = ["book1", "book2", "book2"]
        self.assertEqual(library_obj.view_and_get_books(), desired_books_after_request)

    def test_request_book_only_1_copy_in_library(self):
        """Tests scenario where only one copy is available in library"""
        books = ["book1", "book2", "book2"]
        library_obj = Library(books)
        user = User("Satish")
        user.request_book("book1", library_obj)
        desired_books_after_request = ["book2", "book2"]
        self.assertEqual(library_obj.view_and_get_books(), desired_books_after_request)

    def test_request_book_only_1_can_be_borrowed(self):
        """Tests scenario where only one copy can be borrowed by user"""
        books = ["book1", "book2", "book2"]
        library_obj = Library(books)
        user = User("Satish")
        user.request_book("book2", library_obj)
        self.assertRaises(BookAlreadyBorrowedByUser, user.request_book, "book2", library_obj)

    def test_return_1_of_2_books(self):
        """Tests scenario where 1 book is returned out of 2 borrowed books"""
        books = ["book1", "book2", "book3", "book4"]
        user = User("Satish")
        library_obj = Library(books)
        user.request_book("book1", library_obj)
        user.request_book("book2", library_obj)
        user.view_borrowed_list()
        user.return_book("book1", library_obj)
        desired_borrow_list = ["book2"]
        library_obj.view_and_get_books()
        self.assertEqual(user.view_borrowed_list(), desired_borrow_list)

    def test_return_all_books(self):
        """Tests scenario where all 2 books are returned from borrowed list"""
        books = ["book1", "book2", "book3", "book4"]
        user = User("Satish")
        library_obj = Library(books)
        user.request_book("book1", library_obj)
        user.request_book("book2", library_obj)
        user.view_borrowed_list()
        user.return_book("book1", library_obj)
        user.return_book("book2", library_obj)
        desired_borrow_list = []
        library_obj.view_and_get_books()
        self.assertEqual(user.view_borrowed_list(), desired_borrow_list)

    def test_create_user(self):
        """Tests create user function"""
        user_name = "Satish"
        library_manag_obj = LibraryManagement("xyz Library")
        user_key_pair = library_manag_obj.create_user(user_name)
        self.assertEqual(list(user_key_pair.keys())[0], user_name)
        self.assertIsInstance(list(user_key_pair.values())[0], User)


if __name__ == "__main__":
    unittest.main()
