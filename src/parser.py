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

    def __str__(self):
        """Print the matrix in a readable format"""
        output = ""
        maxWidth = 1 + len(str(max([max(row) for row in self.rowArray])))
        for row in self.rowArray:
            for cell in row:
                output += ("{0:{width}}".format(cell, width=maxWidth, end=' '))
            output += "\n"
        return output[:-1]

    def getCell(self, row, col):
        """Return the content of the requested cell"""
        return self.rowArray[row - 1][col - 1]

    def getRow(self, row):
        """Return the requested row."""
        return self.rowArray[row - 1]

    def genColArray(self, col):
        """Generate only the requested column and store it in self.colArray.

       Generating only the needed column at a time keeps the worst case scenario
       at a reasonable O(m). As the same column vector is requested again,
       then getCol becomes O(1).
       """
        for i in range(self.rowAmount):
            self.colArray[col - 1][i] = self.rowArray[i][col - 1]
        return self.colArray[col - 1]

    def getCol(self, col):
        """Return the requested column of the matrix.

        If this is the first time requesting a column, the column must be first
        generated. Otherwise, we may just look the column up from self.colArray.
        """
        if len(self.colArray[col - 1]) == 0:
            self.genColArray(col)
        return self.colArray[col - 1]


def parseMatrix():
    """Ask user to input a matrix. Then, create a new Matrix object."""

    rows = []
    rowAmount = 0

    print("Input a matrix row by row. Plain enter stops.")
    row = raw_input("row: ")

    while row:
        try:
            newRow = [int(i) for i in row.split(" ")]
            if len(rows) > 0 and len(newRow) != len(rows[0]):
                raise SyntaxError
        except ValueError:
            print("You inputted a non number. Don't do that.")
            print("Please, input the row correctly.")
        except SyntaxError:
            print("You inputted an invalid amount of numbers.")
            print("Please, input the row correctly.")
        else:
            rows.append(newRow)
            rowAmount += 1
        row = raw_input("row: ").strip()
    return Matrix(rows, len(rows), len(rows[0]))


def parseOperator():
    """Ask user, which operation they would like to perform next."""

    print("Which operation you'd like to perform next?")
    print("Depending on your choice, you'll be asked to input another matrix.")
    print("")
    print("+: Add another matrix to the current one.")
    print("-: Substract another matrix from the current one.")
    print("*: Multiply current matrix with another matrix")
    print("det: calculate the determinant of the current matrix")
    print("")

    operator = raw_input("Operator: ").strip().lower()
    while operator not in ["*", "-", "+", "det"]:
        print("Please choose a valid operator.")
        operator = raw_input("Operator: ").strip().lower()

    return operator
