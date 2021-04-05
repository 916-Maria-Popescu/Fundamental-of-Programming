# ------------------------------------------------------------------------------BOOK
import pickle
from Repository.myrepository import RepositoryBook, RepositoryClient, RepositoryRental


class BookBinaryRepository(RepositoryBook):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        try:
            with open(self.__file_name, "rb") as file:
                self.elem = pickle.load(file)

        except EOFError:
            return

    def __save_to_file(self):
        with open(self.__file_name, "wb") as file:
            pickle.dump(self.elem, file)

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
class ClientBinaryRepository(RepositoryClient):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        try:
            with open(self.__file_name, "rb") as file:
                self.elem = pickle.load(file)
        except EOFError:
            return

    def __save_to_file(self):
        with open(self.__file_name, "wb") as f:
            pickle.dump(self.elem, f)

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

class RentalBinaryRepository(RepositoryRental):

    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        try:
            with open(self.__file_name, "rb") as file:
                self.elem = pickle.load(file)
        except EOFError:
            return

    def __save_to_file(self):
        with open(self.__file_name, "wb") as file:
            pickle.dump(self.elem, file)

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
