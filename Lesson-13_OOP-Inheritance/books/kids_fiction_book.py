# class KidsFictionBook: inheriting from FictionBook.
# Inherits title, author, pages, price_per_page, genre and methods. Add field age

from dis import disco

from fiction_book import FictionBook

class KidsFictionBook(FictionBook):
    def __init__(self, title, author, pages, price_per_page, genre, age):
        super().__init__(title, author, pages, price_per_page, genre)
        self.age = age
        
    def __str__(self):
        return f"{super().__str__()}, Age: {self.age}"
      
    def book_price_calculation(self):
        base_price = self.pages * self.price_per_page
        discount_price = round(base_price * 0.75, 2)
        return discount_price
