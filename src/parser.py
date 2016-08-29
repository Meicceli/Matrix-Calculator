from .my_algorithms import my_split, my_strip, my_lower
from .calculator import frac_reduc
from .Matrix import Matrix
import sys

# Make everything here work with python2.
if sys.version_info[0] == 2:
    input = raw_input


def parseMatrix():
    """Ask user to input a matrix. Then, create a new Matrix object."""

    rows = []
    rowAmount = 0

    print("")
    print("Input a matrix row by row. Plain enter stops.")

    # Handle possible Ctrl-c
    try:
        row = input("row: ")
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)

    # Loop until an empty row is encountered.
    while row:
        try:
            newRow = []
            args = my_split(row, " ")
            for i in range(len(args)):
                elem = my_split(args[i], "/")
                # elem is not a fraction
                if len(elem) == 1:
                    elem = my_split(args[i], ".")
                    # elem is not a float (e.g. it is not 23.0329857)
                    if len(elem) == 1:
                        newRow.append((int(elem[0]), 1))
                        continue
                    # elem is a float
                    if len(elem) == 2:
                        numerator = int(elem[0]+elem[1])
                        numerator *= 10 ** (len(elem[1]) - 1)
                        denominator = 10 ** len(elem[1])
                        frac = frac_reduc((numerator, denominator))
                        newRow.append(frac)
                        continue
                    # I don't know what the heck elem is
                    if len(elem) > 2:
                        raise ValueError
                # elem is a fraction
                if (len(elem) == 2):
                    numerator = int(elem[0])
                    denominator = int(elem[1])
                    newRow.append(frac_reduc((numerator, denominator)))
                    continue
                # I don't know what the heck elem is
                if len(elem) > 2:
                    raise ValueError
            # User gives more values than there is in the first row.
            if len(rows) > 0 and len(newRow) != len(rows[0]):
                raise SyntaxError
        # User inputs a non-number.
        except ValueError:
            print("")
            print("You inputted a non-number. Don't do that.")
            print("Please, input the row correctly.")
        except SyntaxError:
            print("")
            print("You inputted an invalid amount of numbers.")
            print("Please, input the row correctly.")
        # If user inputs a row correctly, add it to the rows array.
        else:
            rows.append(newRow)
            rowAmount += 1

        # Handle possible Ctrl-c
        try:
            row = my_strip(input("row: "))
        except KeyboardInterrupt:
            print("\nBye!")
            sys.exit(0)

    # No rows given.
    if len(rows) == 0:
        return None

    return Matrix(rows, len(rows), len(rows[0]))


def parseOperator():
    """Ask user, which operation they would like to perform next."""

    print("")

    print("Which operation you'd like to perform next?")
    print("Depending on your choice, you'll be asked to input another matrix.")

    print("")

    print("+: Add another matrix to the current one.")
    print("-: Substract another matrix from the current one.")
    print("*: Multiply current matrix with another matrix.")
    print("det:       Calculate the determinant of the current matrix.")
    print("inverse:   Invert the given matrix if possible.")
    print("scalar:    Multiply the current matrix by a scalar.")
    print("transpose: Calculate the transpose")
    print("print:     Print the current matrix.")

    print("")

    # Handle possible Ctrl-c
    try:
        operator = my_lower(my_strip(input("Operator: ")))
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)
    while operator not in ["*",
                           "-",
                           "+",
                           "det",
                           "scalar",
                           "inverse",
                           "invert",  # Alternative inputs for inversion.
                           "-1",      #
                           "print",
                           "transpose"]:
        print("Please choose a valid operator.")
        # Handle possible Ctrl-c
        try:
            operator = my_lower(my_strip(input("Operator: ")))
        except KeyboardInterrupt:
            print("\nBye!")
            sys.exit(0)

    return operator


def __is_number(n):
    """Find out if a given argument is a number or not."""
    return isinstance(n, float) or isinstance(n, int)


def parseScalar():
    """Ask a scalar multiplicator from user."""
    print("")

    try:
        scalar = input("Input an integer scalar value: ")
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)

    # User must give an integer as a scalar.
    while not __is_number(scalar) or float(scalar) % 1 != 0:
        try:
            scalar = input("Input a proper integer scalar value: ")
        except KeyboardInterrupt:
            print("\nBye!")
            sys.exit(0)
    return int(scalar)


def askToContinue():
    """Ask the user to continue performing operations to the current matrix."""
    print("")
    print("Do you want to apply more options to the current matrix?")
    try:
        a = input("Y/N: ")
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)
    print("")

    # User wants to continue.
    if my_lower(a) == "y":
        return True

    # User does not want to continue.
    return False
