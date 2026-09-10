from models.book import Book
from models.member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered successfully.")

    def display_books(self):
        for book in self.books:
            book.display()

    def display_members(self):
        for member in self.members:
            member.display_info()

library = Library()

book1 = Book(1, "Python Crash Course", "Eric Matthes")
book2 = Book(2, "Django for beginners", "Mosh")

library.add_book(book1)
library.add_book(book2)

library.display_books()

member1 = Member(1, "Anwar", "anwarsagirmustapha1@gmail.com")
member2 = Member(2, "Hafsat", "hafasatmukthar@gmail.com")

library.register_member(member1)
library.register_member(member2)

library.display_members()