class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def display_info(self):
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print("Borrowed Books:")
        for book in self.borrowed_books:
            print(f"- {book.title}")
