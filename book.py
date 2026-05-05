class Book:
    def __init__(self, title, quantity):
        self.title = title
        self.quantity = quantity

    def is_available(self):
        return self.quantity > 0

    def issue(self):
        if self.quantity > 0:
            self.quantity -= 1

    def restock(self, amount=1):
        self.quantity += amount