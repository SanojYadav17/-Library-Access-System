class Member:
    def __init__(self, name, membership_id):
   
       self.name = name
       self.membership_id = membership_id
    def get_member_info(self):
       return f"Name: {self.name},Membership ID: {self.membership_id}"
              
class StudentMember(Member):
    def __init__(self, name, membership_id):
        super().__init__(name, membership_id)
        self.borrowed_books = []
    def add_book(self, book_title):
        self.borrowed_books.append(book_title)
        print(f'"{book_title}" has been checked out.')
    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)
            print(f'"{book_title}" has been returned.')
        else:
            print("ERROR!")
    def display_borrowing_status(self):
        print(f"{self.name} has borrowed {len(self.borrowed_books)} book(s):")
        for book in self.borrowed_books:
            print(f" - {book}")
            
student = StudentMember("Sanoj","1230440046")
print(student.get_member_info())

student.add_book("DSUC by Dr. Praveen Kumar Sukla")
student.add_book("DBMS by Ritesh Kumar")

student.display_borrowing_status()

student.return_book("DSUC by Dr. Praveen Kumar Sukla")
student.display_borrowing_status()
