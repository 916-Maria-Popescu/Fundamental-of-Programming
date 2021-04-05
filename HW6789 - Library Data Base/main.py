<<<<<<< HEAD

if __name__ == 'main':
    print ("a")
    tests = Tests()
    tests.run_all_tests()
    vBook = ValidatorBook()
    vClient = ValidatorClient()
    vRental = ValidatorRental()
    rBook = RepositoryBook()
    rClient = RepositoryClient()
    rRental = RepositoryRental()
    sBook = ServiceBook(vBook, rBook)
    sClient = ServiceClient (vClient, rClient)
    sRental = ServiceRental(vRental, rRental, rBook, rClient)
    cons = UI(sBook, sClient, sRental)
    cons.run()

=======
from Repository.myrepository import RepositoryBook, RepositoryClient, RepositoryRental
from Service.myservices import ServiceBook, ServiceClient, ServiceRental
#from Test.mytests import Test
from UI.myconsole import UI
from Validator.myvalidators import ValidatorBook, ValidatorClient, ValidatorRental

if __name__ == '__main__':
    #test = Test()
    #test.run_all_tests()
    vBook = ValidatorBook()
    rBook = RepositoryBook()
    sBook = ServiceBook(vBook, rBook)
    vClient = ValidatorClient()
    rClient = RepositoryClient()
    sClient = ServiceClient(vClient, rClient)
    vRental = ValidatorRental()
    rRental = RepositoryRental()
    sRental = ServiceRental(vRental, rRental, rBook, rClient)
    cons = UI(sBook, sClient, sRental)
    cons.run_console()
>>>>>>> 6e1d377e109c672b714e1ab86f355852700c6ac4
