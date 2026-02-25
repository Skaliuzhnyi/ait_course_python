# class Book: title, author, pages, price_per_page.
# Create a method for book price calculation

class Book:
    def __init__(self, title, author, pages, price_per_page):
        self.title = title
        self.author = author
        self.pages = pages
        self.price_per_page = price_per_page

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Price per page: {self.price_per_page}"

    def book_price_calculation(self):
        return round(self.pages * self.price_per_page, 2)
