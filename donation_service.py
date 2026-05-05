from book import Book

class DonationService:
    def __init__(self,library):
        self.library=library

    def donate(self,book_name,amount):
        book_name=book_name.strip().lower()

        if book_name=="":
            print("Invalid book name")
            return

        if amount<=0:
            print("Donation amount must be positive")
            return

        if book_name in self.library.book_list:
            self.library.book_list[book_name].restock(amount)
        else:
            self.library.book_list[book_name]=Book(book_name.title(),amount)

        print("Thanks for donating")