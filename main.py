from models.book import Book
from models.member import Member
from services.library import Library

def main():
    library = Library()


    # =========================
    # ADD BOOKS
    # =========================

    book1 = Book(1, "Python Crash Course", "Eric Matthes")
    book2 = Book(2, "Django for Beginners", "Mosh")

    library.add_book(book1)
    library.add_book(book2)

    library.display_books()


    # =========================
    # REGISTER MEMBERS
    # =========================

    member1 = Member(1, "Anwar", "anwarsagirmustapha1@gmail.com")
    member2 = Member(2, "Hafsat", "hafsatmukthar@gmail.com")

    library.register_member(member1)
    library.register_member(member2)


    # =========================
    # BORROW BOOK
    # =========================

    library.borrow_book(member1, book1)

    library.display_books()
    library.display_members()


    # =========================
    # TEST BORROWING UNAVAILABLE BOOK
    # =========================

    library.borrow_book(member2, book1)


    # =========================
    # RETURN BOOK
    # =========================

    library.return_book(member1, book1)

    library.return_book(member2, book1)


    # =========================
    # SEARCH BY TITLE
    # =========================

    library.search_by_title("Python")
    library.search_by_title("PYTHON CRASH COURSE")
    library.search_by_title("Clean Code")


    # =========================
    # SEARCH BY AUTHOR
    # =========================
    library.search_by_author("Eric")
    library.search_by_author("eric matthes")
    library.search_by_author("ERIC MATTHES")
    library.search_by_author("Robert Martin")


    # =========================
    # SEARCH BY ID
    # =========================
    try: 
       book_id = int(input("Enter book ID to search: "))
       library.search_by_id(book_id)
    except ValueError:
        print("Invalid book ID. Please enter a number.")
    library.search_by_id(2)
    library.search_by_id(5)


    # =========================
    # TEST DUPLICATE BOOK
    # =========================

    book3 = Book(1, "Clean Code", "Robert Martin")
    library.add_book(book3)


    # =========================
    # TEST DUPLICATE MEMBER
    # =========================

    member3 = Member(1, "Abdullahi", "abdullahiyakubabo@gmail.com")
    library.register_member(member3)


    # =========================
    # TEST UNREGISTERED BOOK
    # =========================

    book4 = Book(4, "Clean Architecture", "Robert Martin")
    library.borrow_book(member1, book4)


    # =========================
    # TEST UNREGISTERED MEMBER
    # =========================

    member4 = Member(4, "Ali", "ali@gmail.com")
    library.return_book(member4, book1)

if __name__ == "__main__":
    main()