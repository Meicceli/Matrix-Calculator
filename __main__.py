from src.parser import parseMatrix, parseOperator, parseScalar, askToContinue
from src.calculator import *


def __handle_operator(operator, matrix):
    """Perform user given operation on user given matrix."""
    if operator == "print":
        print(matrix)

    if operator == "det":
        ans = str(matrixDeterminant(matrix))
        print("The determinant is: " + ans)

    if operator == "inverse" or operator == "-1":
        matrix = matrixInverse(matrix)
        print("Inversion successful.")
        print(matrix)

    if operator == "scalar":
        n = parseScalar()
        matrix.multiplyScalar(n)
        print("Scalar multiplication successful.")
        print(matrix)

    if operator == "+":
        matrix2 = parseMatrix()
        matrix = matrixAddition(matrix, matrix2)
        print("Matrix addition successful.")
        print(matrix)

    if operator == "-":
        matrix2 = parseMatrix()
        matrix = matrixSubstraction(matrix, matrix2)
        print(matrix2.scalar)
        print("Matrix substraction successful.")
        print(matrix)

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


if __name__ == '__main__':
    main()
