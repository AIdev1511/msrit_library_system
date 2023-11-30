import json
from datetime import datetime, timedelta


class Book:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return f'{self.title} by {self.author} - Available: {self.quantity}'


class MSRITLibrarySystem:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, quantity):
        new_book = Book(title, author, quantity)
        self.books.append(new_book)
        print(f'Book "{title}" by {author} added successfully!')

    def check_availability(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.quantity > 0:
                print(f'Book "{book.title}" is available.')
                return True
        print(f'Book "{title}" is not available.')
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.quantity > 0:
                book.quantity -= 1
                print(f'You have successfully borrowed "{book.title}". Enjoy reading!')
                return
        print(f'Book "{title}" is not available for borrowing.')

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.quantity += 1
                print(f'Thank you for returning "{book.title}". Hope you enjoyed reading!')
                return
        print(f'Book "{title}" does not belong to this library.')

    def view_books(self):
        if not self.books:
            print('No books available in the MSRIT library.')
        else:
            print('MSRIT Library Book List:')
            for book in self.books:
                print(book)


def run_msrit_library_system():
    msrit_library = MSRITLibrarySystem()

    while True:
        print("\nWelcome to MSRIT Library System!")
        print("1. Add Book")
        print("2. Check Book Availability")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            quantity = int(input("Enter quantity: "))
            msrit_library.add_book(title, author, quantity)
        elif choice == '2':
            title = input("Enter book title: ")
            msrit_library.check_availability(title)
        elif choice == '3':
            title = input("Enter book title: ")
            msrit_library.borrow_book(title)
        elif choice == '4':
            title = input("Enter book title: ")
            msrit_library.return_book(title)
        elif choice == '5':
            msrit_library.view_books()
        elif choice == '6':
            print('Exiting MSRIT Library System. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 6.')


if __name__ == "__main__":
    run_msrit_library_system()
    print("\nMSRIT Library System developed by Jatin Pandey.")
