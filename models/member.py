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


member1 = Member(1, "Anwar", "anwarsagirmustapha1@gmail.com")
member2 = Member(2, "Hafsat", "hafsatmukthar@gmail.com")

member1.display_info()
member2.display_info()