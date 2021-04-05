from Domain.entities import Book, Client, Rental


class LibraryException(Exception):
    pass


class ServiceException(LibraryException):
    pass


class RepositoryException(LibraryException):
    pass


class ValidatorException(LibraryException):
    pass


class BookValidatorException(ValidatorException):
    pass


class ClientValidatorException(ValidatorException):
    pass


class RentalValidatorException(ValidatorException):
    pass



class ValidatorBook:

    @staticmethod
    def validate(book):
        errors = ""
        if Book.get_id_book(book) <= 0:
            errors += "invalid id\n"
        if Book.get_title(book) == "":
            errors += "invalid title\n"
        if Book.get_author(book) == "":
            errors += "invalid author\n"
        if len(errors) > 0:
            raise BookValidatorException(errors)


class ValidatorClient:

    @staticmethod
    def validate(client):
        errors = ""
        if Client.get_id_client(client) <= 0:
            errors += "invalid id"
        if Client.get_name(client) == "":
            errors += "invalid name!"
        if len(errors) > 0:
            raise ClientValidatorException(errors)


class ValidatorRental:

    @staticmethod
    def validate_rent(rental):
        errors = ""
        date = (Rental.get_rented_date(rental)).split(".")
        if int(date[0]) > 31 or int(date[1]) > 12 or int(date[0] or date[1] or date[2]) <= 0:
            errors += "invalid data"
        if Rental.get_id_rental(rental) <= 0:
            errors += "invalid rental id"
        if len(errors) > 0:
            raise RentalValidatorException(errors)

    @staticmethod
    def validate_return(id_rental, date):
        errors = ""
        if int(date[0]) > 31 or int(date[1]) > 12 or int(date[0] or date[1] or date[2]) <= 0:
            errors += "invalid data"
        if id_rental <= 0:
            errors += "invalid rental id"
        if len(errors) > 0:
            raise RentalValidatorException(errors)

    @staticmethod
    def validate_return_date(rented_date, returned_date):
        """
        rented_date[0] = day, rented_date[1] = month, rented_date[2] = year
        returned_date[0] = day, returned_date[1] = month, returned_date[2] = year
        """
        rented_date, returned_date = rented_date.split("."), returned_date.split(".")
        if returned_date[2] < returned_date[1]:
            raise RentalValidatorException("Wrong date! - The rented date is past the returned date")
        elif returned_date[2] == rented_date[2]:
            if returned_date[1] < rented_date[1]:
                raise RentalValidatorException("Wrong date! - The rented date is past the returned date")
            elif returned_date[0] < rented_date[0]:
                raise RentalValidatorException("Wrong date! - The rented date is past the returned date")

