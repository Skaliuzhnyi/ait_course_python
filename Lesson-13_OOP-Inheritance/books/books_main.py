# Create several instances of books and print their details

from book import Book
from fiction_book import FictionBook
from kids_fiction_book import KidsFictionBook

book = Book('Djk', 'Kkklfk', 205, 2.44)
print("Book 1\n", book, ',', "Book price: ", book.book_price_calculation())

print('-' * 100)

book_2 = Book('Hjkdk Hjkds', 'Fkklsdj', 790, 0.44)
print(f"Book 2\n{book_2}, Book price: {book_2.book_price_calculation()}")

print('-' * 100)

fiction_book = FictionBook('Ldfs', 'Ooofd', 300, 5.44, 'Fantastic')
print(f"Fiction Book\n{fiction_book}, Book price: {fiction_book.book_price_calculation()}")

print('-' * 100)

kids_fiction_book = KidsFictionBook('Hjkdk', 'Fkklsdj', 790, 0.44, 'Comix', 9)
print(
    f"Kids Fiction Book\n{kids_fiction_book}, Book price + 20% discount for kids = {kids_fiction_book.book_price_calculation()}")

print('-' * 100)
