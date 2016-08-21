from .myAlgorithms import my_max, my_range
import sys

# Make everything here work with python2.
if sys.version_info[0] == 2:
    input = raw_input


class Matrix:
    """Matrix object"""

    def __init__(self, rows, n, m):
        """Construct matrix

        Keyword arguments:
        rows -- the list of rows in the matrix
        n    -- the number of rows in the matrix
        m    -- the number of column in the matrix
        """
        self.rowAmount = n
        self.colAmount = m
        self.rowArray = rows
        self.colArray = [[] for i in my_range(n)]
        self.scalar = 1

    def __str__(self):
        """Print the matrix in a readable format"""
        output = ""
        # maxWidth is the 1 + length of the longest number in rowArray. It is
        # needed for neater printing.
        maxWidth = 1 + my_max([my_max([len(str(i * self.scalar)) for i in row])
                               for row in self.rowArray])
        for row in self.rowArray:
            # Beginning of a row
            output += "["
            for cell in row:
                elem = self.scalar * cell
                # Make sure each value takes space exactly the amount of
                # maxWidth.
                output += ("{0:{width}}".format(elem, width=maxWidth, end=' '))
            # Ending of a row
            output += "]\n"
        return output[:-1]

    def multiplyScalar(self, n):
        """Multiply the current scalar value.

        self.scalar handles the scalar multiplication of the matrix. Each time
        a value(s) is returned via a getter, the returned values have to be
        multiplied by the scalar.
        """
        self.scalar *= n

    def getRowAmount(self):
        """Return the amount of rows.

        This is needed mainly for testing purposes."""
        return self.rowAmount

    def getRowArray(self):
        """Return the row array.

        This is needed mainly for testing purposes."""
        if self.scalar == 1:
            return self.rowArray
        returnArray = [[self.scalar * elem for elem in row]
                       for row in self.rowArray]
        return returnArray

    def getColAmount(self):
        """Return the amount of columns.

        This is needed mainly for testing purposes."""
        return self.colAmount

    def getColArray(self):
        """Return the current column array.

        This is needed mainly for testing purposes"""
        return self.colArray

    def getScalar(self):
        """Return the current scalar value.

        This is needed mainly for testing purposes"""
        return self.scalar

    def getCell(self, row, col):
        """Return the content of the requested cell"""
        return self.scalar * self.rowArray[row][col]

    def getRow(self, row):
        """Return the requested row."""
        if self.scalar == 1:
            return self.rowArray[row]

        returnRow = [self.scalar * elem for elem in self.rowArray[row]]
        return returnRow

    def genColArray(self, col):
        """Generate only the requested column and store it in self.colArray.

       Generating only the needed column at a time keeps the worst case scenario
       at a reasonable O(m). As the same column vector is requested again,
       then getCol becomes O(1).
       """
        for i in my_range(self.rowAmount):
            self.colArray[col].append(self.rowArray[i][col])
        return self.colArray[col]

    def getCol(self, col):
        """Return the requested column of the matrix.

        If this is the first time requesting a column, the column must be first
        generated. Otherwise, we may just look the column up from self.colArray.
        """
        if len(self.colArray[col]) == 0:
            self.genColArray(col)

        if self.scalar == 1:
            return self.colArray[col]

        returnCol = [self.scalar * elem for elem in self.colArray[col]]
        return returnCol


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
        return

    # Loop until an empty row is encountered.
    while row:
        try:
            newRow = [int(i) for i in row.split(" ")]
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
            row = input("row: ").strip()
        except KeyboardInterrupt:
            print("\nBye!")
            return

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
    print("det: Calculate the determinant of the current matrix.")
    print("inverse: Invert the given matrix if possible.")
    print("scalar: Multiply the current matrix by a scalar.")
    print("print: Print the current matrix.")

    print("")

    # Handle possible Ctrl-c
    try:
        operator = input("Operator: ").strip().lower()
    except KeyboardInterrupt:
        print("")
        print("Bye!")
        return
    while operator not in ["*",
                           "-",
                           "+",
                           "det",
                           "scalar",
                           "inverse",
                           "invert",  # Alternative inputs for inversion.
                           "-1",      #
                           "print"]:
        print("Please choose a valid operator.")
        # Handle possible Ctrl-c
        try:
            operator = input("Operator: ").strip().lower()
        except KeyboardInterrupt:
            print("\nBye!")
            return

    return operator


def __isNumber(n):
    """Find out if a given argument is a number or not."""
    try:
        float(n)
        return True
    except:
        return False


def parseScalar():
    """Ask a scalar multiplicator from user."""
    print("")
    try:
        scalar = input("Input a scalar value: ")
    except KeyboardInterrupt:
        print("\nBye!")
        return
    while not __isNumber(scalar):
        try:
            scalar = input("Input a proper scalar value: ")
        except KeyboardInterrupt:
            print("\nBye!")
            return
    return int(scalar)


def askToContinue():
    print("")
    print("Do you want to apply more options to the current matrix?")
    try:
        a = input("Y/N: ")
    except KeyboardInterrupt:
        print("\nBye!")
        return
    print("")

    if a.lower() == "y":
        return True

    return False
