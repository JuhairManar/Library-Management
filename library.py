class Library:
    def __init__(self, book_list):
        self._books = book_list

    def get_book(self, name):
        return self._books.get(name)

    def add_book(self, name, book):
        self._books[name] = book

    def all_books(self):
        return self._books