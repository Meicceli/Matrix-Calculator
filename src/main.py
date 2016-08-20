from .parser import parseMatrix, parseOperator, parseScalar, askToContinue
from .calculator import *
import sys

if sys.version_info[0] == 2:
    input = raw_input


def __handle_operator(operator, matrix):
    """Perform user given operation on user given matrix."""
    if operator == "det":
        ans = matrixDeterminant(matrix)
        if not (isinstance(ans, float) or isinstance(ans, int)):
            print("Determinant not defined for given matrix.")
        else:
            print("The determinant is: " + str(ans))

    if operator == "inverse" or operator == "-1":
        matrix2 = matrixInverse(matrix)
        if not matrix2:
            print("Matrix not invertible.")
        else:
            matrix = matrix2
            print("Inversion successful.")

    if operator == "scalar":
        n = parseScalar()
        matrix.multiplyScalar(n)
        print("Scalar multiplication successful.")

    if operator == "+":
        matrix2 = parseMatrix()
        matrix = matrixAddition(matrix, matrix2)
        print("Matrix addition successful.")

    if operator == "-":
        matrix2 = parseMatrix()
        matrix = matrixSubstraction(matrix, matrix2)
        print(matrix2.scalar)
        print("Matrix substraction successful.")

    if operator == "*":
        matrix2 = parseMatrix()
        matrix = matrixMultplication(matrix, matrix2)
        print("Matrix multiplication successful.")

    print(matrix)
    return matrix


def main():
    """Wrap all things together.

    Currently supports only one operation per run."""

    matrix = parseMatrix()

    while matrix:
        operator = parseOperator()
        matrix = __handle_operator(operator, matrix)

        userWantsToContinueWithCurrentMatrix = askToContinue()
        if not userWantsToContinueWithCurrentMatrix:
            matrix = parseMatrix()

    print("")
    print("Bye!")


if __name__ == '__main__':
    main()
