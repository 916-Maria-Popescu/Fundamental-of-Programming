import random


def random_book():
    books = [['Umberto Eco', 'Numele trandafirului'], ['Fyodor Dostoevsky', 'Crime and Punishment'],
             ['Erich Maria Remarque', 'Soroc de viata si soroc de moarte'], ['Boualem Sansal', 'Satul Neamtului'],
             ['Fyodor Dostoevsky', 'Idiotul'], ['Nicolas Bouvier', 'Cronica Japoneza'],
             ['André Gide', 'Les Faux-monnayeurs'],
             ['Hermann Hesse', 'Narcis si Gura-de-Aur'], ['André Gide', 'Les Faux-monnayeurs'],
             ['Marin Preda', 'Cel mai iubit dintre pamanteni'],
             ['J. D. Salinger', 'Franny and Zooey'], ['Tom Hanks', 'Caractere atipice'],
             ['Pisica Cara', 'Miau Miau'], ['Crabul Clachi', 'Clac Clac'], ['Cezar Petrescu', 'Fram, ursul polar'],
             ['Marin Sorescu', 'Trei diniti din fata'], ['A.E. Baconsky', 'Biserica Neagra'],
             ['Hermann Hesse', 'Jocul cu margele de sticla']]

    book = random.choice(books)
    return random.randint(10, 99), book[1], book[0]


def random_client():
    clients = ['Alex', 'Alexandra', 'Adriana', 'Adrian', 'Maria', 'Marian', 'Bianca', 'Mihai', 'Mihaela', 'Andrei',
               'Andreea', 'Miruna', 'Liliana', 'Diana', 'Daniel', 'Daniela', 'George', 'Georgiana', 'Ionut']
    id_client = random.randint(10, 99)
    client_name = random.choice(clients)
    return id_client, client_name


def random_rental():
    id_rental = random.randint(10, 99)
    id_book = random.randint(10, 99)
    id_client = random.randint(0, 20)
    rented_date = '{0}.{1}.{2}'.format(random.randint(1, 31), random.randint(1, 12), random.randint(2015, 2017))
    returned_date = '{0}.{1}.{2}'.format(random.randint(1, 31), random.randint(1, 12), random.randint(2018, 2020))
    return id_rental, id_book, id_client, rented_date, returned_date


