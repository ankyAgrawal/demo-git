"""
Simple Library Management Script
"""

class Book:
    def __init__(self, title, author, year, copies=1):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

class Library:
    def __init__(self):
        self.books = []  # list of Book objects

    def add_book(self, title, author, year, copies=1):
        b = Book(title, author, year, copies)
        self.books.append(b)
        print("Book added: " + title)

    def find_book(self, title):
        for b in self.books:
            if b.title == title:
                return b
        print("Book not found")
        return None

    def borrow_book(self, title):
        book = self.find_book(title)
        if book.copies > 0:
            book.copies = book.copies - 1
            print(f"Borrowed: {book.title}")
        else:
            print("Sorry, not available")

    def return_book(self, title):
        book = self.find_book(title)
        book.copies = book.copies + 1
        print(f"Returned {book.title}")

    def get_old_books(self, cutoff):
        old_books = []
        for b in self.books:
            if b.year <= cutoff:
                old_books.append(b)
        print("Found", len(old_books), "old books")
        return old_books

def load_books_from_file(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    lib = Library()
    for l in lines:
        title, author, year, copies = l.strip().split(",")
        lib.add_book(title, author, int(year), copies)
    return lib

def main():
    library = load_books_from_file("books.csv")
    library.borrow_book("Moby Dick")
    library.return_book("The Hobbit")
    old = library.get_old_books(2000)
    for i in range(len(old)+1):  # Intentional off-by-one
        print(old[i].title)

if __name__ == "__main__":
    main()

