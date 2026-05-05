from users import User
from user_repository import UserRepository
from borrow_repository import BorrowRepository

class UserManager:
    def __init__(self):
        self.repo = UserRepository()
        self.borrow_repo = BorrowRepository()

    def register(self, name, roll, password):
        if self.repo.get_user(roll):
            print("Account already exists")
            return None

        self.repo.add_user(roll, name, password)
        return User(name, roll, password)

    def login(self, roll, password):
        data = self.repo.get_user(roll)

        if data and data["password"] == password:
            user = User(data["name"], data["roll"], data["password"])

            # 🔥 LOAD BOOKS FROM DB (IMPORTANT FIX)
            books = self.borrow_repo.get_user_books(roll)
            returned = self.borrow_repo.get_returned(roll)

            for b in books:
                user.borrow(b["book_title"])

            for b in returned:
                user.returned_books.add(b["book_title"])

            return user

        return None

    def get_user(self, roll):
        data = self.repo.get_user(roll)

        if data:
            return User(data["name"], data["roll"], data["password"])

        return None