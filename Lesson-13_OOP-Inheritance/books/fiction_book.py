# class FictionBook: inheriting from Book, inherits title, author, pages,
# price_per_page and methods. Add field genre

from book import Book

class FictionBook(Book):
    def __init__(self, title, author, pages, price_per_page, genre):
        super().__init__(title, author, pages, price_per_page)
        self.genre = genre

    def __str__(self):
        return f"{super().__str__()}, Genre: {self.genre}"
