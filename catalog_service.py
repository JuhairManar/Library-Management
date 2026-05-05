class CatalogService:
    def __init__(self,library):
        self.library=library

    def booklist(self):
        for key in self.library.book_list:
            book=self.library.book_list[key]

            if book.quantity>0:
                print(book.title,"-",book.quantity)