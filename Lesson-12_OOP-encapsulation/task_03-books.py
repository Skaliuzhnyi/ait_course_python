class Book:
    def __init__(self, isbn, title, author, pages):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return (f"Isbn: \033[32m{self.isbn}\033[0m, Title: \033[32m{self.title}\033[0m, Author: \033[32m{self.author}\033[0m, Price: \033[32m{self.pages}\033[0m")

book_1 = Book('0123456789', 'Python for Beginers', 'S. Kaliuzhnyi', '405')
book_2 = Book('0145678333', 'War and Peace', 'L. Tolstoy', '2006')
book_3 = Book('9087654321', 'The Hobbit', 'J. R. R. Tolkien', '206')

print(book_1)
print(book_2)
print(book_3)

print('-' * 100)

library = [book_1, book_2, book_3]

for book in library:
    print(book)

print('-' * 100)

library_dictionary = {
    book_1: 15,
    book_2: 7,
    book_3: 12
}

for book in library_dictionary:
    print(book)
print(library_dictionary)

print('-' * 100)

for key in library_dictionary.keys():
    print(f'{key.title}, quantity = {library_dictionary.get(key)}')