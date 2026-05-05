from .book import Book
from .library import Library
from .user_manager import UserManager
from .borrow_service import BorrowService
from .donation_service import DonationService
from .catalog_service import CatalogService

class LibrarySystem:
    def __init__(self):
        self.library=Library({
            "english":Book("English",2),
            "bangla":Book("Bangla",5),
            "math":Book("Math",3)
        })

        self.user_manager=UserManager()
        self.borrow_service=BorrowService(self.library,self.user_manager)
        self.donation_service=DonationService(self.library)
        self.catalog_service=CatalogService(self.library)

        self.current_user=None

    def run(self):
        while True:

            if self.current_user is None:
                self.guest_menu()
            else:
                self.user_menu()

    def guest_menu(self):
        print("Not logged in")
        print("Please Login or Create Account(L/C)")
        option=input().upper()

        if option=="L":
            roll=int(input("Roll: "))
            password=input("Password: ")

            user=self.user_manager.login(roll,password)

            if user:
                self.current_user=user
            else:
                print("Invalid roll or password")

        elif option=="C":
            name=input("Name: ")
            roll=int(input("Roll: "))
            password=input("Password: ")

            user=self.user_manager.register(name,roll,password)

            if user:
                self.current_user=user

        else:
            print("Invalid option")

    def user_menu(self):
        print("OPTIONS")
        print("1.Borrow a book")
        print("2.Return a book")
        print("3.Borrowed books list")
        print("4.Returned books list")
        print("5.Check book list")
        print("6.Donate")
        print("7.Logout")

        x=int(input("Choose option: "))

        if x==1:
            book_name=input("Book name: ")
            self.borrow_service.borrow_book(book_name,self.current_user)

        elif x==2:
            book_name=input("Book name: ")
            self.borrow_service.return_book(book_name,self.current_user)

        elif x==3:
            print(self.current_user.borrow_books)

        elif x==4:
            print(self.current_user.returned_books)

        elif x==5:
            self.catalog_service.booklist()

        elif x==6:
            book_name=input("Book name: ")
            amount=int(input("Amount: "))
            self.donation_service.donate(book_name,amount)

        elif x==7:
            self.current_user=None

        else:
            print("Invalid option")

app=LibrarySystem()
app.run()
                 

         



