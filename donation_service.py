from book import Book

class DonationService:
    def __init__(self, library):
        self.library = library

    def donate(self, book_name, amount):
        book_name = book_name.strip().lower()

        if not book_name:
            print("Invalid book name")
            return

        if amount <= 0:
            print("Donation must be positive")
            return

        book = self.library.get_book(book_name)

        if book:
            book.restock(amount)
        else:
            self.library.add_book(book_name, Book(book_name.title(), amount))

        print("Thanks for donating")