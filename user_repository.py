from db import DB

class UserRepository:
    def __init__(self):
        self.db=DB()

    def add_user(self,roll,name,password):
        self.db.execute(
            "INSERT INTO users(roll,name,password) VALUES(%s,%s,%s)",
            (roll,name,password)
        )

    def get_user(self,roll):
        return self.db.fetchone(
            "SELECT * FROM users WHERE roll=%s",
            (roll,)
        )