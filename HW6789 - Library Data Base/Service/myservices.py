from datetime import date
<<<<<<< HEAD
=======
from itertools import count

>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
from Domain.entities import Book, Client, Rental
from Validator.myvalidators import LibraryException, ServiceException


<<<<<<< HEAD
# ------------------------------------------------------------------BOOKS

=======
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
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

<<<<<<< HEAD
    def find_by_id(self, id_book):
        return self.__repository_book.find_by_id(id_book)

=======
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
    def remove_book(self, id_book):
        self.__repository_book.remove_book(id_book)

    def update_book(self, id_book, new_title, new_author):
        self.__repository_book.update_book(id_book, new_title, new_author)

    def search_book_id(self, id_book):
        if int(id_book) <= 0:
            raise ServiceException("invalid id!")
        return list(filter(lambda x: id_book in str(x.get_id_book()), self.__repository_book.get_all()))

    def search_book_title(self, title):
        if title == "":
            raise ServiceException("invalid title!")
        return list(filter(lambda x: title.casefold() in x.get_title().casefold(), self.__repository_book.get_all()))

    def search_book_author(self, author):
        if author == "":
            raise ServiceException("invalid author!")
        return list(filter(lambda x: author.casefold() in x.get_author().casefold(), self.__repository_book.get_all()))


<<<<<<< HEAD
# ------------------------------------------------------------------CLIENTS

=======
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
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

<<<<<<< HEAD
    def find_by_id(self, id_client):
        return self.__repository_client.find_by_id(id_client)

=======
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
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


<<<<<<< HEAD
# ------------------------------------------------------------------RENTALS

=======
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
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

<<<<<<< HEAD
    def remove_rental(self, id_rental):
        self.__repository_rental.remove_rental(id_rental)

    def most_rented_books(self):
=======
    def most_rented_books(self):
        """
        It will provide the list of books, sorted in descending order of the number of times they were rented:
        -same_book_rentals -> list with all of the rentals that include a certain book
        -iteration -> tuple (the book, the number of rentals of that book)
        -aux_list -> list with all the books that have been rented (first is empty and as the list with all the rentals
                    is traversed, the books that are in the list are added to aux_list)
                  -> this list helps us to check if we already made an iteration tuple for a rented book
        -most_rented_books -> a list with tupels
        """
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
        rentals = self.__repository_rental.get_all()
        most_rented_books = []
        aux_list = []

        for rental in rentals:
            if rental.get_id_book() not in aux_list:
                same_book_rentals = list(filter(lambda x: str(rental.get_id_book()) in str(x.get_id_book()), rentals))
                iteration = (self.__repository_book.find_by_id(rental.get_id_book()), len(same_book_rentals))
                most_rented_books.append(iteration)
                aux_list.append(rental.get_id_book())
<<<<<<< HEAD
=======

>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
        most_rented_books = reversed(sorted(most_rented_books, key=lambda x: x[1]))
        return most_rented_books

    def most_active_clients(self):
<<<<<<< HEAD

=======
        """
        It will provide the list og clients, sorted in descending of the number of book rental days they have in total.
        - it will make a list <same_client_rentals> with all the rentals of the same client
        -for each rental, it will find out how many days the client had the book, and compute all the days
        (for this we will use another function)
        -it will make a tuple <iteration> formed by the clients and the total number of days
        -the tuple will be added to <most_active_clients> for each client
        -the list <most_active_clients> will be sorted by the second elem of the tuple and reversed
        ------
        same_client_rentals -> list with Rentals
        iteration -> tuple (Client, the total number of days)

        """
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
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
<<<<<<< HEAD
=======
                    print(rent)
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
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

        most_active_clients = reversed(sorted(most_active_clients, key=lambda x: x[1]))
        return most_active_clients

    def most_rented_authors(self):
<<<<<<< HEAD
=======
        """
         This provides the list of books authored, sorted in descending order of the number of rentals their books have.
        -it will make a list with all the rentals from the same author
        -
        """
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
        rentals = self.__repository_rental.get_all()
        most_rented_authors = []
        aux_list = []
        all_authors = []

        for rental in rentals:
            all_authors.append(self.__repository_book.find_by_id(rental.get_id_book()).get_author())

        for author in all_authors:
            if author not in aux_list:
                most_rented_authors.append((author, all_authors.count(author)))
                aux_list.append(author)

        most_rented_authors = reversed(sorted(most_rented_authors, key=lambda x: x[1]))
        return most_rented_authors
