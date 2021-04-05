
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

    nums = [4, 2, 4, 2, 5, 2, 1, 3, 3]
    max_sum = 9
    result = recursive_backtracking(nums, max_sum)
    print(*result)