class CatalogService:
    def __init__(self, library):
        self.library = library

    def booklist(self):
        print("\nAvailable Books:")
        print("----------------")

        books = self.library.all_books()

        for name, book in books.items():
            if book.quantity > 0:
                print(f"{book.title} - {book.quantity}")

        print("----------------\n")