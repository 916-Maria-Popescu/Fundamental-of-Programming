"""
    Service class includes functionalities for implementing program features
"""
import copy
from domain.entity import Book


class Service:

    def __init__(self, validator):
        self.__validator = validator
        self.__entities = []
        self.__backup = []


    def generated_books(self):
        self.__entities.append(Book('978-92-95055-12-5', 'Umberto Eco', 'Numele trandafirului'))
        self.__entities.append(Book('979-97-87664-17-2', 'Fyodor Dostoevsky', 'Crime and Punishment'))
        self.__entities.append(Book('978-32-95242-24-4', 'Erich Maria Remarque', 'Soroc de viata si soroc de moarte'))
        self.__entities.append(Book('978-67-76554-98-0', 'J. D. Salinger', 'Franny and Zooey'))
        self.__entities.append(Book('979-34-71233-34-4', 'Hermann Hesse', 'Narcis si Gura-de-Aur'))
        self.__entities.append(Book('979-87-74945-11-5', 'André Gide', 'Les Faux-monnayeurs'))
        self.__entities.append(Book('978-11-12209-19-7', 'Marin Preda', 'Cel mai iubit dintre pamanteni'))
        self.__entities.append(Book('979-13-34459-45-9', 'Boualem Sansal', 'Satul Neamtului'))
        self.__entities.append(Book('978-65-05373-77-5', 'Fyodor Dostoevsky', 'Idiotul'))
        self.__entities.append(Book('978-87-83498-13-6', 'Nicolas Bouvier', 'Cronica Japoneza'))


    def add_book(self, isbn, author, title):
        """
        This function will add a book with the main list
        """
        book = Book(isbn, author, title)

        try:      #manage dublicate isbn
            self.__validator.dublicate_isbn(book, self.__entities)
        except Exception : print ("ISBN USED\n")

        self.__validator.validate_isbn(book)
        self.__backup.append(copy.deepcopy(self.__entities))
        self.__entities.append(book)

    @property
    def entities(self):
        return self.__entities

    def filter(self, word):
        """
        This function will delete from the main list all the books whose titles start with a given word
        """
        self.__backup.append(copy.deepcopy(self.__entities))
        for book in self.__entities:
            title = book.title.split()
            if title[0] == word:
                book.title = ' '

    def undo (self):
        """
        This function will erase the effect of the last action (add, filter)
        """
        try:
            self.__entities = copy.deepcopy(self.__backup[-1])
            del self.__backup[-1]
        except IndexError:
            print("There is no command to undo!\n")
