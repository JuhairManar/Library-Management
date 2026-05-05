from collections import deque
from book import Book

class BorrowService:
    def __init__(self, library, user_manager):
        self.library = library
        self.user_manager = user_manager
        self.waiting = {}

    def borrow_book(self, book_name, user):
        book_name = book_name.strip().lower()

        book = self.library.get_book(book_name)
        if not book:
            print("This Book is not available")
            return

        if book_name in user.borrow_books:
            print("You already borrowed it")
            return

        if not book.is_available():
            if book_name not in self.waiting:
                self.waiting[book_name] = deque()

            if user.roll not in self.waiting[book_name]:
                self.waiting[book_name].append(user.roll)

            print("Book unavailable. Added to waiting list.")
            return

        book.issue()
        user.borrow(book_name)
        print("Borrow done")

    def return_book(self, book_name, user):
        book_name = book_name.strip().lower()

        book = self.library.get_book(book_name)
        if not book:
            print("This book doesn't belong to this library")
            return

        if book_name not in user.borrow_books:
            print("You didn't borrow this book")
            return

        user.return_book(book_name)

        if book_name in self.waiting and self.waiting[book_name]:
            next_roll = self.waiting[book_name].popleft()
            next_user = self.user_manager.get_user(next_roll)

            if next_user:
                next_user.borrow(book_name)
                print("Returned & assigned to waiting user")
                return

        book.restock()
        print("Book returned successfully")