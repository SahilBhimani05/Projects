class Book:
    def __init__(self, title, author, count):
        self.title = title.title()
        self.author = author.title()
        self.count = count
        self.isAvailable = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} by {book.author} added to the library")

    def display_books(self):
        for book in self.books:
            availability = 'Available' if book.isAvailable else 'Unavailable'
            print(f"{book.author}'s {book.title} book is {availability}")

    def search_book(self, title):
        found = False
        for book in self.books:
            if book.title == title.title():
                print(f"{book.author}'s {book.title} book found")
                found = True
                break
        if not found:
            print("Book not found")

class Person():
    def __init__(self):
        self.member = []
        self.i_book = {}

    def add_member(self,member):
        self.member.append(member)
        print(f"{member} added")

    def borrow_book(self, member, book_title):
        if member not in self.member:
            print(f"Member {member} is not added")
        else:
            found = False
            for book in library.books:
                if book.title == book_title.title():
                    found = True
                    self.i_book[member] = book
                    book.count -= 1
                    book.isAvailable = False
                    print(f"{book.author}'s {book.title} book issued to {member}")
                    break
            if not found:
                print(f"Book {book_title} not found or not available")

    def return_book(self, member, book_title):
        if member in self.member:
            for book in library.books:
                if book.title == book_title.title():
                    self.i_book.pop(member)
                    book.count += 1
                    book.isAvailable = True
                    print(f"{book.author}'s {book.title} book returned by {member}")
                    break
        else:
            print(f"Member {member} is not found")

    def ledger_view(self):
        print(f"\n{'Member':<15}{'Book Title':<30}{'Author':<30}{'Availability':<15}{'No. of Books':<15}")
        print('-' * 115)
        for member, book in self.i_book.items():
            availability = 'Available' if book.count > 0 else 'Unavailable'
            print(f"{member.title():<15}{book.title:<30}{book.author:<30}{availability:<15}{book.count:<15}")
            
        for book in library.books:
            if book not in self.i_book.values():
                availability = 'Available' if book.count > 0 else 'Unavailable'
                print(f"{'No Member':<15}{book.title:<30}{book.author:<30}{availability:<15}{book.count:<15}")
        print()

library = Library()
person = Person()

while True:
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Add Member")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Ledger View")
    print("0. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        title = input("Enter name of the book: ")
        author = input("Enter author of the book: ")
        count = int(input("Enter no. of books: "))
        book = Book(title, author, count)
        library.add_book(book)
    elif ch == 2:
        library.display_books()
    elif ch == 3:
        title = input("Enter name of the book to search: ")
        library.search_book(title)
    elif ch == 4:
       member = input("Enter member name to add: ")
       person.add_member(member)
    elif ch == 5:
        member = input("Enter member: ")
        book_title = input("Enter book: ")
        person.borrow_book(member, book_title)
    elif ch == 6:
        member = input("Enter member: ")
        book_title = input("Enter book: ")
        person.return_book(member, book_title)
    elif ch == 7:
        person.ledger_view()
    elif ch == 0:
        break
    else:
        print("Invalid choice!")