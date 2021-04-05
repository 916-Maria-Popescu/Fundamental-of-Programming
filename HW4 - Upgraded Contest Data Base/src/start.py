"""
Assemble the program and start the user interface here
"""
## Write the implementation for A3 in this file

# domain section is here (domain = numbers, transactions, expenses, etc.)
def get(list, position):
    """ The function will extract a certain element from a list."""
    return list[int(position)]

def set(list, element, position):
   """ The functin will set a certain element from a list."""
   list.insert(int(position), element)
   list.remove(get(list, int(position)+1))


# Functionalities section (functions that implement required features)
def make_a_list(cmd):
    """ The function will make a list containing the given scores P1, P2 and P3 that are found in the command.
    :param sentence: Add 7 8 9
    :return: ['7', '8', '9']
    """
    list_one_score = []
    for i in range(1, 4):
        list_one_score.append(cmd[i])
    return list_one_score

def add_scores(list, cmd):
    """ The function will add to the principal list (with all the scores of all the participants) a list with the
    scores of just one participant.
    """
    list.append(make_a_list(cmd))

def insert_scores(list, cmd):
    """ The function will insert in a given position to the principal list (with all the scores of all the participants)
     a list with the scores of just one participant
    """
    list.insert(int(get(cmd,5)), make_a_list(cmd))

def remove_one_part(list, position):
    """ The function will set the scores of the participant at a given position to 0.
        So that, the participant <position> score P1=P2=P3= 0. """

    nul_element = ['0', '0', '0']
    set(list, nul_element, position)

def remove_more_part(list, first_position, last_position):
    """ The function will set the scores of all the participants between the first position and last position to 0.
       For all the participants between <first_position> and <last_position>, P1=P1=P3= 0 """

    nul_element = ['0', '0', '0']
    for i in range(int(first_position), int(last_position) + 1):
        set(list, nul_element, i)

def remove(list, cmd):
    if len(cmd) == 2:  # The command is remove <position>
        remove_one_part(list, get(cmd, 1))

    elif len(cmd) == 4:  # The command is remove <first pos> to <last pos>
        remove_more_part(list, get(cmd, 1), get(cmd, 3))

def replace(list, problem, new_score):
    """ The function will replace a score obtained by a participant at a specific problem with a new score.
        List represents the list with the scores of a participant, where <problem> ( P1/P2/P3 ) will recive a new score
    """
    set(list, new_score, int(problem[1])-1)

def calc_average(list):
    """ The function will calculate the average of all the integers from a list ( it will calculate the sum of al the
        integers, and then it will divide the sum by the value of the len of tne list)
    :param list: [ '2', '4', '3' ]
    :return: 3
    """
    result = 0
    for i in range(0, len(list)):
        result = result + int(get(list, i))
    return result/len(list)

def average_score_lesser(list, number):
    """ The function will display all the participants with an average score lesser than the given number.
    """
    l = []   # l is the required list
    for i in range(0, len(list)):
        if calc_average(get(list, i)) < number:
           l.append(get(list, i))
    return l

def average_score_equal(list, number):
    """ The function will display all the participants with an average score equal with the given number."""
    l = []    # l is the required list
    for i in range(0, len(list)):
        if calc_average(get(list, i)) == number:
            l.append(get(list, i))
    return l

def average_score_greater(list, number):
    """The function will return a list with all the participants with an average score greater than the given number."""
    l = []  # l is the required list
    for i in range(0, len(list)):
        if calc_average(get(list, i)) > number:
            l.append(get(list, i))
    return l

def list_sorted(list):
    """The function will return a list with participants sorted in decreasing order of average score"""
    l = []# l is the required list
    for i in range(0, len(list)):
        get(list, i).insert(0, calc_average(get(list, i)))
        l.append(get(list, i))

    l.sort(reverse=True)

    for i in range(0, len(l)):
        get(l, i)
        get(l, i).remove(get(get(l, i), 0))
    return l

# UI section
def list (list, cmd):
    l = []# l is the required list
    if len(cmd) == 1:
        l = list # the command is print list
    elif get(cmd, 1) == 'sorted':
         l = list_sorted(list)
    elif get(cmd, 1) == '<': # the command is print the list with the participants whose average score is < nr
        l = average_score_lesser(list, int(get(cmd, 2)))
    elif get(cmd, 1) == '=': # the command is print the list with the participants whose average score is = nr
        l = average_score_equal(list, int(get(cmd, 2)))
    elif get(cmd,1) == '>': # the command is print the list with the participants whose average score is > nr
        l = average_score_greater(list, int(get(cmd, 2)))
    print("The required participants are:")
    for i in range (0, len(l)):
        print ("Participant", i+1, ":", get(l, i))

def print_menu():
    commands = [' add <P1 score> <P2 score> <P3 score>', ' insert <P1 score> <P2 score> <P3 score> at <position>',
                ' remove <position>', ' remove <start position> to <end position>',
                ' replace <position> <P1 | P2 | P3> with <new score>', ' list', ' list sorted', ' list [< | = | >] <score>']
    print("The possible commands are:")
    print(*commands, sep="\n")

def run_menu():
    list_participants_scores = [['5', '8', '9'], ['10', '4', '6'], ['9', '3', '2'], ['10', '10', '10'], ['7', '8', '9'],
                                ['8', '9', '10'], ['10', '2', '9'], ['2', '4', '6'], ['8', '2', '1'], ['0', '8', '4']]
    while True:
        command = input("Enter the command: ")
        command_splited = command.split()
        first_word = get(command_splited, 0)

        if first_word == 'add':  # The command is add P1, P2, P3
            add_scores(list_participants_scores, command_splited)

        elif first_word == 'insert':  # The command is insert [P1, P2, P3] at position
            insert_scores(list_participants_scores, command_splited)

        elif first_word == 'remove':
            remove(list_participants_scores, command_splited)

        elif first_word == 'replace':  # The command is replace <old score> P1/P2/P3 with <new score>

            replace(get(list_participants_scores, int(get(command_splited, 1))), get(command_splited, 2),
                    (get(command_splited, 4)))

        elif first_word == 'list':
            (list(list_participants_scores, command_splited))

        else:
            raise NameError


# Test functions go here
def test_make_a_list():

    assert make_a_list(['add', '3', '4', '5']) == ['3', '4', '5']

def test_add_scores():

    l = [['1', '2', '3']]
    add_scores(l, ['add', '3', '4', '5'])
    assert l == [['1', '2', '3'], ['3', '4', '5']]

def test_insert():

    l = [['5', '8', '9'], ['10', '4', '6']]
    insert_scores(l, ['insert', '0', '0', '0', 'at', '0'])
    assert l == [['0', '0', '0'], ['5', '8', '9'], ['10', '4', '6']]

def test_remove_one_part():

    l = [['1', '2', '3']]
    remove_one_part(l,0)
    assert l == [['0', '0', '0']]

def test_remove_more_part():

    l = [['5', '8', '9'], ['10', '4', '6']]
    remove_more_part(l, 0, 1)
    assert l == [['0', '0', '0'], ['0', '0', '0']]

def test_calc_average():

    assert calc_average([ '2', '4', '3' ]) == 3

def test_average_score_equal():

    l = [['1', '1', '1'], ['0', '0', '6'], ['10', '10', '10']]
    assert average_score_equal(l, 10) == [['10', '10', '10']]

def test_average_score_lesser():

    l = [['1', '1', '1'], ['0', '0', '6'], ['10', '10', '10']]
    assert average_score_lesser(l, 2) == [['1', '1', '1']]

def test_average_score_greater():

    l = [['1', '1', '1'], ['0', '0', '6'], ['10', '10', '10']]
    assert average_score_greater(l, 9) == [['10', '10', '10']]

def test_list_sorted():

    l = [['1', '1', '1'], ['0', '0', '6'], ['10', '10', '10']]
    assert list_sorted(l) == [['10', '10', '10'], ['0', '0', '6'], ['1', '1', '1']]

def test_all():
    test_make_a_list()
    test_insert()
    test_add_scores()
    test_remove_one_part()
    test_remove_more_part()
    test_calc_average()
    test_list_sorted()
    test_average_score_greater()
    test_average_score_lesser()
    test_average_score_equal()


if __name__ == '__main__':

    test_all()
    print('Hello A3')
    print_menu()
    while True:
         try:
             run_menu()
         except NameError:
             print ("Wrong command!")


