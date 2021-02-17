# Calculating with Functions
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3

# Requirements:

#     There must be a function for each number from 0 ("zero") to 9 ("nine")
#     There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
#     Each calculation consist of exactly one operation and two numbers
#     The most outer function represents the left operand, the most inner function represents the right operand
#     Division should be integer division. For example, this should return 2, not 2.666666...:

# eight(divided_by(three()))

import inspect


NUMBERS = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

OPERATORS = {
    'plus',
    'minus',
    'times',
    'divided_by',
}


def zero(operator_tuple=None):
    return _build_result(0, operator_tuple)


def one(operator_tuple=None):
    return _build_result(1, operator_tuple)


def two(operator_tuple=None):
    return _build_result(2, operator_tuple)


def three(operator_tuple=None):
    return _build_result(3, operator_tuple)


def four(operator_tuple=None):
    return _build_result(4, operator_tuple)


def five(operator_tuple=None):
    return _build_result(5, operator_tuple)


def six(operator_tuple=None):
    return _build_result(6, operator_tuple)


def seven(operator_tuple=None):
    return _build_result(7, operator_tuple)


def eight(operator_tuple=None):
    return _build_result(8, operator_tuple)


def nine(operator_tuple=None):
    return _build_result(9, operator_tuple)


def _build_result(a_value, operator_tuple):
    if operator_tuple is None:
        return a_value
    operation, b_value = operator_tuple
    return operation(a_value, b_value)


def _sumar(a, b):
    return a + b


def _restar(a, b):
    return a - b


def _multiplicar(a, b):
    return a * b


def _dividir(a, b):
    return a // b


def plus(b_value):
    return (_sumar, b_value)


def minus(b_value):
    return (_restar, b_value)


def times(b_value):
    return (_multiplicar, b_value)


def divided_by(b_value):
    return (_dividir, b_value)


print(seven(plus(one())))
