from Domain.entities import Book, Client, Rental
from Repository.myrepository import RepositoryBook, RepositoryClient, RepositoryRental

# ------------------------------------------------------------------------------BOOK


class BookFileRepository(RepositoryBook):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line != "\n":
                    line = line.split(",")
                    book = Book(int(line[0]), line[1], line[2].strip())
                    super().add_book(book)

    def __save_to_file(self):
        books = super().get_all()
        with open(self.file_name, "w") as f:
            for book in books:
                book_str = str(book.get_id_book()) + "," + str(book.get_title()) + "," + str(book.get_author() + "\n")
                f.write(book_str)

    def find_by_id(self, id_book):
        return super().find_by_id(id_book)

    def add_book(self, book):
        super().add_book(book)
        self.__save_to_file()

    def get_all(self):
        return super().get_all()

    def remove_book(self, id_book):
        super().remove_book(id_book)
        self.__save_to_file()

    def update_book(self, id_book, new_title, new_author):
        super().update_book(id_book, new_title, new_author)
        self.__save_to_file()


# ------------------------------------------------------------------------------- CLIENT
class ClientFileRepository(RepositoryClient):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_data()

    def __save_to_file(self):
        clients = super().get_all()[:]
        with open(self.__file_name, "w") as f:
            for client in clients:
                client_str = str(client.get_id_client()) + "," + client.get_name() + "\n"
                f.write(client_str)

    def __load_data(self):
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line != "\n":
                    line = line.split(",")
                    client = Client(int(line[0]), line[1].strip())
                    super().add_client(client)

    def find_by_id(self, id_client):
        return super().find_by_id(id_client)

    def add_client(self, client):
        super().add_client(client)
        self.__save_to_file()

    def get_all(self):
        return super().get_all()

    def remove_client(self, id_client):
        super().remove_client(id_client)
        self.__save_to_file()

    def update_client(self, id_client, new_name):
        super().update_client(id_client, new_name)
        self.__save_to_file()


# -----------------------------------------------------------------------------------------RENTAL

class RentalFileRepository(RepositoryRental):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line != "\n":
                    line = line.split(",")
                    rental = Rental(int(line[0]), int(line[1]), int(line[2]), line[3], line[4].strip())
                    super().add_rental(rental)

    def __save_to_file(self):
        rentals = super().get_all()
        with open(self.__file_name, "w") as f:
            for rental in rentals:
                rental_str = str(rental.get_id_rental()) + "," + str(rental.get_id_book()) + "," + str(
                    rental.get_id_client()) + "," + str(rental.get_rented_date()) + "," + str(rental.get_returned_date()) + "\n"
                f.write(rental_str)

    def get_all(self):
        return super().get_all()

    def find_by_id(self, id_rental):
        return super().find_by_id(id_rental)

    def remove_rental(self, id_rental):
        super().remove_rental(id_rental)
        self.__save_to_file()

    def add_rental(self, rental):
        super().add_rental(rental)
        self.__save_to_file()

    def return_book(self, id_rental, returned_date):
        super().return_book(id_rental, returned_date)
        self.__save_to_file()

