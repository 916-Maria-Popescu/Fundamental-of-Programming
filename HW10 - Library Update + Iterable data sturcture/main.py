
from Repository.RepositoryBinaryFiles import BookBinaryRepository, ClientBinaryRepository, RentalBinaryRepository
from Repository.RepositoryTextFiles import BookFileRepository, ClientFileRepository, RentalFileRepository
from Repository.myrepository import RepositoryBook, RepositoryClient, RepositoryRental
from Service.myservices import ServiceBook, ServiceClient, ServiceRental


from UI.myconsole import UI
from Validator.myvalidators import ValidatorBook, ValidatorClient, ValidatorRental

if __name__ == '__main__':
    user_interface = 'UI'  # input("Do you want a UI or GUI?")

    with open("settings", "r") as file:
        lines = file.readlines()
        repository_book_file = (lines[1].split("="))[1].strip()
        repository_client_file = (lines[2].split("="))[1].strip()
        repository_rental_file = (lines[3].split("="))[1].strip()
        repository_setting = (lines[4].split("="))[1].strip()
    ValidatorBook = ValidatorBook()
    ValidatorClient = ValidatorClient()
    ValidatorRental = ValidatorRental()

    if repository_setting == "memory":
        RepositoryBook = RepositoryBook()
        RepositoryClient = RepositoryClient()
        RepositoryRental = RepositoryRental()

    if repository_setting == "binary file":
        RepositoryBook = BookBinaryRepository(repository_book_file)
        RepositoryClient = ClientBinaryRepository(repository_client_file)
        RepositoryRental = RentalBinaryRepository(repository_rental_file)

    if repository_setting == "text file":
        RepositoryBook = BookFileRepository(repository_book_file)
        RepositoryClient = ClientFileRepository(repository_client_file)
        RepositoryRental = RentalFileRepository(repository_rental_file)

    ServiceBook = ServiceBook(ValidatorBook, RepositoryBook)
    ServiceClient = ServiceClient(ValidatorClient, RepositoryClient)
    ServiceRental = ServiceRental(ValidatorRental, RepositoryRental, RepositoryBook, RepositoryClient)

    if user_interface == 'UI':
        cons = UI(ServiceBook, ServiceClient, ServiceRental)
        cons.run_console()

    #elif user_interface == 'GUI':
    #   gui = GUI(ServiceBook, ServiceClient, ServiceRental)
    #   gui.create_gui()

