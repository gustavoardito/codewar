
"""
You have to create a function that takes a positive integer number and returns
the next bigger number formed by the same digits:
next_bigger(12)==21
next_bigger(513)==531
next_bigger(2017)==2071
If no bigger number can be composed using those digits, return -1:

next_bigger(9)==-1
next_bigger(111)==-1
next_bigger(531)==-1
TIP: run -> python -c 'import exercise; print exercise.next_bigger(5)'
"""
from itertools import permutations


def num_to_list(num):
    """return number as list"""
    return [int(c) for c in list(str(num))]


def list_to_num(lst):
    """join ponderate numbers"""
    exp = len(lst) - 1
    num = 0
    for val in lst:
        num += val * 10**exp
        exp -= 1
    return num


def get_permutations(num):
    """get perms"""
    perms = [list_to_num(p) for p in permutations(num)]
    return perms


def exclude_lowers(num, values):
    """filter list"""
    return [val for val in values if val > num]


def next_bigger(num):
    """return next bigger number"""
    num_list = num_to_list(num)
    results = get_permutations(num_list)
    filtered_results = exclude_lowers(num, results)

    if filtered_results:
        return min(filtered_results)
    return -1
