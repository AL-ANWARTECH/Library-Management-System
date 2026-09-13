from models.book import Book
from models.member import Member
from services.library import Library


def find_member(library, member_id):
    for member in library.members:
        if member.member_id == member_id:
            return member
    return None


def find_book(library, book_id):
    for book in library.books:
        if book.book_id == book_id:
            return book
    return None


def search_books(library):
    print("\n--- SEARCH BOOK ---")
    print("1. Search by Title")
    print("2. Search by Author")
    print("3. Search by ID")

    search_choice = input("Enter your choice: ")

    if search_choice == "1":
        title = input("Enter book title: ")
        library.search_by_title(title)

    elif search_choice == "2":
        author = input("Enter book author: ")
        library.search_by_author(author)

    elif search_choice == "3":
        try:
            book_id = int(input("Enter book ID: "))
            library.search_by_id(book_id)
        except ValueError:
            print("Invalid book ID. Please enter a number.")

    else:
        print("Invalid search option.")


def search_members(library):
    print("\n--- SEARCH MEMBER ---")
    print("1. Search by ID")
    print("2. Search by Name")

    search_choice = input("Enter your choice: ")

    if search_choice == "1":
        try:
            member_id = int(input("Enter member ID: "))
            library.search_member_by_id(member_id)
        except ValueError:
            print("Invalid member ID. Please enter a number.")

    elif search_choice == "2":
        name = input("Enter member name: ")
        library.search_member_by_name(name)

    else:
        print("Invalid search option.")


def add_book(library):
    try:
        book_id = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        author = input("Enter book author: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    except ValueError:
        print("Invalid book ID. Please enter a number.")


def register_member(library):
    try:
        member_id = int(input("Enter member ID: "))
    except ValueError:
        print("Invalid member ID. Please enter a number.")
        return

    name = input("Enter member name: ")
    email = input("Enter member email: ")

    try:
        member = Member(member_id, name, email)
        library.register_member(member)

    except ValueError as error:
        print(f"Error: {error}")


def borrow_book(library):
    try:
        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))
    except ValueError:
        print("Invalid ID. Please enter numbers only.")
        return

    selected_member = find_member(library, member_id)
    selected_book = find_book(library, book_id)

    if selected_member is None:
        print("Member not found.")
    elif selected_book is None:
        print("Book not found.")
    else:
        library.borrow_book(selected_member, selected_book)


def return_book(library):
    try:
        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))
    except ValueError:
        print("Invalid ID. Please enter numbers only.")
        return

    selected_member = find_member(library, member_id)
    selected_book = find_book(library, book_id)

    if selected_member is None:
        print("Member not found.")
    elif selected_book is None:
        print("Book not found.")
    else:
        library.return_book(selected_member, selected_book)


def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Display Books")
        print("4. Display Members")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Search Book")
        print("8. Search Member")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)

        elif choice == "2":
            register_member(library)

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            library.display_members()

        elif choice == "5":
            borrow_book(library)

        elif choice == "6":
            return_book(library)

        elif choice == "7":
            search_books(library)

        elif choice == "8":
            search_members(library)

        elif choice == "9":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()