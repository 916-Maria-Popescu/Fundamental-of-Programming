from Repository.IterableData import IterableData
from Validator.myvalidators import RepositoryException, ValidatorRental


# ------------------------------------------------------------------BOOKS

class RepositoryBook:

    def __init__(self):
        self.__elem = IterableData()

    @property
    def elem(self):
        return self.__elem

    @elem.setter
    def elem(self, value):
        self.__elem = value

    def find_by_id(self, id_book):
        """
        It returns the book the book corresponding with the given id if that book is in the library, otherwise it
        returns none
        """
        for book in self.__elem:
            if book.get_id_book() == id_book:
                return book
        return None

    def add_book(self, book):
        """
        It adds a new book in the library, if the id of the new book is already registered it'll raise an error
        """
        if book in self.__elem:
            raise RepositoryException("duplicate id!")
        self.__elem.append(book)

    def get_all(self):
        return self.__elem[:]

    def remove_book(self, id_book):
        """
        It deletes the book corresponding with the given id from the library, if that id isn't registered it'll raise an
        error
        """
        book = self.find_by_id(id_book)
        if book is None:
            raise RepositoryException("no book to remove")
        del self.__elem[book]

    def update_book(self, id_book, new_title, new_author):
        """
        Can change the title and the author of an existent book by its id
        """
        book = self.find_by_id(id_book)
        if book is None:
            raise RepositoryException("no book to update")
        book.set_title(new_title)
        book.set_author(new_author)


# ------------------------------------------------------------------CLIENTS

class RepositoryClient:
    def __init__(self):
        self.__elem = IterableData()

    @property
    def elem(self):
        return self.__elem

    @elem.setter
    def elem(self, value):
        self.__elem = value

    def find_by_id(self, id_client):
        for client in self.__elem:
            if client.get_id_client() == id_client:
                return client
        return None

    def add_client(self, client):
        if client in self.__elem:
            raise RepositoryException("duplicate id!")
        self.__elem.append(client)

    def get_all(self):
        return self.__elem[:]

    def remove_client(self, id_client):
        client = self.find_by_id(id_client)
        if client is None:
            raise RepositoryException("no client to remove!")
        del self.__elem[client]

    def update_client(self, id_client, new_name):
        client = self.find_by_id(id_client)
        if client is None:
            raise RepositoryException("no client to update!")
        client.set_name(new_name)


# ------------------------------------------------------------------RENTALS


class RepositoryRental:
    def __init__(self):
        self.__elem = IterableData()

    @property
    def elem(self):
        return self.__elem

    @elem.setter
    def elem(self, value):
        self.__elem = value

    def get_all(self):
        return self.__elem[:]

    def find_by_id(self, id_rental):
        """
        It will find the object rent by its id. It'll return either the object, either None (if the rental it's not in
        the list yet)
        """
        for rental in self.__elem:
            if rental.get_id_rental() == id_rental:
                return rental
        return None

    def remove_rental(self, id_rental):
        rental = self.find_by_id(id_rental)
        if rental is None:
            raise RepositoryException("no rental to remove!")
        del self.__elem[rental]

    def add_rental(self, rental):
        """
        It'll add a rental to the list with all rentals after it checks if:
        - there is other rental with the same id
        - the new rental book it was already rented and not returned(checks the dates)
        """
        if rental in self.__elem:
            raise RepositoryException("duplicate id!")
        for rent in self.__elem:
            if rent.get_id_book() == rental.get_id_book():
                if rent.get_returned_date() == '-':
                    raise RepositoryException("Sorry, this book is rented by someone else at this moment!")
        self.__elem.append(rental)

    def return_book(self, id_rental, returned_date):
        """
        It'll complete the rental corresponding to the id by adding the returned date. Now the book will be available
        again.
        -it checks if the there is such an id
        -it checks if the date is past the rented date
        """
        rental = self.find_by_id(id_rental)
        if rental is None:
            raise RepositoryException("Sorry, this rental id does not match any of our library rentals")
        if rental.get_returned_date() != '-':
            raise RepositoryException("This book has already been returned")
        ValidatorRental.validate_return_date(rental.get_rented_date(), returned_date)
        rental.set_returned_date(returned_date)
