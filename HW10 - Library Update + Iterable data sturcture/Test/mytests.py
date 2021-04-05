import unittest
from Domain.entities import Book, Client, Rental
from Repository.IterableData import IterableData, filter_list, comb_sort
from Repository.myrepository import RepositoryBook, RepositoryClient, RepositoryRental
from Service.myservices import ServiceBook, ServiceClient, ServiceRental
from Validator.myvalidators import RepositoryException, ValidatorBook, ServiceException, ValidatorClient, \
    ValidatorRental


# -------------------------------------------------------------------------TEST DOMAIN

class TestBook(unittest.TestCase):

    def test_book(self):
        book = Book(10, 'title', 'author')

        self.assertEqual(book.get_id_book(), 10)
        self.assertEqual(book.get_title(), 'title')
        self.assertEqual(book.get_author(), 'author')

        book.set_author('new_author')
        book.set_title('new_title')
        self.assertEqual(book.get_author(), 'new_author')
        self.assertEqual(book.get_title(), 'new_title')

class TestIterabledata(unittest.TestCase):

    def test_iterable_data(self):
        list = IterableData()

        #append
        list.append(2)
        self.assertEqual(len(list), 1)
        list.append(5)
        self.assertEqual(len(list), 2)
        list.append(10)
        list.append(21)
        list.append(99)

        #del
        del list[0]
        self.assertEqual(len(list), 4)
        with self.assertRaises(IndexError):
            del list[6]

        #index
        self.assertEqual(list[0], 5)
        with self.assertRaises(IndexError):
            a = list[7]

        #set
        list[0] = 100
        self.assertEqual(list[0], 100)

        # for el in list
        aux = []
        for el in list:
            aux.append(el)
        self.assertEqual(list[0], aux[0])
        self.assertEqual(len(aux), len(list))
        for i in range(len(list)):
            self.assertEqual(list[i], aux[i])


    def test_filter_function(self):

        mylist = [8, 0, 7, 9, 6]
        condition = lambda x: True if x < 3 else False
        new_list = filter_list(mylist, condition)
        self.assertEqual(len(new_list), 1)

        for i in range(len(new_list)):
            value = new_list[i] < 3
            self.assertEqual(value, True)


    def test_comb_sort(self):
        array = [3, 6, 10, 44, 6]
        new_array = [44, 10, 6, 6, 3]
        condition = lambda x, y: x < y
        comb_sort(array, condition)
        self.assertEqual(len(new_array), len(array))
        self.assertEqual(array[0], new_array[0])





class TestClient(unittest.TestCase):

    def test_client(self):
        client = Client(10, 'name')
        self.assertEqual(client.get_id_client(), 10)
        self.assertEqual(client.get_name(), 'name')

        client.set_name('new_name')
        self.assertEqual(client.get_name(), 'new_name')


class TestRental(unittest.TestCase):

    def test_rental(self):
        rental = Rental(10, 11, 12, '12.09.2002', '13.09.2003')
        self.assertEqual(rental.get_id_book(), 11)
        self.assertEqual(rental.get_rented_date(), '12.09.2002')
        self.assertEqual(rental.get_returned_date(), '13.09.2003')
        self.assertEqual(rental.get_id_rental(), 10)
        self.assertEqual(rental.get_id_client(), 12)

        rental.set_returned_date('14.09.2004')
        self.assertEqual(rental.get_returned_date(), '14.09.2004')


# ----------------------------------------------------------------------------TEST REPOSITORY

class TestRepoBook(unittest.TestCase):

    def setUp(self):
        self.book_repo = RepositoryBook()
        self.book_repo.add_book(Book(1, "title1", "author1"))
        self.book_repo.add_book(Book(2, 'title2', 'author2'))
        self.book_repo.add_book(Book(3, 'title3', 'author3'))
        self.book_repo.add_book(Book(4, 'title4', 'author4'))

    def test_add_book(self):
        self.assertEqual(len(self.book_repo.get_all()), 4)
        with self.assertRaises(RepositoryException):
            self.book_repo.add_book(Book(3, 'a', 'b'))

    def test_find_by_id(self):
        self.assertEqual(self.book_repo.find_by_id(1), Book(1, "title1", "author1"))
        self.assertEqual(self.book_repo.find_by_id(5), None)

    def test_get_all(self):
        my_list = [Book(1, "title1", "author1"), Book(2, 'title2', 'author2'), Book(3, 'title3', 'author3'),
                   Book(4, 'title4', 'author4')]
        self.assertEqual(self.book_repo.get_all(), my_list)

    def test_remove_book(self):
        self.book_repo.remove_book(4)
        self.assertEqual(len(self.book_repo.get_all()), 3)
        self.assertEqual(self.book_repo.get_all()[2], Book(3, 'title3', 'author3'))

        with self.assertRaises(RepositoryException):
            self.book_repo.remove_book(5)

    def test_update_book(self):
        self.book_repo.update_book(1, 'new_title', 'new_author')
        self.assertEqual(self.book_repo.get_all()[0], Book(1, 'new_title', 'new_author'))

        with self.assertRaises(RepositoryException):
            self.book_repo.update_book(5, 'a', 'a')


class TestRepoClient(unittest.TestCase):
    def setUp(self):
        self.client_repo = RepositoryClient()
        self.client_repo.add_client(Client(1, "name1"))
        self.client_repo.add_client(Client(2, 'name2'))
        self.client_repo.add_client(Client(3, 'name3'))
        self.client_repo.add_client(Client(4, 'name4'))

    def test_add_client(self):
        self.assertEqual(len(self.client_repo.get_all()), 4)
        with self.assertRaises(RepositoryException):
            self.client_repo.add_client(Client(4, 'a'))

    def test_find_by_id(self):
        self.assertEqual(self.client_repo.find_by_id(1), Client(1, "name1"))
        self.assertEqual(self.client_repo.find_by_id(5), None)

    def test_get_all(self):
        my_list = [Client(1, "name1"), Client(2, 'name2'), Client(3, 'name3'), Client(4, 'name4')]
        self.assertEqual(self.client_repo.get_all(), my_list)

    def test_remove_book(self):
        self.client_repo.remove_client(4)
        self.assertEqual(len(self.client_repo.get_all()), 3)
        self.assertEqual(self.client_repo.get_all()[2], Client(3, 'name3'))

        with self.assertRaises(RepositoryException):
            self.client_repo.remove_client(5)

    def test_update_book(self):
        self.client_repo.update_client(1, 'new_name')
        self.assertEqual(self.client_repo.get_all()[0], Client(1, 'new_name'))

        with self.assertRaises(RepositoryException):
            self.client_repo.update_client(5, 'a')


class TestRepoRental(unittest.TestCase):

    def setUp(self):
        self.rental_repo = RepositoryRental()
        self.rental_repo.add_rental(Rental(10, 10, 10, '12.09.2002', '13.09.2003'))
        self.rental_repo.add_rental(Rental(11, 11, 11, '14.09.2000', '15.09.2002'))
        self.rental_repo.add_rental(Rental(12, 12, 12, '15.08.2005', '-'))

    def test_add_rental(self):
        self.assertEqual(len(self.rental_repo.get_all()), 3)

        with self.assertRaises(RepositoryException):
            self.rental_repo.add_rental(Rental(10, 23, 65, '12.09.2002', '15.09.2002'))

        with self.assertRaises(RepositoryException):
            self.rental_repo.add_rental(Rental(13, 12, 14, '12.09.2007', '12.09.2009'))

    def test_get_all(self):
        my_list = [Rental(10, 10, 10, '12.09.2002', '13.09.2003'), Rental(11, 11, 11, '14.09.2000', '15.09.2002'),
                   Rental(12, 12, 12, '15.08.2005', '-')]
        self.assertEqual(self.rental_repo.get_all(), my_list)

    def test_find_by_id(self):
        self.assertEqual(self.rental_repo.find_by_id(10), Rental(10, 10, 10, '12.09.2002', '13.09.2003'))
        self.assertEqual(self.rental_repo.find_by_id(15), None)

    def test_return_book(self):
        self.rental_repo.return_book(12, '17.09.2009')
        self.assertEqual((self.rental_repo.get_all()[2]).get_returned_date(), '17.09.2009')

        with self.assertRaises(RepositoryException):
            self.rental_repo.return_book(10, '10.10.2020')

        with self.assertRaises(RepositoryException):
            self.rental_repo.return_book(15, '10.10.2020')


# -----------------------------------------------------------------------------TEST SERVICE

class TestServiceBook(unittest.TestCase):
    def setUp(self):
        self.val_book = ValidatorBook()
        self.repo_book = RepositoryBook()
        self.serv_book = ServiceBook(self.val_book, self.repo_book)
        self.serv_book.add_book(1, 'title1', 'author1')
        self.serv_book.add_book(2, 'title2', 'author2')
        self.serv_book.add_book(3, 'title3', 'author3')
        self.serv_book.add_book(4, 'title4', 'author4')

    def test_add_book(self):
        self.assertEqual(len(self.serv_book.get_all_books()), 4)

    def test_update_book(self):
        self.serv_book.update_book(4, 'new title', 'new author')
        self.assertEqual(self.serv_book.get_all_books()[3], Book(4, 'new title', 'new author'))
        self.assertEqual(len(self.serv_book.get_all_books()), 4)

    def test_remove_book(self):
        self.serv_book.remove_book(4)
        self.assertEqual(len(self.serv_book.get_all_books()), 3)
        self.assertEqual(self.serv_book.get_all_books()[2], Book(3, 'title3', 'author3'))

    def test_get_all(self):
        list_books = [Book(1, 'title1', 'author1'), Book(2, 'title2', 'author2'), Book(3, 'title3', 'author3'),
                      Book(4, 'title4', 'author4')]
        self.assertEqual(self.serv_book.get_all_books(), list_books)

    def test_search_book_by_id(self):
        self.assertEqual(self.serv_book.search_book_id('1'), [Book(1, 'title1', 'author1')])
        with self.assertRaises(ServiceException):
            self.serv_book.search_book_id('-5')

    def test_search_book_by_author(self):
        self.assertEqual(self.serv_book.search_book_author('author1'), [Book(1, 'title1', 'author1')])
        with self.assertRaises(ServiceException):
            self.serv_book.search_book_author('')

    def test_search_book_by_title(self):
        self.assertEqual(self.serv_book.search_book_title('title1'), [Book(1, 'title1', 'author1')])
        with self.assertRaises(ServiceException):
            self.serv_book.search_book_title('')

    def test_find_by_id(self):
        self.assertEqual(self.serv_book.find_by_id(1), Book(1, 'title1', 'author1'))
        self.assertEqual(self.serv_book.find_by_id(7), None)


class TestServiceClient(unittest.TestCase):
    def setUp(self):
        self.val_client = ValidatorClient()
        self.repo_client = RepositoryClient()
        self.serv_client = ServiceClient(self.val_client, self.repo_client)
        self.serv_client.add_client(1, 'name1')
        self.serv_client.add_client(2, 'name2')
        self.serv_client.add_client(3, 'name3')
        self.serv_client.add_client(4, 'name4')

    def test_add_client(self):
        self.assertEqual(len(self.serv_client.get_all_clients()), 4)

    def test_update_client(self):
        self.serv_client.update_client(4, 'new name')
        self.assertEqual(self.serv_client.get_all_clients()[3], Client(4, 'new name'))
        self.assertEqual(len(self.serv_client.get_all_clients()), 4)

    def test_remove_client(self):
        self.serv_client.remove_client(4)
        self.assertEqual(len(self.serv_client.get_all_clients()), 3)
        self.assertEqual(self.serv_client.get_all_clients()[2], Client(3, 'name3'))

    def test_find_by_id(self):
        self.assertEqual(self.serv_client.find_by_id(1), Client(1, 'name1'))
        self.assertEqual(self.serv_client.find_by_id(7), None)

    def test_get_all(self):
        list_clients = [Client(1, 'name1'), Client(2, 'name2'), Client(3, 'name3'), Client(4, 'name4')]
        self.assertEqual(self.serv_client.get_all_clients(), list_clients)

    def test_search_client_by_id(self):
        self.assertEqual(self.serv_client.search_client_id('1'), [Client(1, 'name1')])
        with self.assertRaises(ServiceException):
            self.serv_client.search_client_id('-5')

    def test_search_client_by_name(self):
        self.assertEqual(self.serv_client.search_client_name('name1'), [Client(1, 'name1')])
        with self.assertRaises(ServiceException):
            self.serv_client.search_client_name('')


class TestServiceRental(unittest.TestCase):
    def setUp(self):
        self.val_rental = ValidatorRental()
        self.repo_rental = RepositoryRental()
        self.repo_book = RepositoryBook()
        self.repo_client = RepositoryClient()
        self.repo_book.add_book(Book(1, 'title1', 'author1'))
        self.repo_book.add_book(Book(2, 'title2', 'author2'))
        self.repo_book.add_book(Book(3, 'title3', 'author3'))
        self.repo_client.add_client(Client(1, "name1"))
        self.repo_client.add_client(Client(2, "name2"))
        self.repo_client.add_client(Client(3, "name3"))
        self.repo_client.add_client(Client(4, "name4"))
        self.serv_rental = ServiceRental(self.val_rental, self.repo_rental, self.repo_book, self.repo_client)
        self.serv_rental.add_rental(1, 1, 1, '12.09.2003', '12.07.2005')
        self.serv_rental.add_rental(2, 1, 2, '12.09.2003', '12.07.2005')
        self.serv_rental.add_rental(3, 2, 3, '12.09.2020', '-')
        self.serv_rental.add_rental(4, 1, 4, '14.08.2004', '15.08.2004')

    def test_add_rental(self):
        self.assertEqual(len(self.serv_rental.get_all_rentals()), 4)
        self.serv_rental.add_rental(5, 3, 4, '12.09.2002', '-')
        self.assertEqual(self.serv_rental.get_all_rentals()[4], Rental(5, 3, 4, '12.09.2002', '-'))

    def test_get_all(self):
        my_list = [Rental(1, 1, 1, '12.09.2003', '12.07.2005'), Rental(2, 1, 2, '12.09.2003', '12.07.2005'),
                   Rental(3, 2, 3, '12.09.2020', '-'), Rental(4, 1, 4, '14.08.2004', '15.08.2004')]
        self.assertEqual(self.serv_rental.get_all_rentals(), my_list)

    def test_return_book(self):
        self.serv_rental.return_book(3, '15.09.2020')
        self.assertEqual((self.serv_rental.get_all_rentals()[2]).get_returned_date(), '15.09.2020')

    def test_most_rented_book(self):
        aux_list = []
        aux_list12 = []
        my_list = self.serv_rental.most_rented_authors()
        for book in my_list:
            aux_list.append(book[1])
        self.assertEqual([3, 1], aux_list)

    def test_most_active_clients(self):
        aux_list = []
        my_list = self.serv_rental.most_active_clients()
        for client in my_list:
            aux_list.append(client[1])
        self.assertEqual([669, 669, 1, 0], aux_list)

    def test_most_rented_authors(self):
        aux_list = []
        my_list = self.serv_rental.most_rented_authors()
        for author in my_list:
            aux_list.append(author[1])
        self.assertEqual([3, 1], aux_list)

    def test_remove(self):
        self.serv_rental.remove_rental(1)
        self.assertEqual(len(self.serv_rental.get_all_rentals()), 3)
        with self.assertRaises(RepositoryException):
            self.serv_rental.remove_rental('5')






