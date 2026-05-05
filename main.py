from book import Book
from library import Library
from user_manager import UserManager
from borrow_service import BorrowService
from donation_service import DonationService
from catalog_service import CatalogService

class LibrarySystem:
    def __init__(self):
        self.library = Library()

        self.user_manager = UserManager()
        self.borrow_service = BorrowService(self.library, self.user_manager)
        self.donation_service = DonationService(self.library)
        self.catalog_service = CatalogService(self.library)

        self.current_user = None

    def run(self):
        while True:
            if self.current_user is None:
                self.guest_menu()
            else:
                self.user_menu()

    def guest_menu(self):
        print("\nLogin / Create Account (L/C)")
        option = input().upper()

        if option == "L":
            roll = int(input("Roll: "))
            password = input("Password: ")

            user = self.user_manager.login(roll, password)

            if user:
                self.current_user = user
            else:
                print("Invalid credentials")

        elif option == "C":
            name = input("Name: ")
            roll = int(input("Roll: "))
            password = input("Password: ")

            user = self.user_manager.register(name, roll, password)

            if user:
                self.current_user = user

    def user_menu(self):
        print("\n--- MENU ---")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. My Borrowed Books")
        print("4. Returned Books")
        print("5. View Book List")
        print("6. Donate Book")
        print("7. Logout")
        print("------------")

        x = int(input("Choose: "))

        if x == 1:
            b = input("Book: ")
            self.borrow_service.borrow_book(b, self.current_user)

        elif x == 2:
            b = input("Book: ")
            self.borrow_service.return_book(b, self.current_user)

        elif x == 3:
            print("\nBorrowed:", self.current_user.borrow_books)

        elif x == 4:
            if self.current_user.returned_books:
                print("\nReturned:", self.current_user.returned_books)
            else: 
                print("[]")

        elif x == 5:
            self.catalog_service.booklist()

        elif x == 6:
            b = input("Book: ")
            a = int(input("Amount: "))
            self.donation_service.donate(b, a)

        elif x == 7:
            self.current_user = None

app = LibrarySystem()
app.run()