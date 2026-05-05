from collections import deque

class User:
    def __init__(self,name,roll,password):
        self.name=name
        self.roll=roll
        self.password=password
        self.borrow_books=set()
        self.returned_books=set()
        
class Book:
    def __init__(self, title, quantity):
        self.title=title
        self.quantity=quantity

class Library:
    def __init__(self, book_list):
        self.book_list = book_list
        self.waiting = {}

    def borrow_book(self, bookName, user):
        bookName = bookName.strip().lower()

        if bookName not in self.book_list:
            print("This Book is not available")
            return

        if bookName in user.borrow_books:
            print("You already borrowed it")
            return

        book = self.book_list[bookName]

        if book.quantity == 0:

            if bookName not in self.waiting:
                self.waiting[bookName] = deque()

            if user.roll not in self.waiting[bookName]:
                self.waiting[bookName].append(user.roll)

            print("Book unavailable. Added to waiting list.")
            return

        book.quantity -= 1
        user.borrow_books.add(bookName)
        
        print("Borrow done")

    def return_book(self, bookName, user):
        bookName = bookName.strip().lower()

        if bookName not in self.book_list:
            print("This book doesn't belong to this library")
            return

        if bookName not in user.borrow_books:
            print("You didn't borrow this book")
            return

        user.borrow_books.remove(bookName)
        user.returned_books.add(bookName)

        if bookName in self.waiting and len(self.waiting[bookName]) > 0:

            next_roll = self.waiting[bookName].popleft()
            next_user = users[next_roll]
            next_user.borrow_books.add(bookName)

            print("Returned successfully")

        else:
            self.book_list[bookName].quantity += 1
            print("Book returned successfully")

    def donate(self, bookname, amount):
        bookname=bookname.strip().lower()

        if bookname=="":
            print("Invalid book name")
            return

        if amount <= 0:
            print("Donation amount must be positive")
            return

        if bookname in self.book_list:
            self.book_list[bookname].quantity+=amount
        else:
            self.book_list[bookname] = Book(bookname.title(), amount)

        print("Thanks for donating")

    def booklist(self):
        for key in self.book_list:
            book = self.book_list[key]

            if book.quantity > 0:
                print(book.title, "-", book.quantity) 

                    


lb=Library({
    "english": Book("English", 2),
    "bangla": Book("Bangla", 5),
    "math": Book("Math", 3)
})
users={}
current_user=None

while True:
    if current_user==None:
        print("Not logged in\nPlease Login or create account(L/C)")
        option=input()
        
        if option=='L':
            roll=int(input("Roll: "))
            password=input("Password: ")
            match=False
            if roll in users and users[roll].password==password:
                current_user=users[roll]
                match=True
            else:
                print("Invalid roll or password")     

        elif option=='C':           
            name=input("Name: ")
            roll=int(input("Roll: "))
            password=input("Passwod: ")
            found=False
            #loop to check creating account with same roll or not
            if roll in users:
                print("Account already created")
                continue     
            user=User(name,roll,password)
            current_user=user
            users[roll]=user
            """ print("End of user")
            break """
        
        else:
            print("Invalid option")

    else:
        print("OPTIONS",end='')
        print("__________")
        print("1.Borrow a book")
        print("2.Return a book")
        print("3.Borrowed books list")
        print("4.Returned books list")
        print("5.Check book list")
        print("6.Donate")
        print("7.Logout")
        x=int(input("Choose a option\n"))
        if x==1:
            bookName=input("Book name: ")
            lb.borrow_book(bookName,current_user)
        elif x==2:    
            bookName=input("Book name: ")
            lb.return_book(bookName,current_user)
        elif x==3:
            print(current_user.borrow_books)
        elif x==4:
            print(current_user.returned_books)   
        elif x==5:
              #print(lb.book_list) 
              lb.booklist()
        elif x==6:
            bookName=input("Book name: ")
            """ if bookName in lb.book_list:
                lb.book_list[bookName]+=1
              else:
                lb.book_list[bookName]=1 """
            amount=int(input("amount: "))
            lb.donate(bookName,amount)     
        elif x==7:
            current_user=None    
        else:
            print("invalid option")  
                 
        """ lb.borrow_book("English",current_user)
        print(lb.book_list)
        print(current_user.borrow_books)
        lb.borrow_book("English",current_user)
        lb.return_book("Science",current_user) """
        #break


         



