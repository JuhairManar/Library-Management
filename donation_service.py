from book import Book

class DonationService:
    def __init__(self,library):
        self.library=library

    def donate(self,name,amount):
        book=self.library.get_book(name)

        if book:
            book.restock(amount)
            self.library.save_book(book)
        else:
            self.library.add_book(name,Book(name,amount))

        print("Thanks for donating")