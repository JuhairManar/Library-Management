from book_repository import BookRepository
from book import Book

class Library:
    def __init__(self):
        self.repo=BookRepository()

    def get_book(self,name):
        data=self.repo.get_book(name)

        if data:
            return Book(data["title"],data["quantity"])

        return None

    def save_book(self,book):
        self.repo.update_qty(book.title,book.quantity)

    def add_book(self,name,book):
        self.repo.add_book(book.title,book.quantity)

    def all_books(self):
        rows=self.repo.get_books()

        books={}

        for row in rows:
            books[row["title"]]=Book(row["title"],row["quantity"])

        return books