"""
You will be given one of the problems below to solve using feature-driven development
The program must provide a menu-driven console user interface.
Use classes to represent the following:
The domain entity (complex, expense, student, book)
A services class that implements the required functionalities
The ui class which implements the user interface
Have 10 programmatically generated entries in the application at start-up.
Unit tests and specifications for non-UI functions related to the first functionality.

4. Books
Manage a list of books. Each book has an isbn (string, unique), an author and a title (strings). Provide the following features:

Add a book. Book data is read from the console.
Display the list of books.
Filter the list so that book titles starting with a given word are deleted from the list.
Undo the last operation that modified program data. This step can be repeated.
"""
from services.service import Service
from services.validator import BookValidator
from tests import test_all
from ui.console import Console


if __name__ == '__main__':
    test_all()
    try:
        validator = BookValidator()
        service = Service(validator)
        console = Console(service)
        console.run_menu()

    except Exception as ex:
        print('Unexpected exception! ', ex)

