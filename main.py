from models.book import Book
from models.member import Member
from  services.library import Library

library = Library()

book1 = Book(1, "Python crash course", "Eric Matthes")

library.add_book(book1)

member1 = Member(1, "Anwar", "anwarsagirmustapha1@gmail.com")
library.register_member(member1)

