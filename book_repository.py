from db import DB

class BookRepository:
    def __init__(self):
        self.db=DB()

    def get_books(self):
        return self.db.fetchall("SELECT * FROM books")

    def get_book(self,title):
        return self.db.fetchone(
            "SELECT * FROM books WHERE title=%s",
            (title,)
        )

    def update_qty(self,title,qty):
        self.db.execute(
            "UPDATE books SET quantity=%s WHERE title=%s",
            (qty,title)
        )

    def add_book(self,title,qty):
        self.db.execute(
            "INSERT INTO books(title,quantity) VALUES(%s,%s)",
            (title,qty)
        )