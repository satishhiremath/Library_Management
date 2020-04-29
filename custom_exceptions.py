"""
This file has all custom exceptions implementations
"""


class MaximumBookBorrowLimit(Exception):
    """Raised when more than 2 books are requested for a user"""
    pass


class BookNotPresentInLibrary(Exception):
    """Raised when there are no books in library"""
    pass


class BookAlreadyBorrowedByUser(Exception):
    """Raised when book is already borrowed by User"""
    pass
