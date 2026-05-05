class CatalogService:
    def __init__(self,library):
        self.library=library

    def booklist(self):
        books=self.library.all_books()

        print()

        for k in books:
            b=books[k]
            print(b.title,"-",b.quantity)

        print()