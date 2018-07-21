#    Copyright © 2016 Marcus Leivo
#
#    This file is part of Matrix-Calculator.
#
#    Matrix-Calculator is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Matrix-Calculator is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Matrix-Calculator. If not, see <https://www.gnu.org/licenses/>.


from .parser import parseMatrix, parseOperator, parseScalar, askToContinue
from .calculator import *
import sys

# Make this module python2 compatible.
if sys.version_info[0] == 2:
    input = raw_input


def __handle_operator(operator, matrix):
    """Perform user given operation on user given matrix."""

    # User wants to calculate the determinant.
    if operator == "det":
        ans = matrixDeterminant(matrix)
        if ans != 0 and not ans:
            print("Determinant not defined for the given matrix.")
        else:
            print("The determinant is: " + str(ans))

    # User wants to calculate the inverse.
    if operator == "inverse" or operator == "-1":
        matrix2 = matrixInverse(matrix)
        if not matrix2:
            print("Matrix not invertible.")
        else:
            matrix = matrix2
            print("Inversion successful.")

    # User wants to multiply the matrix by a scalar.
    if operator == "scalar":
        n = parseScalar()
        matrix.multiplyScalar(n)
        print("Scalar multiplication successful.")

    # User wants to calculate the transpose
    if operator == "transpose":
        matrix = matrixTranspose(matrix)
        print("Calculating the transpose successful.")

    # User wants to add two matrices.
    if operator == "+":
        matrix2 = parseMatrix()

        # This will be None if addition is not possible.
        resultMatrix = matrixAddition(matrix, matrix2)

        if not resultMatrix:
            print("Matrix addition failed.")
        else:
            matrix = resultMatrix
            print("Matrix addition successful.")

    # User wants to substract two matrices.
    if operator == "-":
        matrix2 = parseMatrix()
        resultMatrix = matrixSubstraction(matrix, matrix2)
        if not resultMatrix:
            print("Matrix substraction failed.")
        else:
            matrix = resultMatrix
            print("Matrix substraction successful.")

    # User wants to multiply two matrices.
    if operator == "*":
        matrix2 = parseMatrix()
        resultMatrix = matrixMultiplication(matrix, matrix2)
        if not resultMatrix:
            print("Matrix multiplication failed.")
        else:
            matrix = resultMatrix
            print("Matrix multiplication successful.")

    # Print the result matrix to user.
    print(matrix)
    return matrix


def main():
    """Wrap all things together."""

    # Ask 1st matrix.
    matrix = parseMatrix()

    # Perform matrix operations. Stop when no matrix is None
    while matrix:
        # Ask which operation the user wants to perform (multiplication,
        # determinant, inverse etc.)
        operator = parseOperator()

        # Perform the operation on matrix.
        matrix = __handle_operator(operator, matrix)

        userWantsToContinueWithCurrentMatrix = askToContinue()
        if not userWantsToContinueWithCurrentMatrix:
            # Ask for a new matrix. If user inputs no rows, matrix is None and
            # the program will halt.
            matrix = parseMatrix()

    print("")
    print("Bye!")
