from datetime import date
from Domain.entities import Book, Client, Rental
from Repository.IterableData import filter_list, comb_sort
from Validator.myvalidators import LibraryException, ServiceException


# ------------------------------------------------------------------BOOKS

class ServiceBook:

    def __init__(self, validator_book, repository_book):
        self.__validator_book = validator_book
        self.__repository_book = repository_book

    def add_book(self, id_book, title, author):
        book = Book(id_book, title, author)
        self.__validator_book.validate(book)
        self.__repository_book.add_book(book)

    def get_all_books(self):
        return self.__repository_book.get_all()

    def find_by_id(self, id_book):
        return self.__repository_book.find_by_id(id_book)

    def remove_book(self, id_book):
        self.__repository_book.remove_book(id_book)

    def update_book(self, id_book, new_title, new_author):
        self.__repository_book.update_book(id_book, new_title, new_author)

    def search_book_id(self, id_book):
        if int(id_book) <= 0:
            raise ServiceException("invalid id!")
        # return list(filter(lambda x: id_book in str(x.get_id_book()), self.__repository_book.get_all()))
        my_list = filter_list(self.__repository_book.get_all(), lambda x: id_book in str(x.get_id_book()))
        return my_list[:]

    def search_book_title(self, title):
        if title == "":
            raise ServiceException("invalid title!")
        # return list(filter(lambda x: title.casefold() in x.get_title().casefold(), self.__repository_book.get_all()))
        my_list = filter_list(self.__repository_book.get_all(), lambda x: title.casefold() in x.get_title().casefold())
        return my_list[:]

    def search_book_author(self, author):
        if author == "":
            raise ServiceException("invalid author!")
        # return list(filter(lambda x: author.casefold() in x.get_author().casefold(),
        # self.__repository_book.get_all()))
        my_list = filter_list(self.__repository_book.get_all(),
                              lambda x: author.casefold() in x.get_author().casefold())
        return my_list[:]


# ------------------------------------------------------------------CLIENTS

class ServiceClient:
    def __init__(self, validator_client, repository_client):
        self.__validator_client = validator_client
        self.__repository_client = repository_client

    def add_client(self, id_client, name):
        client = Client(id_client, name)
        self.__validator_client.validate(client)
        self.__repository_client.add_client(client)

    def get_all_clients(self):
        return self.__repository_client.get_all()

    def find_by_id(self, id_client):
        return self.__repository_client.find_by_id(id_client)

    def remove_client(self, id_client):
        self.__repository_client.remove_client(id_client)

    def update_client(self, id_client, new_name):
        self.__repository_client.update_client(id_client, new_name)

    def search_client_id(self, id_client):
        if int(id_client) <= 0:
            raise ServiceException("wrong id!")
        return list(filter(lambda x: id_client in str(x.get_id_client()), self.__repository_client.get_all()))

    def search_client_name(self, name):
        if name == "":
            raise ServiceException("wrong input")
        return list(filter(lambda x: name.casefold() in x.get_name().casefold(), self.__repository_client.get_all()))


# ------------------------------------------------------------------RENTALS

class ServiceRental:
    def __init__(self, validator_rental, repository_rental, repository_book, repository_client):
        self.__validator_rental = validator_rental
        self.__repository_rental = repository_rental
        self.__repository_book = repository_book
        self.__repository_client = repository_client

    def add_rental(self, id_rental, id_book, id_client, rented_date, returned_date):
        rental = Rental(id_rental, id_book, id_client, rented_date, returned_date)
        self.__validator_rental.validate_rent(rental)  # validates the data introduced
        book = self.__repository_book.find_by_id(id_book)
        if book is None:  # checks if the book is in the library
            raise LibraryException("Sorry, we don't have this book in our library")
        client = self.__repository_client.find_by_id(id_client)
        if client is None:  # check if the client is subscribed to the library
            raise LibraryException("Sorry, this client id does not match any of our library subscribers")

        self.__repository_rental.add_rental(rental)

    def return_book(self, id_rental, returned_date):
        self.__validator_rental.validate_return(id_rental, returned_date)
        self.__repository_rental.return_book(id_rental, returned_date)

    def get_all_rentals(self):
        return self.__repository_rental.get_all()

    def remove_rental(self, id_rental):
        self.__repository_rental.remove_rental(id_rental)

    def most_rented_books(self):
        rentals = self.__repository_rental.get_all()
        most_rented_books = []
        aux_list = []

        for rental in rentals:
            if rental.get_id_book() not in aux_list:
                same_book_rentals = list(filter(lambda x: str(rental.get_id_book()) in str(x.get_id_book()), rentals))
                iteration = (self.__repository_book.find_by_id(rental.get_id_book()), len(same_book_rentals))
                most_rented_books.append(iteration)
                aux_list.append(rental.get_id_book())
        comb_sort(most_rented_books, lambda x, y: x[1] < y[1])
        # most_rented_books = reversed(sorted(most_rented_books, key=lambda x: x[1]))
        return most_rented_books

    def most_active_clients(self):

        rentals = self.__repository_rental.get_all()
        most_active_clients = []
        aux_list = []

        for rental in rentals:
            if rental.get_id_client() not in aux_list:
                same_client_rentals = list(filter(lambda x: str(rental.get_id_client()) in str(x.get_id_client()),
                                                  rentals))
                number_days = 0
                for i in range(0, len(same_client_rentals)):
                    rent = same_client_rentals[i]
                    if rent.get_returned_date() != '-':
                        #
                        returned_date = rent.get_returned_date().split(".")
                        rented_date = rent.get_rented_date().split(".")
                        l_date = date(int(returned_date[2]), int(returned_date[1]), int(returned_date[0]))
                        f_date = date(int(rented_date[2]), int(rented_date[1]), int(rented_date[0]))
                        delta = l_date - f_date
                        #
                        number_days = number_days + delta.days
                iteration = (self.__repository_client.find_by_id(rental.get_id_client()), number_days)
                most_active_clients.append(iteration)
                aux_list.append(rental.get_id_client())
        comb_sort(most_active_clients, lambda x, y: x[1] < y[1])
        # most_active_clients = reversed(sorted(most_active_clients, key=lambda x: x[1]))
        return most_active_clients

    def most_rented_authors(self):
        rentals = self.__repository_rental.get_all()
        most_rented_authors = []
        aux_list = []
        all_authors = []

        for rental in rentals:
            book = self.__repository_book.find_by_id(rental.get_id_book())
            all_authors.append(book.get_author())

        for author in all_authors:
            if author not in aux_list:
                most_rented_authors.append((author, all_authors.count(author)))
                aux_list.append(author)
        comb_sort(most_rented_authors, lambda x, y: x[1] < y[1])
        # most_rented_authors = reversed(sorted(most_rented_authors, key=lambda x: x[1]))
        return most_rented_authors
