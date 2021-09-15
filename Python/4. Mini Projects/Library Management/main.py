# -----Mini Project 1 - OOPs Library-----
"""
Rules -
Create a Library class
Methods: display_books, lend_book (who owns the book if not present), add_book, return_book
HarryLibrary = Library(list_of_books, library_name)
dictionary (key = book_name, value = name_of_the_person)
create main function and run infinite while loop asking user for their input
"""


class Library:
    def __init__(self, book_list, lib_name):
        self.booksList = book_list
        self.name = lib_name
        self.lendDict = {}

    def display_books(self):
        print("\nWe have following books in our library:-")
        for book_name in self.booksList:
            print(book_name)

    def lend_book(self, book_name, user_name):
        if book_name in self.booksList:
            if book_name not in self.lendDict.keys():
                self.lendDict.update({book_name: user_name})
                print("Lender-Book database has been updated. You can take the book now.")
            else:
                print(f"Book is already being used by '{self.lendDict[book_name]}'.")
        else:
            print(f"'{book_name}' is not in our library.")

    def add_book(self, book_name):
        self.booksList.append(book_name)
        print("Book has been added to the book list.")

    def return_book(self, book_name):
        if book_name in self.booksList:
            if book_name in self.lendDict.keys():
                self.lendDict.pop(book_name)
                print("Successfully returned.")
            else:
                print("You can't return a book which you haven't lent.")
        else:
            print(f"'{book_name}' is not in our library.")


if __name__ == '__main__':
    # customisable inputs
    list_of_books = ["Engineering Mathematics", "Analog Electronics", "Electromagnetic Theory", "Microprocessor",
                     "Digital Electronics", "Network Theory", "Electronic Devices"]
    HarryLibrary = Library(list_of_books, "Harry's Library")

    # main program
    print(f"----Welcome to {HarryLibrary.name}----")
    user = input("Please enter your name: ").capitalize()
    print(f"Welcome {user}.")

    while True:
        print("\nPress 1 to see books details\n"
              "Press 2 to lend a book\n"
              "Press 3 to add a book in library\n"
              "Press 4 to return a book\n"
              "Press 5 to exit")
        ch = input("Enter your choice: ")
        if ch == '1':
            HarryLibrary.display_books()
        elif ch == '2':
            book = input("Enter the name of the book you want to lend: ")
            HarryLibrary.lend_book(book, user)
        elif ch == '3':
            book = input("Enter the name of the book you want to add: ")
            HarryLibrary.add_book(book)
        elif ch == '4':
            book = input("Enter the name of the book you want to return: ")
            HarryLibrary.return_book(book)
        elif ch == '5':
            print("\nThanks for visiting\n")
            break
        else:
            print("Invalid Input")
