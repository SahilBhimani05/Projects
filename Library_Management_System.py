from datetime import datetime
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

    def remove_book(self, title):
        found = False
        for book in self.books:
            if book.title == title.title():
                self.books.remove(book)
                print(f"{book.title} by {book.author} removed from the library")
                found = True
                break
        if not found:
            print(f"Book '{title}' not found in the library")

    def display_books(self):
        print(f"\n{'Book Title':<30}{'Author':<30}{'Availability':<30}{'No. of copies':<30}")
        for book in self.books:
            availability = 'Available' if book.count > 0 else 'Unavailable'
            print(f"{book.title:<30}{book.author:<30}{availability:30}{book.count:<30}")

    def search_book(self, title):
        found = False
        for book in self.books:
            if book.title == title.title():
                availability = 'Available' if book.count > 0 else 'Unavailable'
                print(f"{book.title:<30}{book.author:<30}{availability:<30}{book.count:<30}")
                found = True
                break
        if not found:
            print("Book not found")

class Person:
    def __init__(self):
        self.member = []
        self.i_book = {}
        self.transaction = []

    def add_member(self, member):
        self.member.append(member)
        print(f"{member} added")

    def remove_member(self, member):
        self.member.remove(member)
        print(f"{member} removed")

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
                    issue_date = datetime.now().strftime("%B %d, %Y")
                    self.transaction.append((member.title(), book.title, book.author, "Issued", issue_date, "-"))
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
                    return_date = datetime.now().strftime("%B %d, %Y")
                    self.transaction.append((member.title(), book.title, book.author, "Returned", "-", return_date))
                    break
        else:
            print(f"Member {member} is not found")

    def ledger_view(self):
        print(f"\n{'Member':<15}{'Book Title':<30}{'Author':<30}{'Transaction':<15}{'Issue Date':<20}{'Return Date':<20}")
        print('-' * 130)
        for transaction in self.transaction:
            member, title, author, action, issue_date, return_date = transaction
            print(f"{member:<15}{title:<30}{author:<30}{action:<15}{issue_date:<20}{return_date:<20}")
        print()

library = Library()
person = Person()

while True:
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Display Books")
    print("4. Search Book")
    print("5. Add Member")
    print("6. Remove Member")
    print("7. Borrow Book")
    print("8. Return Book")
    print("9. Ledger View")
    print("0. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        title = input("Enter name of the book: ")
        author = input("Enter author of the book: ")
        count = int(input("Enter no. of books: "))
        book = Book(title, author, count)
        library.add_book(book)
    elif ch == 2:
        title = input("Enter name of the book: ")
        library.remove_book(title)    
    elif ch == 3:
        library.display_books()
    elif ch == 4:
        title = input("Enter name of the book to search: ")
        library.search_book(title)
    elif ch == 5:
       member = input("Enter member name to add: ")
       person.add_member(member)
    elif ch == 6:
       member = input("Enter member name to remove: ")
       person.remove_member(member)
    elif ch == 7:
        member = input("Enter member: ")
        book_title = input("Enter book: ")
        person.borrow_book(member, book_title)
    elif ch == 8:
        member = input("Enter member: ")
        book_title = input("Enter book: ")
        person.return_book(member, book_title)
    elif ch == 9:
        person.ledger_view()
    elif ch == 0:
        break
    else:
        print("Invalid choice!")