class User:
    def __init__(self,name,roll,password):
        self.name=name
        self.roll=roll
        self.password=password
        self.borrow_books=set()
        self.returned_books=set()

    def borrow(self,book_name):
        self.borrow_books.add(book_name)

    def return_book(self,book_name):
        self.borrow_books.remove(book_name)
        self.returned_books.add(book_name)