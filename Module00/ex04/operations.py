import sys

usage = "Usage: python operations.py <number1> <number2>\n\
Example:\n\tpython operations.py 10 3"


def is_intstring(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "ERROR (div by zero)"


def mod(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        return "ERROR (modulo by zero)"


def elementary(x, y):
    return x + y, x - y, x * y, div(x, y), mod(x, y)


if (len(sys.argv) == 1):
    sys.exit(usage)

if (len(sys.argv) > 3):
    print("InputError: too many arguments\n")
    sys.exit(usage)

if not is_intstring(sys.argv[1]) or not is_intstring(sys.argv[2]):
    print("InputError: only numbers\n")
    sys.exit(usage)

op = elementary(int(sys.argv[1]), int(sys.argv[2]))

print("Sum:\t\t{0}\n\
Difference:\t{1}\n\
Product:\t{2}\n\
Quotient:\t{3}\n\
Remainder:\t{4}".format(*op))
