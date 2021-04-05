class Book:
    def __init__(self, id_book, title, author):
        self.__id_book = id_book
        self.__title = title
        self.__author = author

    def get_id_book(self):
        return self.__id_book

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def __eq__(self, other):
        return self.__id_book == other.__id_book

    def __str__(self) -> str:
        return "Id book:{0}, Title:{1}, Author:{2}".format(self.__id_book, self.__title, self.__author)


class Client:
    def __init__(self, id_client, name):
        self.__id_client = id_client
        self.__name = name

    def get_id_client(self):
        return self.__id_client

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __eq__(self, other):
        return self.__id_client == other.__id_client

    def __str__(self) -> str:
        return "ID client: {0}, Name: {1}".format(self.__id_client, self.__name)


class Rental:
    def __init__(self, id_rental, id_book, id_client, rented_date, returned_date):
        self.__id_rental = id_rental
        self.__id_book = id_book
        self.__id_client = id_client
        self.__rented_date = rented_date
        self.__returned_date = returned_date

    def get_id_rental(self):
        return self.__id_rental

    def get_id_book(self):
        return self.__id_book

    def get_id_client(self):
        return self.__id_client

    def get_rented_date(self):
        return self.__rented_date

    def get_returned_date(self):
        return self.__returned_date

    def set_returned_date(self, date):
        self.__returned_date = date

    def __eq__(self, other):
        return self.__id_rental == other.__id_rental

    def __str__(self) -> str:
        return "ID rent: {0}, ID book:{1}, ID client{2}, rented date:{3}, returned date{4}".format(self.__id_rental,
                                                                                                   self.__id_book,
                                                                                                   self.__id_client,
                                                                                                   self.__rented_date,
                                                                                                   self.__returned_date)
