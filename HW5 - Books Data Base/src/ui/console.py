"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""

class Console:
    def __init__(self, service):
        self.__service = service

    def print_menu(self):
        print("Choose an option:")
        print("  1-Add a book")
        print("  2-Display all books")
        print("  3-Filter the list so that book titles starting with a given word are deleted")
        print("  4- Undo")
        print("  5- Exit\n")

    def add_book_ui(self):
        isbn = input('isbn:')
        title = input('title:')
        author = input("author:")
        self.__service.add_book(isbn, author, title)

    def filter_ui(self):
        word = input('The key word is:')
        self.__service.filter(word)

    def display_books_ui(self):
        print ("The list with all the books is:")
        for element in self.__service.entities:
            print(element)

    def run_menu(self):
        self.__service.generated_books()
        while True:
            self.print_menu()
            option = int(input("My option is:"))

            if option == 1:
                self.add_book_ui()
            elif option == 2:
                self.display_books_ui()
            elif option == 3:
                self.filter_ui()
            elif option == 4:
                self.__service.undo()
            elif option == 5:
                break
            else:
                print("wrong command\n")
