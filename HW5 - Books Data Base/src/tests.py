from domain.entity import Book
from services.service import Service
from services.validator import BookValidator


def set_up(): #This function will be called at the beggining of every test function
    validator = BookValidator()
    a = Service(validator)
    a.entities.append(Book('978-92-00055-99-9', ' A0', 'word T0'))
    a.entities.append(Book('978-92-95055-12-9', 'A1', 'T1'))
    a.entities.append(Book('978-92-00055-12-9', 'A2', 'T2'))
    return a


def test_add_book(): #test the add_book function from service
    a = set_up()
    Service.add_book(a,'978-02-00055-99-9', 'A3', 'T3')
    Service.add_book(a,'978-02-00000-99-9', 'A4', 'T4')
    assert len(a.entities) == 5


def test_filter(): #test the filter function from service
    a = set_up()
    Service.filter(a,'word')
    book = a.entities[0]
    assert book.title == ' '


def test_undo(): #test the undo function from service
    a = set_up()
    Service.add_book(a, '978-02-00055-99-9', 'A3', 'T3')
    Service.undo(a)
    assert len(a.entities) == 3


def test_all(): #all the test functions go here
    test_add_book()
    test_filter()
    test_undo()









