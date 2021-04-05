# ASSIGNMENT 3
"""
    During a programming contest, each contestant had to solve 3 problems (named P1, P2 and P3).
    Afterwards, an evaluation committee graded the solutions to each of the problems using integers between 0 and 10.
    The committee needs a program that will allow managing the list of scores and establishing the winners.
    Write a program that implements the functionalities exemplified below:

    (A) Add the result of a new participant (add, insert)
    (B) Modify scores (remove, remove between two postion, replace the score obtained by a certain participant at a
                       certain problem with other score obtained by other participant)
    (C) Display participants whose score has different properties. """


def get(list, position):
    """ The function will extract a certain element from a list."""
    return list[int(position)]


def set(list, element, position):
    """ The functin will set a certain element from a list.
   :param list: [ ['2', '4', '8'], ['3', '5', '6'], ['10', '4', '6'], ['9', '3', '2'], ['10', '10', '10'] ]
   :param element: ['5', '8', '9']
   :param position: 1
   :return: [ ['2', '4', '8'], ['5', '8', '9'], ['10', '4', '6'], ['9', '3', '2'], ['10', '10', '10']
   """
    list.insert(int(position), element)
    list.remove(get(list, int(position) + 1))


def make_a_list(sentence):
    """ The function will make a list containing the given scores P1, P2 and P3 that are found in the command."""
    list_one_score = []
    for i in range(1, 4):
        list_one_score.append(sentence[i])
    return list_one_score


def add_scores(list, sentence):
    """ The function will add to the principal list (with all the scores of all the participants) a list with the
    scores of just one participant.
    """
    list.append(make_a_list(sentence))


def insert_scores(list, sentence, position):
    """ The function will insert in a given position to the principal list (with all the scores of all the participants)
     a list with the scores of just one participant
    """
    list.insert(int(position), make_a_list(sentence))


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
    set(list, new_score, int(problem[1]) - 1)


def calc_average(list):
    """ The function will calculate the average of all the integers from a list ( it will calculate the sum of al the
        integers, and then it will divide the sum by the value of the len of tne list)
    :param list: [ '2', '4', '3' ]
    :return: 3
    """
    result = 0
    for i in range(0, len(list)):
        result = result + int(get(list, i))
    return result / len(list)


def average_score_lesser(list, number):
    """ The function will display all the participants with an average score lesser than the given number.
    :param list: [['5', '8', '9'], ['10', '4', '6'], ['9', '3', '2'], ['10', '10', '10'], ['7', '8', '9']]
    :param number: 7
    :return:['10', '4', '6'], ['9', '3', '2']
    """
    l = []  # l is the required list
    for i in range(0, len(list)):
        if calc_average(get(list, i)) < number:
            l.append(get(list, i))
    return l


def average_score_equal(list, number):
    """ The function will display all the participants with an average score equal with the given number.
        :param list: [['5', '8', '9'], ['10', '4', '6'], ['9', '3', '2'], ['10', '10', '10'], ['7', '8', '9']]
        :param number: 8
        :return:['7', '8', '9']
        """
    l = []  # l is the required list
    for i in range(0, len(list)):
        if calc_average(get(list, i)) == number:
            l.append(get(list, i))
    return l


def average_score_greater(list, number):
    """ The function will return a list with all the participants with an average score greater than the given number.
       :param list: [['10', '4', '6'], ['9', '3', '2'], ['10', '10', '10'], ['7', '8', '9']]
       :param number: 7
       :return: [['10', '10', '10'], ['7', '8', '9']]
       """
    l = []  # l is the required list
    for i in range(0, len(list)):
        if calc_average(get(list, i)) > number:
            l.append(get(list, i))
    return l


def list_sorted(list):
    """ The function will return a list with participants sorted in decreasing order of average score
    :param list: [['5', '8', '9'], ['10', '4', '6'], ['10', '10', '10'], ['7', '8', '9'], ['10', '2', '9']]
    :return:    [['10', '10', '10'], , ['7', '8', '9'], ['5', '8', '9'], ['10', '2', '9'], ['10', '4', '6']]
    """
    l = []
    for i in range(0, len(list)):
        get(list, i).insert(0, calc_average(get(list, i)))
        l.append(get(list, i))

    l.sort(reverse=True)

    for i in range(0, len(l)):
        get(l, i)
        get(l, i).remove(get(get(l, i), 0))
    return l


def list(list, cmd):
    if len(cmd) == 1:
        l = list

    elif get(cmd, 1) == 'sorted':
        l = list_sorted(list)

    elif get(cmd, 1) == '<':

        l = average_score_lesser(list, int(get(cmd, 2)))

    elif get(cmd, 1) == '=':
        l = average_score_equal(list, int(get(cmd, 2)))

    elif get(cmd, 1) == '>':
        l = average_score_greater(list, int(get(cmd, 2)))

    print(l)


def print_menu():
    commands = ['add <P1 score> <P2 score> <P3 score>', 'insert <P1 score> <P2 score> <P3 score> at <position>',
                'remove <position>', 'remove <start position> to <end position>',
                'replace <position> <P1 | P2 | P3> with <new score>', 'list', 'list sorted', 'list [< | = | >] <score>']
    print("The possible comands are:")
    print(*commands, sep="\n")


def run_menu():
    list_participants_scores = [['5', '8', '9'], ['10', '4', '6'], ['9', '3', '2'], ['10', '10', '10'], ['7', '8', '9'],
                                ['8', '9', '10'], ['10', '2', '9'], ['2', '4', '6'], ['8', '2', '1'], ['0', '8', '4']]

    commands = ['add <P1 score> <P2 score> <P3 score>', 'insert <P1 score> <P2 score> <P3 score> at <position>',
                'remove <position>', 'remove <start position> to <end position>',
                'replace <position> <P1 | P2 | P3> with <new score>', 'list', 'list sorted', 'list [< | = | >] <score>']

    while True:
        comand = input()
        comand_splited = comand.split()
        first_word = get(comand_splited, 0)

        if first_word == 'add':  # The command is add P1, P2, P3
            add_scores(list_participants_scores, comand_splited)

        elif first_word == 'insert':  # The command is insert [P1, P2, P3] at position
            insert_scores(list_participants_scores, comand_splited, comand_splited[5])

        elif first_word == 'remove':
            remove(list_participants_scores, comand_splited)

        elif first_word == 'replace':  # The command is replace <old score> P1/P2/P3 with <new score>

            replace(get(list_participants_scores, int(get(comand_splited, 1))), get(comand_splited, 2),
                    (get(comand_splited, 4)))

        elif first_word == 'list':
            (list(list_participants_scores, comand_splited))

        else:
            print("Wrong command")
            break


if __name__ == '__main__':
    print_menu()
    run_menu()
