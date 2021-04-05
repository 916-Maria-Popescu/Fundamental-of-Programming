from enum import Enum
from Service.ServiceUndoRedo import RedoService, UndoService


# -----------------------------------------------------------------------------------------BOOK

def undo_add_book(service_book, id_book):
    title = service_book.find_by_id(id_book).get_title()  # for redo
    author = service_book.find_by_id(id_book).get_author()  # for redo
    service_book.remove_book(id_book)
    RedoService.store_operation(service_book, RedoHandler.ADD_BOOK, id_book, title, author)


def undo_remove_book(service_book, id_book, title, author):
    service_book.add_book(id_book, title, author)
    RedoService.store_operation(service_book, RedoHandler.REMOVE_BOOK, id_book)


def undo_update_book(service_book, id_book, old_title, old_author):
    new_title = service_book.find_by_id(id_book).get_title  # for redo
    new_author = service_book.find_by_id(id_book).get_author  # for redo
    service_book.find_by_id(id_book).set_title(old_title)
    service_book.find_by_id(id_book).set_author(old_author)
    RedoService.store_operation(service_book, RedoHandler.UPDATE_BOOK, id_book, new_title, new_author)


# ------------------------------------------------------------------------------------------CLIENT

def undo_add_client(service_client, id_client):
    name = service_client.find_by_id(id_client).get_name()
    service_client.remove_client(id_client)
    RedoService.store_operation(service_client, RedoHandler.ADD_CLIENT, id_client, name)


def undo_remove_client(service_client, id_client, name):
    service_client.add_client(id_client, name)
    RedoService.store_operation(service_client, RedoHandler.REMOVE_CLIENT, id_client)


def undo_update_client(service_client, id_client, old_name):
    new_name = service_client.find_by_id(id_client).get_name()  # for redo
    service_client.find_by_id(id_client).set_name(old_name)
    RedoService.store_operation(service_client, RedoHandler.UPDATE_CLIENT, id_client, new_name)


# ---------------------------------------------------------------------------------------RENTAL

def undo_rent_book(service_rental, id_rental):
    id_book = service_rental.find_by_id(id_rental).get_id_book()  # for redo
    id_client = service_rental.find_by_id(id_rental).get_id_client()  # fore redo
    rented_date = service_rental.find_by_id(id_rental).get_rented_date()  # for redo
    service_rental.remove_rental(id_rental)
    RedoService.store_operation(service_rental, RedoHandler.RENT_BOOK, id_rental, id_book, id_client, rented_date)


def undo_return_book(service_rental, id_rental):
    returned_date = service_rental.find_by_id(id_rental).get_returned_date()
    service_rental.find_by_id(id_rental).set_returned_date('-')
    RedoService.store_operation(service_rental, RedoHandler.RETURN_BOOK, id_rental, returned_date)


# ---------UNDO HANDLER CLASS

class UndoHandler(Enum):
    ADD_BOOK = undo_add_book
    REMOVE_BOOK = undo_remove_book
    UPDATE_BOOK = undo_update_book

    ADD_CLIENT = undo_add_client
    REMOVE_CLIENT = undo_remove_client
    UPDATE_CLIENT = undo_update_client

    RENT_BOOK = undo_rent_book
    RETURN_BOOK = undo_return_book


# -----------------------------------------------------------------------------------BOOK

def redo_add_book(service_book, id_book, title, author):
    service_book.add_book(id_book, title, author)
    UndoService.store_operation(service_book, UndoHandler.ADD_BOOK, id_book)


def redo_remove_book(service_book, id_book):
    title = service_book.find_by_id(id_book).get_title()
    author = service_book.find_by_id(id_book).get_author()
    service_book.remove_book(id_book)
    UndoService.store_operation(service_book, UndoHandler.REMOVE_BOOK, id_book, title, author)


def redo_update_book(service_book, id_book, title, author):
    old_title = service_book.find_by_id(id_book).get_title()
    old_author = service_book.find_by_id(id_book).get_author()
    service_book.find_by_id(id_book).set_title(title)
    service_book.find_by_id(id_book).set_author(author)
    UndoService.store_operation(service_book, UndoHandler.UPDATE_BOOK, id_book, old_title, old_author)


# --------------------------------------------------------------------------------------CLIENT


def redo_add_client(service_client, id_client, name):
    service_client.add_client(id_client, name)
    UndoService.store_operation(service_client, UndoHandler.ADD_CLIENT, id_client)


def redo_remove_client(service_client, id_client):
    name = service_client.find_by_id(id_client).get_name()
    service_client.remove_client(id_client)
    UndoService.store_operation(service_client, UndoHandler.REMOVE_CLIENT, id_client, name)


def redo_update_client(service_client, id_client, name):
    old_name = service_client.find_by_id(id_client).get_name()
    service_client.find_by_id(id_client).set_name(name)
    UndoService.store_operation(service_client, UndoHandler.UPDATE_CLIENT, id_client, old_name)


# ---------------------------------------------------------------------------------------RENTAL

def redo_rent_book(service_rental, id_rental, id_book, id_client, rented_date):
    service_rental.add_rental(id_rental, id_book, id_client, rented_date, '-')
    UndoService.store_operation(service_rental, UndoHandler.RENT_BOOK, id_rental)


def redo_return_book(service_rental, id_rental, returned_date):
    service_rental.find_by_id(id_rental).set_returned_date(returned_date)
    UndoService.store_operation(service_rental, UndoHandler.RETURN_BOOK, id_rental)


# -----------------------------------------------------------------------------------CLIENT

class RedoHandler(Enum):
    ADD_BOOK = redo_add_book
    REMOVE_BOOK = redo_remove_book
    UPDATE_BOOK = redo_update_book

    ADD_CLIENT = redo_add_client
    REMOVE_CLIENT = redo_remove_client
    UPDATE_CLIENT = redo_update_client

    RENT_BOOK = redo_rent_book
    RETURN_BOOK = redo_return_book
