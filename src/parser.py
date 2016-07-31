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
        self.colArray = [[] for i in range(m)]
        self.scalar = 1

    def __str__(self):
        """Print the matrix in a readable format"""
        output = ""
        maxWidth = 1 + len(str(self.scalar * max([max(row)
                                                  for row in self.rowArray])))
        for row in self.rowArray:
            output += "["
            for cell in row:
                elem = self.scalar * cell
                output += ("{0:{width}}".format(elem, width=maxWidth, end=' '))
            output += "]\n"
        return output[:-1]

    def multiplyScalar(self, n):
        """Multiply the current scalar value.

        self.scalar handles the scalar multiplication of the matrix. Each time
        a value(s) is returned via a getter, the returned values have to be
        multiplied by the scalar.
        """
        self.scalar *= n

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
        for i in range(self.rowAmount):
            self.colArray[col][i] = self.rowArray[i][col]
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
    row = raw_input("row: ")

    while row:
        try:
            newRow = [int(i) for i in row.split(" ")]
            if len(rows) > 0 and len(newRow) != len(rows[0]):
                raise SyntaxError
        except ValueError:
            print("")
            print("You inputted a non number. Don't do that.")
            print("Please, input the row correctly.")
        except SyntaxError:
            print("")
            print("You inputted an invalid amount of numbers.")
            print("Please, input the row correctly.")
        else:
            rows.append(newRow)
            rowAmount += 1
        row = raw_input("row: ").strip()
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
    print("scalar: Multiply the current matrix by a scalar.")

    print("")

    operator = raw_input("Operator: ").strip().lower()
    while operator not in ["*", "-", "+", "det", "scalar"]:
        print("Please choose a valid operator.")
        operator = raw_input("Operator: ").strip().lower()

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
    scalar = raw_input("Input a scalar value: ")
    while not __isNumber(scalar):
        scalar = raw_input("Input a proper scalar value: ")
    return int(scalar)
