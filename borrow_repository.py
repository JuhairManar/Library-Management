from db import DB

class BorrowRepository:
    def __init__(self):
        self.db=DB()

    def borrow(self,roll,book):
        self.db.execute(
            "INSERT INTO borrow(roll,book_title) VALUES(%s,%s)",
            (roll,book)
        )

    def return_book(self,roll,book):
        self.db.execute(
            "DELETE FROM borrow WHERE roll=%s AND book_title=%s LIMIT 1",
            (roll,book)
        )

        self.db.execute(
            "INSERT INTO returned(roll,book_title) VALUES(%s,%s)",
            (roll,book)
        )

    def get_user_books(self,roll):
        return self.db.fetchall(
            "SELECT book_title FROM borrow WHERE roll=%s",
            (roll,)
        )

    def get_returned(self,roll):
        return self.db.fetchall(
            "SELECT book_title FROM returned WHERE roll=%s",
            (roll,)
        )