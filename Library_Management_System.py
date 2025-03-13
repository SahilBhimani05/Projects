from datetime import datetime
import os

class Book:
    def __init__(self, title, author, count):
        self.title = title.title()
        self.author = author.title()
        self.count = count

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        for book_ in self.books:
            if book.title == book_.title and book.author == book_.author:
                print(f"'{book.title}' by '{book.author}' already exists in the library")
                return
        self.books.append(book)
        print(f"'{book.title}' by '{book.author}' added to the library")

    def remove_book(self, title):
        try:
            found = False
            for book in self.books:
                if book.title == title.title():
                    self.books.remove(book)
                    print(f"'{book.title}' by '{book.author}' removed from the library")
                    found = True
                    break
            if not found:
                print(f"Book '{title}' not found in the library")
        except Exception as e:
            print(f"Error removing book: {e}")

    def display_books(self):
        try:
            print(f"\n{"Book Title":<30}{"Author":<30}{"Availability":<30}{"No. of copies":<30}")
            print("-" * 110)
            for book in self.books:
                availability = "Available" if book.count > 0 else "Unavailable"
                print(f"{book.title:<30}{book.author:<30}{availability:30}{book.count:<30}")
        except Exception as e:
            print(f"Error displaying books: {e}")

    def search_book(self, title):
        try:
            found = False
            for book in self.books:
                if book.title == title.title():
                    availability = "Available" if book.count > 0 else "Unavailable"
                    print(f"\n{"Book Title":<30}{"Author":<30}{"Availability":<30}{"No. of copies":<30}")
                    print("-" * 110)
                    print(f"{book.title:<30}{book.author:<30}{availability:<30}{book.count:<30}")
                    found = True
                    break
            if not found:
                print("Book not found")
        except Exception as e:
            print(f"Error searching for book: {e}")

class Person:
    def __init__(self):
        self.member = []
        self.i_book = {}
        self.transaction = []
        self.header = False

    def add_member(self, member):
        try:
            self.member.append(member)
            print(f"'{member}' added")
        except Exception as e:
            print(f"Error adding member: {e}")

    def remove_member(self, member):
        try:
            self.member.remove(member)
            print(f"'{member}' removed")
        except ValueError:
            print(f"Member '{member}' does not exist")
        except Exception as e:
            print(f"Error removing member: {e}")

    def borrow_book(self, member, book_title):
        try:
            if member not in self.member:
                print(f"Member '{member.title()}' is not added")
            elif member in self.i_book:
                print(f"Member '{member.title()}' can borrow only one book at a time")
            else:
                found = False
                for book in library.books:
                    if book.title == book_title.title():
                        found = True
                        if book.count == 0:
                            print(f"{book.title} can't be issued")
                            break
                        self.i_book[member] = book
                        book.count -= 1
                        print(f"'{book.title}' by '{book.author}' book issued to {member.title()}")
                        issue_date = datetime.now().strftime("%B %d, %Y")
                        self.transaction.append((member.title(), book.title, book.author, "Issued", issue_date, "-"))
                        break
                if not found:
                    print(f"Book '{book_title.title()}' not found or not available")
        except Exception as e:
            print(f"Error borrowing book: {e}")

    def return_book(self, member, book_title):
        try:
            if member in self.member:
                if member in self.i_book and self.i_book[member].title == book_title.title():
                    returned_book = self.i_book.pop(member)
                    for book in library.books:
                        if book.title == returned_book.title:
                            book.count += 1
                            break
                    print(f"'{returned_book.title}' by '{returned_book.author}' book returned by {member.title()}")
                    return_date = datetime.now().strftime("%B %d, %Y")
                    self.transaction.append((member.title(), returned_book.title, returned_book.author, "Returned", "-", return_date))
                else:
                    print(f"'{member.title()}' did not borrow the book '{book_title.title()}'")
            else:
                print(f"Member '{member.title()}' is not found")
        except Exception as e:
            print(f"Error returning book: {e}")

    def ledger_view(self):
        try:
            print(f"\n{"Member":<15}{"Book Title":<30}{"Author":<30}{"Transaction":<15}{"Issue Date":<20}{"Return Date":<20}")
            print("-" * 130)
            for transaction in self.transaction:
                member, title, author, action, issue_date, return_date = transaction
                print(f"{member:<15}{title:<30}{author:<30}{action:<15}{issue_date:<20}{return_date:<20}")
            print()
        except Exception as e:
            print(f"Error displaying ledger: {e}")

    def ledger_file_view(self):
        try:
            if os.path.exists("Member_Transaction.txt"):
                with open("Member_Transaction.txt","a") as file:
                    if not self.header:
                        file.write(f"{"Member":<15}{"Book Title":<30}{"Author":<30}{"Transaction":<15}{"Issue Date":<20}{"Return Date":<20}" + "\n")
                        file.write("-" * 130 + "\n")
                        self.header = True
                    if self.header:
                        for transaction in self.transaction:
                            member, title, author, action, issue_date, return_date = transaction
                            file.write(f"{member:<15}{title:<30}{author:<30}{action:<15}{issue_date:<20}{return_date:<20}" + "\n")
                        self.transaction.clear()
                        print("Ledger view has been printed to Member_Transaction.txt")
                        print()
            else:
                print("File doesn't exist")
        except Exception as e:
            print(f"Error file I/O: {e}")

library = Library()
person = Person()

while True:
    try:
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Search Book")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Ledger View")
        print("10. Ledger View in '.txt' format")
        print("0. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            title = input("Enter name of the book: ")
            author = input("Enter author of the book: ")
            count = int(input("Enter no. of copies: "))
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
        elif ch == 10:
            person.ledger_file_view()
        elif ch == 0:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")