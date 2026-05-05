from borrow_repository import BorrowRepository

class BorrowService:
    def __init__(self,library,user_manager):
        self.library=library
        self.user_manager=user_manager
        self.repo=BorrowRepository()

    def borrow_book(self, book_name, user):
        book_name = book_name.strip().lower()

        book = self.library.get_book(book_name)

        if not book:
            print("Book not found")
            return

        if not book.is_available():
            print("Unavailable")
            return

        # 1. DB FIRST
        self.repo.borrow(user.roll, book_name)

        # 2. THEN memory update
        book.issue()
        self.library.save_book(book)

        # 3. user update
        user.borrow(book_name)

        print("Borrow done")

    def return_book(self, book_name, user):
        book_name = book_name.strip().lower()

        book = self.library.get_book(book_name)

        if not book:
            return

        self.repo.return_book(user.roll, book_name)

        user.return_book(book_name)

        book.restock()
        self.library.save_book(book)

        print("Returned")