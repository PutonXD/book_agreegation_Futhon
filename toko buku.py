class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class Bookstore:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print(f"Daftar buku di {self.name}:")
        for book in self.books:
            print(f"Judul: {book.title}")
            print(f"Penulis: {book.author}")
            print(f"Harga: {book.price}")
            print()


# Membuat objek Bookstore
bookstore = Bookstore("Toko Buku ABC")

# Membuat objek Book dan menambahkannya ke Bookstore
book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 10.99)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 8.99)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 7.99)

bookstore.add_book(book1)
bookstore.add_book(book2)
bookstore.add_book(book3)

# Menampilkan daftar buku yang tersedia di toko
bookstore.display_books()
