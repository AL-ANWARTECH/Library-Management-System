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

    def borrow_book(self, member, book):
        if book.is_available:
            book.is_available = False    
            member.borrowed_books.append(book)
            print(f"{member.name} borrowed '{book.title}' successfully.") 
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, member, book):
        if book in member.borrowed_books:
            book.is_available = True
            member.borrowed_books.remove(book)
            print(f"{member.name} returned '{book.title}' successfully.")
        else:
            print(f"{member.name} did not borrow '{book.title}'.")

    def search_by_title(self, title):

        found = False

        for book in self.books:
            if book.title == title:
                book.display()
                found = True

        if not found:
            print(f"Book '{title}' not found.")

    def search_by_author(self, author):
        found = False

        for book in self.books:
            if book.author == author:
                book.display()
                found = True

        if not found:
            print(f"Book '{author}' not found.")

    def search_by_id(self, book_id):

        found = False

        for book in self.books:
            if book.book_id == book_id:
                book.display()
                found = True

        if not found:
            print(f"Book '{book_id}' not found.")

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

library.borrow_book(member1, book1)

library.display_books()
library.display_members()

library.borrow_book(member2, book1)

library.return_book(member1, book1)

library.return_book(member2, book1)

library.search_by_title("Python Crash Course")
library.search_by_title("Clean Code")

library.search_by_author("Eric Matthes")
library.search_by_author("Robert Martin")

library.search_by_id(1)
library.search_by_id(2)
library.search_by_id(5)