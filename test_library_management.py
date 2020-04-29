"""
This file has all unit test for Library Management application
"""
import unittest

from library import Library


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


if __name__ == "__main__":
    unittest.main()
