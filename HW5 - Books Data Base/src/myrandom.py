import random


def random_book():
    books = [['Umberto Eco', 'Numele trandafirului'], ['Fyodor Dostoevsky', 'Crime and Punishment'],
             ['Erich Maria Remarque', 'Soroc de viata si soroc de moarte'],['Boualem Sansal', 'Satul Neamtului'],
             ['Fyodor Dostoevsky', 'Idiotul'], ['Nicolas Bouvier', 'Cronica Japoneza'], ['André Gide', 'Les Faux-monnayeurs'],
             ['Hermann Hesse', 'Narcis si Gura-de-Aur'], ['André Gide', 'Les Faux-monnayeurs'], ['Marin Preda', 'Cel mai iubit dintre pamanteni'],
             ['J. D. Salinger', 'Franny and Zooey'], ['Maria Popescu', 'a very good book by un yet unknown artist'],
             ['Pisica Cara', 'Miau Miau'], ['Crabul Clachi', 'Clac Clac']]
    a = random.choice(books)
    return a


def random_isbn():
    a = ['978', '979']
    m1 = random.choice(a)
    m2 = random.randint(10, 99)
    m3 = random.randint(10000, 99999)
    m4 = random.randint(10, 99)
    m5 = random.randint(0, 9)
    isbn = ("{0}-{1}-{2}-{3}-{4}").format(m1, m2, m3, m4, m5)
    return isbn
