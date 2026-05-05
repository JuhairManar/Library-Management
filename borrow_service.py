from collections import deque

class BorrowService:
    def __init__(self,library,user_manager):
        self.library=library
        self.user_manager=user_manager
        self.waiting={}

    def borrow_book(self,book_name,user):
        book_name=book_name.strip().lower()

        if book_name not in self.library.book_list:
            print("This Book is not available")
            return

        if book_name in user.borrow_books:
            print("You already borrowed it")
            return

        book=self.library.book_list[book_name]

        if not book.is_available():

            if book_name not in self.waiting:
                self.waiting[book_name]=deque()

            if user.roll not in self.waiting[book_name]:
                self.waiting[book_name].append(user.roll)

            print("Book unavailable. Added to waiting list.")
            return

        book.issue()
        user.borrow(book_name)

        print("Borrow done")

    def return_book(self,book_name,user):
        book_name=book_name.strip().lower()

        if book_name not in self.library.book_list:
            print("This book doesn't belong to this library")
            return

        if book_name not in user.borrow_books:
            print("You didn't borrow this book")
            return

        user.return_book(book_name)

        if book_name in self.waiting and len(self.waiting[book_name])>0:

            next_roll=self.waiting[book_name].popleft()
            next_user=self.user_manager.get_user(next_roll)

            if next_user:
                next_user.borrow(book_name)
                print("Returned successfully")
                return

        self.library.book_list[book_name].restock()
        print("Book returned successfully")