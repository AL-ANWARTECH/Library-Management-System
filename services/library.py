from models.book import Book
from models.member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                print("Do not add the book")
                return
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def register_member(self, member):
        for existing_member in self.members:
            if existing_member.member_id == member.member_id:
                print("Do not add member.")
                return
            
        self.members.append(member)
        print(f"Member '{member.name}' registered successfully.")

    def display_books(self):
        for book in self.books:
            book.display()

    def display_members(self):
        for member in self.members:
            member.display_info()

    def borrow_book(self, member, book):

        if member not in self.members:
            print("Member is not registered.")
            return
        if book not in self.books:
            print("Book is not registered in the library.")
            return
        
        if book.is_available:
            book.is_available = False    
            member.borrowed_books.append(book)
            print(f"{member.name} borrowed '{book.title}' successfully.") 
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, member, book):

        if member not in self.members:
            print("Member is not registered.")
            return
        
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

