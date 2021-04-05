"""
1. A number of `n` coins are given, with values of a<sub>1</sub>, ..., a<sub>n</sub>  and a value `s`.
  Display all payment modalities for the sum `s`. If no payment modality exists print a message.

"""


def function(price, coins):
    correct_combination = []
    for coin in coins:
        if coin == price:
            #if the value of the coin is equal to the price, the only correct combination with that coin is itself
            correct_combination.append([coin])
            coins.remove(coin)

        elif coin > price:
            #if the value of that coin is greater than the price, there is no correct combination with that coin
            coins.remove(coin)

    # now the list <coins> will contain only the coins with the value lesser then the price
    return coins

def backtracking_iterable(price, mylist):
    correct_combination = []
    mysum = 0  # sum is the sum of the coins at one point
    i = 0    # i is used for iteration in a branch
    j = 0    # the number of main branches
    lenlist = len(mylist)
    while j < lenlist:
        branch_list = mylist.copy()

        while i < len(branch_list):
            print(mysum, i, price)
            while mysum < price:  # it creates new branches
                #mytuple = (sum, mylist)
                mysum = mysum + branch_list[i]
                i = i + 1
            if mysum == price:
                # if the sum of the coins is equal to the price, we'll add all the coins that forms that sum in a list
                # and that list will be added to the list with correct results
                correct_list = []
                for aux in range(0, i):
                    correct_list.append(branch_list[aux])
                correct_combination.append(correct_list)
            else:
                # if the sum is greater, we dont need to search further in this combination
                # the last coin will bw deleted and e will return tu the sum before adding the last coin

                i = i - 1
                mysum = mysum - mylist[i]
                branch_list.remove(branch_list[i])
        mylist.remove(mylist[j])
        j = j +1

    return correct_combination[:]

def recursive_backtracking(set, num):

    
    if num < 0:
        return
    if len(set) == 0:
        if num == 0:
            yield []
        return
    for solution in recursive_backtracking(set[1:], num):
        yield solution
    for solution in recursive_backtracking(set[1:], num - set[0]):
        yield [set[0]] + solution


if __name__ == '__main__':
    myset = [3, 5, 7, 10, 9, 1, 4, 3, 2, 0]
    num = 5
    mylist = list(recursive_backtracking(myset, num))
    for el in mylist:
        print(el)