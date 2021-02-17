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


def nine(operation=None):
    return _build_result(9, operation)


def _build_result(a_value, operation):
    return a_value if operation is None else operation(a_value)


def plus(y): return lambda x: x+y


def minus(y): return lambda x: x-y


def times(y): return lambda x: x*y


def divided_by(y): return lambda x: x//y


print(seven(plus(one())))
