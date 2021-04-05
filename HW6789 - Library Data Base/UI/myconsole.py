<<<<<<< HEAD
from Service.ServiceUndoRedo import UndoService, RedoService
from Service.UndoRedoHandler import UndoHandler
=======
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
from Service.myrandom import random_book, random_client
from Validator.myvalidators import LibraryException, RepositoryException


class UI:
    def __init__(self, service_book, service_client, service_rental):
        self.__service_book = service_book
        self.__service_client = service_client
        self.__service_rental = service_rental
        self.__commands = {"add book": self.__ui_add_book,
                           "list books": self.__ui_list_books,
                           "remove book": self.__ui_remove_book,
                           "update book": self.__ui_update_book,
                           "add client": self.__ui_add_client,
                           "list clients": self.__ui_list_clients,
                           "remove client": self.__ui_remove_client,
                           "update client": self.__ui_update_client,
                           "rent book": self.__ui_rent_book,
                           "return book": self.__ui_return_book,
                           "list rentals": self.__ui_list_rentals,
                           "search client": self.__ui_search_client,
                           "search book": self.__ui_search_book,
                           "most rented books": self.__ui_most_rented_books,
                           "most rented authors": self.__ui_most_rented_authors,
<<<<<<< HEAD
                           "most active clients": self.__ui_most_active_clients,
                           "undo": UndoService.do_undo,
                           "redo": RedoService.do_redo}

    # --------------------------------------------------------------------------UI rental


=======
                           "most active clients": self.__ui_most_active_clients}

    # --------------------------------------------------------------------------UI rental

>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
    def __ui_rent_book(self):
        id_rental = int(input("   id rental: "))
        id_book = int(input("   id book: "))
        id_client = int(input("   id client: "))
        rented_date = input("   date: ")
        returned_date = "-"
        self.__service_rental.add_rental(id_rental, id_book, id_client, rented_date, returned_date)
<<<<<<< HEAD
        UndoService.store_operation(self.__service_rental, UndoHandler.RENT_BOOK, id_rental)
        RedoService.clear_all_redo()
=======
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4

    def __ui_return_book(self):
        id_rental = int(input("   id rental: "))
        returned_date = input("   date: ")
        self.__service_rental.return_book(id_rental, returned_date)
<<<<<<< HEAD
        UndoService.store_operation(self.__service_rental, UndoHandler.RETURN_BOOK, id_rental)
        RedoService.clear_all_redo()


    def __ui_list_rentals(self):
        rentals = self.__service_rental.get_all_rentals()
        if rentals == None:
            print("no rentals yet")
            return
=======

    def __ui_list_rentals(self):
        rentals = self.__service_rental.get_all_rentals()
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
        for rental in rentals:
            print(rental)

    def __ui_most_rented_books(self):
        books = self.__service_rental.most_rented_books()
        place = 1
        for book in books:
            if int(book[1]) == 1:
<<<<<<< HEAD
                print(" -> {0}st place".format(place))
                print(book[0], "has been rented one time\n")
            else:
                print(" -> {0}st place".format(place))
                print(book[0], "has been rented", book[1], "times\n")
=======
                print(place, " -> ", book[0], "has been rented one time")
            else:
                print(place, " -> ", book[0], "has been rented", book[1], "times")
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
            place = place + 1
        print("The rest of the books registered in this library have not yet been rented")

    def __ui_most_rented_authors(self):
        authors = self.__service_rental.most_rented_authors()
        place = 1
        for author in authors:
            if int(author[1]) == 1:
<<<<<<< HEAD
                print(" -> {0}st place".format(place))
                print(author[0], "'s books have one rental\n")
            else:
                print(" -> {0}st place".format(place))
                print(author[0], "'s books have", author[1], "rentals\n")
            place = place + 1
        print("The rest of the authors do not have rented books")
=======
                print(place, " -> ", author[0], "'s books has one rental")
            else:
                print(place, " -> ", author[0], "'s books has", author[1], "rentals")
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4

    def __ui_most_active_clients(self):
        clients = self.__service_rental.most_active_clients()
        place = 1
        for client in clients:
            if int(client[1]) == 1:
<<<<<<< HEAD
                print(" -> {0}st place".format(place))
                print(client[0], "has one rental day\n")
            else:
                print(" -> {0}st place".format(place))
                print(client[0], "has", client[1], "rental days\n")
=======
                print(place, " -> ", client[0], "has one rental day")
            else:
                print(place, " -> ", client[0], "has", client[1], "rental days")
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
            place = place + 1
        print("The rest of the clients registered in this library have not rented a book yet")

    # --------------------------------------------------------------------------UI client

    def __ui_add_client(self):
        id_client = int(input("   id_client: "))
        name = input("   name: ")
        self.__service_client.add_client(id_client, name)
<<<<<<< HEAD
        UndoService.store_operation(self.__service_client, UndoHandler.ADD_CLIENT, id_client)
        RedoService.clear_all_redo()

=======
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4

    def __ui_list_clients(self):
        print("List:")
        clients = (self.__service_client.get_all_clients())[:]
        if len(clients) == 0:
            print("No clients!")
            return
        for client in clients:
            print(client)

    def __ui_remove_client(self):
        id_client = int(input("The id of the client you want to remove:"))
<<<<<<< HEAD
        name = self.__service_client.find_by_id(id_client).get_name()  # for undo
        self.__service_client.remove_client(id_client)
        UndoService.store_operation(self.__service_client, UndoHandler.REMOVE_CLIENT, id_client, name)
        RedoService.clear_all_redo()

=======
        self.__service_client.remove_client(id_client)
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4

    def __ui_update_client(self):
        id_client = int(input("The id of the client you want to update:"))
        new_name = input("new name:")
<<<<<<< HEAD
        old_name = self.__service_client.find_by_id(id_client).get_name()  # for undo
        self.__service_client.update_client(id_client, new_name)
        UndoService.store_operation(self.__service_client, UndoHandler.UPDATE_CLIENT, id_client, old_name)
        RedoService.clear_all_redo()

=======
        self.__service_client.update_client(id_client, new_name)
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4

    def __ui_search_client(self):
        option = input("Search by name or id?\n:")
        if option == 'id':
            id_client = input("Enter id: ")
            clients = self.__service_client.search_client_id(id_client)
        elif option == 'name':
            name = input("Enter name: ")
            clients = self.__service_client.search_client_name(name)
        else:
            print("Wrong option. Please chose an option between 'id' and 'name'")
            return
        if len(clients) == 0:
            print("There is no such client!")
            return

        for client in clients:
            print(client)

    # -----------------------------------------------------------------------UI BOOK

    def __ui_add_book(self):
        id_book = int(input("Id book: "))
        title = input("title: ")
        author = input("author: ")
        self.__service_book.add_book(id_book, title, author)
<<<<<<< HEAD
        UndoService.store_operation(self.__service_book, UndoHandler.ADD_BOOK, id_book)
        RedoService.clear_all_redo()
=======
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4

    def __ui_list_books(self):
        print("List:")
        books = (self.__service_book.get_all_books())[:]
        if len(books) == 0:
            print("No books!")
<<<<<<< HEAD
            return
=======
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
        for book in books:
            print(book)

    def __ui_remove_book(self):
        id_book = int(input("The id of the book you want to remove: "))
<<<<<<< HEAD
        title = self.__service_book.find_by_id(id_book).get_title()  # for undo
        author = self.__service_book.find_by_id(id_book).get_author()  # for undo
        self.__service_book.remove_book(id_book)
        UndoService.store_operation(self.__service_book, UndoHandler.REMOVE_BOOK, id_book, title, author)
        RedoService.clear_all_redo()

=======
        self.__service_book.remove_book(id_book)
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4

    def __ui_update_book(self):
        id_book = int(input("The id of the book you want to update: "))
        new_title = input("new title: ")
        new_author = input("new author: ")
<<<<<<< HEAD
        old_title = self.__service_book.find_by_id(id_book).get_title()  # for undo
        old_author = self.__service_book.find_by_id(id_book).get_author()  # for undo
        self.__service_book.update_book(id_book, new_title, new_author)
        UndoService.store_operation(self.__service_book, UndoHandler.UPDATE_BOOK, id_book, old_title, old_author)
        RedoService.clear_all_redo()

=======
        self.__service_book.update_book(id_book, new_title, new_author)
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4

    def __ui_search_book(self):
        option = input("Search book by id, title or author?\n:")
        if option == 'id':
            id_book = input("Enter the id: ")
            books = self.__service_book.search_book_id(id_book)
        elif option == 'title':
            title = input("Enter the title: ")
            books = self.__service_book.search_book_title(title)
        elif option == 'author':
            author = input("Enter the author: ")
            books = self.__service_book.search_book_author(author)
        else:
            print("Wrong option. Please chose between 'id', 'title', and 'author' ")
            return
        if len(books) == 0:
            print("There is no such book")
            return
        for book in books:
            print(book)

    # ---------------------------------------------------------------------Console

    def run_console(self):
<<<<<<< HEAD
        # while True:
        #     try:
        #         book, client = random_book(), random_client()
        #         self.__service_book.add_book(book[0], book[1], book[2])
        #         self.__service_client.add_client(client[0], client[1])
        #     except RepositoryException:
        #         continue
        #     if len(self.__service_book.get_all_books()) == 10 and len(self.__service_client.get_all_clients()) == 10:
        #         break

        # self.__service_book.add_book(1, 'Alegerea Sofiei', 'William Styron')
        # self.__service_book.add_book(2, 'The next day', 'John Buck')
        # self.__service_book.add_book(3, 'New ways', 'George London')
        # self.__service_book.add_book(4, 'Indemn la simplitate', 'Ernest Bernea')
        # self.__service_client.add_client(1, 'Cristian')
        # self.__service_client.add_client(2, 'Isabella')
        # self.__service_client.add_client(3, 'Lucia')
        # self.__service_client.add_client(4, 'Alexia')
        # self.__service_rental.add_rental(1, 1, 1, '12.09.2002', '15.09.2002')
        # self.__service_rental.add_rental(2, 1, 3, '17.08.2005', '26.09.2005')
        # self.__service_rental.add_rental(3, 1, 1, '16.12.2020', '18.12.2020')
        # self.__service_rental.add_rental(4, 2, 3, '10.04.2003', '11.03.2003')
        # self.__service_rental.add_rental(5, 2, 4, '15.08.2002', '17.08.2005')
        # self.__service_rental.add_rental(6, 3, 2, '19.02.2007', '28.02.2007')
=======
        while True:
            try:
                book, client = random_book(), random_client()
                self.__service_book.add_book(book[0], book[1], book[2])
                self.__service_client.add_client(client[0], client[1])
            except RepositoryException:
                continue
            if len(self.__service_book.get_all_books()) == 10 and len(self.__service_client.get_all_clients()) == 10:
                break
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4

        print("Your options:\n"
              "-> BOOKS: add book, remove book, update book, list books, search book\n"
              "-> CLIENTS: add client, remove client, update client, list clients, search client\n"
              "-> RENTALS: rent book, return book, list rentals\n"
              "-> STATISTICS: most rented books, most rented authors, most active clients\n"
<<<<<<< HEAD
              "-> undo / redo"
=======
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
              "-> exit")

        while True:
            cmd = input("Enter your command:")
            if len(cmd.strip()) == 0:
                print("No command!")
                continue
            if cmd == "exit":
                print("Bye!")
                return

            if cmd in self.__commands:
                try:
                    self.__commands[cmd]()
                except ValueError:
                    print("wrong params")
                except IndexError:
                    print("wrong params")
                except LibraryException as ex:
                    print(ex)

            else:
                print("wrong command!")
