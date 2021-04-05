def filter_list(list, condition):
    returned_list = []
    for element in list:
        if condition(element) is True:  # ex: lambda x: title.casefold() in x.get_title().casefold()
            returned_list.append(element)
    return returned_list


def find_gap(gap):
    # Shrink gap by Shrink factor
    gap = (gap * 10)//13
    if gap < 1:
        return 1
    return gap

def comb_sort(array, condition):
    n = len(array)
    gap = n
    swapped = True
    # the program will continue while gap is more than 1 and last iteration caused a swap
    while gap != 1 or swapped is True:
        gap = find_gap(gap)
        # Initialize swapped as false so that we can
        # check if swap happened or not
        swapped = False  # if there will be no swaps, swapped will remain false
        # Compare all elements with current gap
        for i in range(0, n - gap):
            if condition(array[i], array[i + gap]):
                array[i] = array[i + gap]
                array[i + gap] = array[i]
                swapped = True


class IterableData:
    def __init__(self):
        self.__iterable_data = []

    def __setitem__(self, index, new_data):
        self.__iterable_data[index] = new_data

    def __getitem__(self, index):
        return self.__iterable_data[index]

    def __delitem__(self, index):
        del self.__iterable_data[index]

    def __iter__(self):
        for element in self.__iterable_data:
            yield element

    def __len__(self):
        return len(self.__iterable_data)

    def append(self, new_data):
        self.__iterable_data.append(new_data)

