from users import User
from user_repository import UserRepository

class UserManager:
    def __init__(self):
        self.repo=UserRepository()

    def register(self,name,roll,password):
        if self.repo.get_user(roll):
            print("Account already exists")
            return None

        self.repo.add_user(roll,name,password)
        return User(name,roll,password)

    def login(self,roll,password):
        data=self.repo.get_user(roll)

        if data and data["password"]==password:
            return User(data["name"],data["roll"],data["password"])

        return None

    def get_user(self,roll):
        data=self.repo.get_user(roll)

        if data:
            return User(data["name"],data["roll"],data["password"])

        return None