from parser import parseMatrix, parseOperator, parseScalar
from calculator import *


def main():
    """Wrap all things together.

    Currently supports only one operation per run."""

    matrix = parseMatrix()
    operator = parseOperator()

    if operator == "det":
        print("The determinant is: " + matrixDeterminant(matrix))

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

main()
