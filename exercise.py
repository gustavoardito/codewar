
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


def get_digit(num):
    """return 1st digit"""
    max_pow = len(str(num))
    if max_pow <= 1:
        return -1, 0
    ponderation = 10 ** (max_pow - 1)
    rest_part = num % ponderation
    main_number = num - rest_part
    return main_number / ponderation, rest_part


def create_number(num_list):
    """return number from digit list"""
    number = 0
    if num_list:
        max_pow = len(num_list) - 1
        for num in num_list:
            number += num * 10**max_pow
            max_pow -= 1
    return -1 if number == 0 else number


def next_bigger(num):
    """return next bigger number"""
    digits = []
    while True:
        first_digit, rest = get_digit(num)
        if first_digit == -1 or rest == 0:
            if digits:
                digits.append(num)
            break
        # print "{0} {1}".format(first_digit, rest)
        num = rest
        digits.append(first_digit)
    sorted_list = sorted(digits, reverse=True)
    if digits == sorted_list:
        return -1
    return create_number(sorted_list)
