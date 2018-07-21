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


# coding: utf-8
import unittest
import random
from src import calculator
from src import Matrix
from src.my_algorithms import my_gcd, my_abs, my_range, my_max, my_reversed
from src.my_algorithms import my_split, my_strip, my_lower


class TestMatrixCalculations(unittest.TestCase):

    def __random_n_by_m_array(self, n, m, lowerBound=0, upperBound=10):
        """Generate and return a n by m matrix with random values."""
        rows = []
        for row in range(n):
            newRow = []
            for col in range(m):
                newRow.append((random.randint(lowerBound, upperBound+1), 1))
            rows.append(newRow)
        return rows

    def __n_by_n_identity_matrix(self, n):
        """Generate and return an n by n identity matrix."""
        matrix = []
        for row in range(n):
            newRow = []
            for col in range(n):
                if row == col:
                    newRow.append((1, 1))
                else:
                    newRow.append((0, 1))
            matrix.append(newRow)
        return Matrix.Matrix(matrix, n, n)

    def __small_3x3_matrix1(self):
        """Return a simple 3x3 matrix."""
        matrix = Matrix.Matrix([[(1, 1), (2, 1), (3, 1)],
                                [(3, 1), (4, 1), (5, 1)],
                                [(4, 1), (5, 1), (6, 1)]], 3, 3)
        return matrix

    def __small_3x3_matrix2(self):
        """Return a simple 3x3 matrix."""
        matrix = Matrix.Matrix([[(1, 1), (0, 1), (1, 1)],
                                [(1, 1), (0, 1), (0, 1)],
                                [(0, 1), (0, 1), (1, 1)]], 3, 3)
        return matrix

    def __small_10x10_matrix1(self):
        """Matrix 0,..,99 from left to right, up-down"""
        matrix = [[] for i in range(10)]
        num = 0
        row = 0
        while row < 10:
            matrix[row].append((num, 1))
            num += 1
            if num % 10 == 0:
                row += 1
        return Matrix.Matrix(matrix, 10, 10)

    def __small_10x10_matrix2(self):
        """Matrix 100,...,1"""
        matrix = [[] for i in range(10)]
        num = 100
        row = 0
        while row < 10:
            matrix[row].append((num, 1))
            num -= 1
            if num % 10 == 0:
                row += 1
        return Matrix.Matrix(matrix, 10, 10)

    def test_small_matrix_addition_1(self):
        """Test small matrix addition."""
        resultMatrix = Matrix.Matrix([[(2, 1), (2, 1), (4, 1)],
                                      [(4, 1), (4, 1), (5, 1)],
                                      [(4, 1), (5, 1), (7, 1)]], 3, 3)
        matrix1 = self.__small_3x3_matrix1()
        matrix2 = self.__small_3x3_matrix2()
        self.assertEqual(
            str(calculator.matrixAddition(matrix1, matrix2)),
            str(resultMatrix))

    def test_small_matrix_addition_2(self):
        """Test small matrix addition."""
        resultMatrix = Matrix.Matrix([[(2, 1), (4, 1), (6, 1)],
                                      [(6, 1), (8, 1), (10, 1)],
                                      [(8, 1), (10, 1), (12, 1)]], 3, 3)
        matrix = self.__small_3x3_matrix1()
        self.assertEqual(str(calculator.matrixAddition(matrix, matrix)),
                         str(resultMatrix))

    def test_small_matrix_addition_3(self):
        """Test small matrix addition."""
        resultMatrix = Matrix.Matrix(
            [[(100, 1) for i in range(10)] for j in range(10)], 10, 10)
        matrix1 = self.__small_10x10_matrix1()
        matrix2 = self.__small_10x10_matrix2()
        self.assertEqual(str(calculator.matrixAddition(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_addition_4(self):
        """Test small matrix addition."""
        resultMatrix = [[(col+10*row, 1) for col in range(10)]
                        for row in range(10)]
        for j in range(10):
            resultMatrix[j][j] = calculator.frac_add(resultMatrix[j][j], (1, 1))
        resultMatrix = Matrix.Matrix(resultMatrix, 10, 10)
        matrix1 = self.__n_by_n_identity_matrix(10)
        matrix2 = self.__small_10x10_matrix1()
        self.assertEqual(str(calculator.matrixAddition(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_addition_5(self):
        """See what happens if we try adding the same matrix object to itself"""
        resultMatrix = Matrix.Matrix([[(2, 1), (0, 1), (2, 1)],
                                      [(2, 1), (0, 1), (0, 1)],
                                      [(0, 1), (0, 1), (2, 1)]], 3, 3)
        matrix = self.__small_3x3_matrix2()
        self.assertEqual(str(calculator.matrixAddition(matrix, matrix)),
                         str(resultMatrix))

    def test_small_matrix_addition_6(self):
        """See what happens if we try adding the same matrix object to itself"""
        resultMatrix = Matrix.Matrix([[(2, 1), (4, 1), (6, 1)],
                                      [(6, 1), (8, 1), (10, 1)],
                                      [(8, 1), (10, 1), (12, 1)]], 3, 3)
        matrix1 = self.__small_3x3_matrix1()
        self.assertEqual(str(calculator.matrixAddition(matrix1, matrix1)),
                         str(resultMatrix))

    def test_small_matrix_substraction_1(self):
        """Basic sanity test"""
        resultMatrix = Matrix.Matrix([[(0, 1), (2, 1), (2, 1)],
                                      [(2, 1), (4, 1), (5, 1)],
                                      [(4, 1), (5, 1), (5, 1)]], 3, 3)
        matrix1 = self.__small_3x3_matrix1()
        matrix2 = self.__small_3x3_matrix2()
        self.assertEqual(str(calculator.matrixSubstraction(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_substraction_2(self):
        """Basic sanity test"""
        resultMatrix = Matrix.Matrix([[(-0, 1), (-2, 1), (-2, 1)],
                                      [(-2, 1), (-4, 1), (-5, 1)],
                                      [(-4, 1), (-5, 1), (-5, 1)]], 3, 3)
        matrix1 = self.__small_3x3_matrix2()
        matrix2 = self.__small_3x3_matrix1()
        self.assertEqual(str(calculator.matrixSubstraction(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_substraction_3(self):
        """Test substraction when given matrixes are the same object."""
        resultMatrix = Matrix.Matrix([[(0, 1), (0, 1), (0, 1)],
                                      [(0, 1), (0, 1), (0, 1)],
                                      [(0, 1), (0, 1), (0, 1)]], 3, 3)
        matrix1 = self.__small_3x3_matrix1()
        self.assertEqual(str(calculator.matrixSubstraction(matrix1, matrix1)),
                         str(resultMatrix))

    def test_small_matrix_substraction_4(self):
        """Test substraction with just the 10x10 identity matrix"""
        resultMatrix = Matrix.Matrix(
            [[(0, 1) for i in range(10)] for j in range(10)], 10, 10)

        matrix1 = self.__n_by_n_identity_matrix(10)
        matrix2 = self.__n_by_n_identity_matrix(10)
        self.assertEqual(str(calculator.matrixSubstraction(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_substraction_5(self):
        """Test substraction with two different 10x10 matrices"""
        resultMatrix = Matrix.Matrix(
            [[(100 - 2 * (col + 10 * row), 1) for col in range(10)]
             for row in range(10)],
            10, 10)
        matrix1 = self.__small_10x10_matrix2()
        matrix2 = self.__small_10x10_matrix1()
        self.assertEqual(str(calculator.matrixSubstraction(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_substraction_6(self):
        """Test substraction with two different 10x10 matrices"""
        resultMatrix = Matrix.Matrix(
            [[(-100 + 2 * (col + 10 * row), 1) for col in range(10)]
             for row in range(10)],
            10, 10)
        matrix1 = self.__small_10x10_matrix1()
        matrix2 = self.__small_10x10_matrix2()
        self.assertEqual(str(calculator.matrixSubstraction(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_multiplication_1(self):
        """Test multiplying identity matrices together"""
        matrix1 = self.__n_by_n_identity_matrix(20)
        self.assertEqual(str(calculator.matrixMultiplication(matrix1, matrix1)),
                         str(matrix1))

    def test_small_matrix_multiplication_2(self):
        """Test multiplying two different matrices together"""
        resultMatrix = Matrix.Matrix([[(3, 1), (0, 1), (4, 1)],
                                      [(7, 1), (0, 1), (8, 1)],
                                      [(9, 1), (0, 1), (10, 1)]], 3, 3)
        matrix1 = self.__small_3x3_matrix1()
        matrix2 = self.__small_3x3_matrix2()
        self.assertEqual(str(calculator.matrixMultiplication(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_multiplication_3(self):
        """Test multiplying two different matrices together"""
        resultMatrix = Matrix.Matrix([[(5, 1), (7, 1), (9, 1)],
                                      [(1, 1), (2, 1), (3, 1)],
                                      [(4, 1), (5, 1), (6, 1)]], 3, 3)
        matrix1 = self.__small_3x3_matrix2()
        matrix2 = self.__small_3x3_matrix1()
        self.assertEqual(str(calculator.matrixMultiplication(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_multiplication_4(self):
        """Test multiplying two different matrices together"""
        resultMatrix = Matrix.Matrix(
            [[(1650, 1), (1605, 1), (1560, 1), (1515, 1), (1470, 1), (1425, 1), (1380, 1), (1335, 1), (1290, 1), (1245, 1)],
             [(7150, 1), (7005, 1), (6860, 1), (6715, 1), (6570, 1), (6425, 1), (6280, 1), (6135, 1), (5990, 1), (5845, 1)],
             [(12650, 1), (12405, 1), (12160, 1), (11915, 1), (11670, 1), (11425, 1), (11180, 1), (10935, 1), (10690, 1), (10445, 1)],
             [(18150, 1), (17805, 1), (17460, 1), (17115, 1), (16770, 1), (16425, 1), (16080, 1), (15735, 1), (15390, 1), (15045, 1)],
             [(23650, 1), (23205, 1), (22760, 1), (22315, 1), (21870, 1), (21425, 1), (20980, 1), (20535, 1), (20090, 1), (19645, 1)],
             [(29150, 1), (28605, 1), (28060, 1), (27515, 1), (26970, 1), (26425, 1), (25880, 1), (25335, 1), (24790, 1), (24245, 1)],
             [(34650, 1), (34005, 1), (33360, 1), (32715, 1), (32070, 1), (31425, 1), (30780, 1), (30135, 1), (29490, 1), (28845, 1)],
             [(40150, 1), (39405, 1), (38660, 1), (37915, 1), (37170, 1), (36425, 1), (35680, 1), (34935, 1), (34190, 1), (33445, 1)],
             [(45650, 1), (44805, 1), (43960, 1), (43115, 1), (42270, 1), (41425, 1), (40580, 1), (39735, 1), (38890, 1), (38045, 1)],
             [(51150, 1), (50205, 1), (49260, 1), (48315, 1), (47370, 1), (46425, 1), (45480, 1), (44535, 1), (43590, 1), (42645, 1)]],
            10, 10)
        matrix1 = self.__small_10x10_matrix1()
        matrix2 = self.__small_10x10_matrix2()
        self.assertEqual(str(calculator.matrixMultiplication(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_multiplication_5(self):
        """Test multiplying a matrix by the identity matrix"""
        resultMatrix = self.__small_10x10_matrix2()
        matrix1 = self.__n_by_n_identity_matrix(10)
        matrix2 = self.__small_10x10_matrix2()
        self.assertEqual(str(calculator.matrixMultiplication(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_multiplication_6(self):
        """Test multiplying by a zero matrix"""
        matrix1 = self.__small_10x10_matrix1()
        matrix2 = Matrix.Matrix([[(0, 1) for i in range(10)]
                                 for j in range(10)], 10, 10)
        self.assertEqual(str(calculator.matrixMultiplication(matrix1, matrix2)),
                         str(matrix2))

    def test_small_matrix_scalar_multiplication_1(self):
        """Test multiplying a matrix by 0"""
        scalar = 0
        matrix = self.__small_10x10_matrix1()
        result = []
        for i in range(matrix.rowAmount):
            row = []
            for j in range(matrix.colAmount):
                row.append((scalar * matrix.getCell(i, j)[0],
                            matrix.getCell(i, j)[1]))
            result.append(row)
        self.assertEqual(str(calculator.matrixScalarMultiplication(matrix,
                                                                   scalar)),
                         str(Matrix.Matrix(result, 10, 10)))

    def test_small_matrix_scalar_multiplication_2(self):
        """Test multiplying a matrix by 1"""
        scalar = 1
        matrix = self.__small_10x10_matrix2()
        result = []
        for i in range(matrix.rowAmount):
            row = []
            for j in range(matrix.colAmount):
                row.append(matrix.getCell(i, j))
            result.append(row)
        self.assertEqual(str(calculator.matrixScalarMultiplication(matrix,
                                                                   scalar)),
                         str(Matrix.Matrix(result, 10, 10)))

    def test_small_matrix_scalar_multiplication_3(self):
        """Test multiplying by -1"""
        scalar = -1
        matrix = self.__small_10x10_matrix2()
        result = []
        for i in range(matrix.rowAmount):
            row = []
            for j in range(matrix.colAmount):
                row.append((scalar * matrix.getCell(i, j)[0],
                            matrix.getCell(i, j)[1]))
            result.append(row)
        self.assertEqual(str(calculator.matrixScalarMultiplication(matrix,
                                                                   scalar)),
                         str(Matrix.Matrix(result, 10, 10)))

    def test_small_matrix_scalar_multiplication_4(self):
        """Test multiplying by 10"""
        scalar = 10
        matrix = self.__small_10x10_matrix2()
        result = []
        for i in range(matrix.rowAmount):
            row = []
            for j in range(matrix.colAmount):
                row.append((scalar * matrix.getCell(i, j)[0],
                            matrix.getCell(i, j)[1]))
            result.append(row)
        self.assertEqual(str(calculator.matrixScalarMultiplication(matrix,
                                                                   scalar)),
                         str(Matrix.Matrix(result, 10, 10)))

    def test_small_matrix_scalar_multiplication_5(self):
        """Test multiplying by -10"""
        scalar = -10
        matrix = self.__small_10x10_matrix2()
        result = []
        for i in range(matrix.rowAmount):
            row = []
            for j in range(matrix.colAmount):
                row.append((scalar * matrix.getCell(i, j)[0],
                            matrix.getCell(i, j)[1]))
            result.append(row)
        self.assertEqual(str(calculator.matrixScalarMultiplication(matrix,
                                                                   scalar)),
                         str(Matrix.Matrix(result, 10, 10)))

    def test_small_matrix_scalar_multiplication_6(self):
        """Test multiplying by 8"""
        scalar = 2**3
        matrix = self.__small_10x10_matrix2()
        result = []
        for i in range(matrix.rowAmount):
            row = []
            for j in range(matrix.colAmount):
                row.append((scalar * matrix.getCell(i, j)[0],
                            matrix.getCell(i, j)[1]))
            result.append(row)
        self.assertEqual(str(calculator.matrixScalarMultiplication(matrix,
                                                                   scalar)),
                         str(Matrix.Matrix(result, 10, 10)))

    def test_matrix_class_getCell_1(self):
        """Test getCell of the Matrix class for correct value returns."""
        matrix = self.__small_3x3_matrix1()
        self.assertEqual(matrix.getCell(0, 0), (1, 1))

    def test_matrix_class_getCell_2(self):
        """Test getCell of the Matrix class for correct value returns."""
        matrix = self.__small_3x3_matrix2()
        self.assertEqual(matrix.getCell(2, 1), (0, 1))

    def test_matrix_class_getCell_3(self):
        """Test getCell of the Matrix class for correct value returns."""
        matrix = self.__small_10x10_matrix1()
        self.assertEqual(matrix.getCell(4, 4), (44, 1))

    def test_matrix_class_getCell_4(self):
        """Test getCell of the Matrix class for correct value returns."""
        matrix = self.__small_10x10_matrix2()
        self.assertEqual(matrix.getCell(9, 9), (1, 1))

    def test_matrix_class_getCell_5(self):
        """Test getCell of the Matrix class for correct value returns."""
        matrix = self.__n_by_n_identity_matrix(20)
        self.assertEqual(matrix.getCell(10, 10), (1, 1))

    def test_matrix_class_getCell_6(self):
        """Test getCell of the Matrix class for correct value returns."""
        matrix = self.__n_by_n_identity_matrix(20)
        self.assertEqual(matrix.getCell(10, 11), (0, 1))

    def test_matrix_class_getCell_7(self):
        """Test getCell of the Matrix class for correct value returns.

        Now with scalar multiplication."""
        matrix = self.__small_10x10_matrix1()
        matrix.multiplyScalar(0)
        self.assertEqual(matrix.getCell(9, 3), (0, 1))

    def test_matrix_class_getRow_1(self):
        """Test getRow of the Matrix class for correct value returns."""
        matrix = self.__n_by_n_identity_matrix(20)
        result = [(0, 1) for i in range(20)]
        result[10] = (1, 1)
        self.assertListEqual(matrix.getRow(10), result)

    def test_matrix_class_getRow_2(self):
        """Test getRow of the Matrix class for correct value returns."""
        matrix = self.__n_by_n_identity_matrix(20)
        self.assertListEqual(matrix.getRow(19), [(0, 1) for i in range(19)]
                             + [(1, 1)])

    def test_matrix_class_getRow_3(self):
        """Test getRow of the Matrix class for correct value returns."""
        matrix = self.__small_10x10_matrix1()
        self.assertListEqual(matrix.getRow(5), [(50+i, 1) for i in range(10)])

    def test_matrix_class_getRow_4(self):
        """Test getRow of the Matrix class for correct value returns."""
        matrix = self.__small_10x10_matrix1()
        self.assertListEqual(matrix.getRow(5), [(50+i, 1) for i in range(10)])

    def test_matrix_class_getRow_5(self):
        """Test getRow of the Matrix class for correct value returns."""
        matrix = self.__small_10x10_matrix2()
        self.assertListEqual(matrix.getRow(5), [(50-i, 1) for i in range(10)])

    def test_matrix_class_getRow_6(self):
        """Test getRow of the Matrix class for correct value returns."""
        matrix = self.__small_3x3_matrix1()
        self.assertListEqual(matrix.getRow(0), [(1, 1), (2, 1), (3, 1)])

    def test_matrix_class_getRow_7(self):
        """Test getRow of the Matrix class for correct value returns.

        Testing now with scalar multiplication."""
        matrix = self.__small_3x3_matrix1()
        matrix.multiplyScalar(-2)
        self.assertListEqual(matrix.getRow(0), [(-2, 1), (-4, 1), (-6, 1)])

    def test_matrix_class_getCol_1(self):
        """Test getCol of the Matrix class for correct value returns."""
        matrix = self.__small_3x3_matrix1()
        self.assertEqual(matrix.getCol(0), [(1, 1), (3, 1), (4, 1)])

    def test_matrix_class_getCol_2(self):
        """Test getCol of the Matrix class for correct value returns."""
        matrix = self.__small_3x3_matrix1()
        self.assertEqual(matrix.getCol(2), [(3, 1), (5, 1), (6, 1)])

    def test_matrix_class_getCol_3(self):
        """Test getCol of the Matrix class for correct value returns."""
        matrix = self.__small_10x10_matrix2()
        self.assertEqual(matrix.getCol(0), [(100 - 10*i, 1) for i in range(10)])

    def test_matrix_class_getCol_4(self):
        """Test getCol of the Matrix class for correct value returns."""
        matrix = self.__small_10x10_matrix2()
        matrix.multiplyScalar(10)
        self.assertEqual(matrix.getCol(0),
                         [(1000 - 100*i, 1) for i in range(10)])

    def test_matrix_class_getCol_5(self):
        """Test getCol of the Matrix class for correct value returns.

        This one also tests that the method works as expected when scalar
        multiplication has taken place.
        """
        matrix = self.__small_10x10_matrix1()
        matrix.multiplyScalar(-1)
        self.assertEqual(matrix.getCol(3),
                         [(-3 - (10*i), 1) for i in range(10)])

    def test_matrix_class_getCol_6(self):
        """Test getCol of the Matrix class for correct value returns.

        This one also tests that the method works as expected when scalar
        multiplication has taken place.
        """
        matrix = self.__small_10x10_matrix1()
        matrix.multiplyScalar(0)
        self.assertEqual(matrix.getCol(7), [(0, 1) for i in range(10)])

    def test_matrix_class_multiplyScalar_1(self):
        """Make sure setting a scalar for matrices works."""
        matrix = self.__small_3x3_matrix1()
        matrix.multiplyScalar(-10)
        self.assertEqual(matrix.getScalar(), -10)

    def test_matrix_class_multiplyScalar_2(self):
        """Make sure setting a scalar for matrices works."""
        matrix = self.__small_3x3_matrix2()
        matrix.multiplyScalar(0)
        self.assertEqual(matrix.getScalar(), 0)

    def test_matrix_class_multiplyScalar_3(self):
        """Make sure setting a scalar for matrices works."""
        matrix = self.__small_10x10_matrix1()
        matrix.multiplyScalar(-3)
        matrix.multiplyScalar(-2)
        self.assertEqual(matrix.getScalar(), 6)

    def test_matrix_class_multiplyScalar_4(self):
        """Make sure setting a scalar for matrices works."""
        matrix = self.__small_10x10_matrix1()
        matrix.multiplyScalar(1)
        self.assertEqual(matrix.getScalar(), 1)

    def test_matrix_class_multiplyScalar_5(self):
        """Make sure setting a scalar for matrices works."""
        matrix = self.__small_10x10_matrix1()
        self.assertEqual(matrix.getScalar(), 1)

    def test_matrix_class_multiplyScalar_6(self):
        """Make sure setting a scalar for matrices works."""
        matrix = self.__small_10x10_matrix1()
        matrix.multiplyScalar(2)
        matrix.multiplyScalar(10)
        matrix.multiplyScalar(0)
        matrix.multiplyScalar(1337)
        self.assertEqual(matrix.getScalar(), 0)

    def test_matrix_creation_1(self):
        """Test random 10x10 matrix generation."""
        n = 10
        m = 10
        rows = self.__random_n_by_m_array(n, m)
        matrix = Matrix.Matrix(rows, n, m)
        self.assertListEqual(matrix.getRowArray(), rows)
        self.assertListEqual(matrix.getColArray(), [[] for i in range(n)])
        self.assertEqual(matrix.getRowAmount(), n)
        self.assertEqual(matrix.getColAmount(), m)
        self.assertEqual(matrix.getScalar(), 1)

    def test_matrix_creation_2(self):
        """Test random 5x10 matrix generation."""
        n = 5
        m = 10
        rows = self.__random_n_by_m_array(n, m)
        matrix = Matrix.Matrix(rows, n, m)
        self.assertListEqual(matrix.getRowArray(), rows)
        self.assertListEqual(matrix.getColArray(), [[] for i in range(n)])
        self.assertEqual(matrix.getRowAmount(), n)
        self.assertEqual(matrix.getColAmount(), m)
        self.assertEqual(matrix.getScalar(), 1)

    def test_matrix_creation_3(self):
        """Test random 1x1 matrix generation."""
        n = 1
        m = 1
        rows = self.__random_n_by_m_array(n, m)
        matrix = Matrix.Matrix(rows, n, m)
        self.assertListEqual(matrix.getRowArray(), rows)
        self.assertListEqual(matrix.getColArray(), [[] for i in range(n)])
        self.assertEqual(matrix.getRowAmount(), n)
        self.assertEqual(matrix.getColAmount(), m)
        self.assertEqual(matrix.getScalar(), 1)

    def test_matrix_creation_4(self):
        """Test random 10x2 matrix generation."""
        n = 10
        m = 2
        rows = self.__random_n_by_m_array(n, m)
        matrix = Matrix.Matrix(rows, n, m)
        self.assertListEqual(matrix.getRowArray(), rows)
        self.assertListEqual(matrix.getColArray(), [[] for i in range(n)])
        self.assertEqual(matrix.getRowAmount(), n)
        self.assertEqual(matrix.getColAmount(), m)
        self.assertEqual(matrix.getScalar(), 1)

    def test_matrix_creation_5(self):
        """Test random 0x0 matrix generation."""
        n = 0
        m = 0
        rows = self.__random_n_by_m_array(n, m)
        matrix = Matrix.Matrix(rows, n, m)
        self.assertListEqual(matrix.getRowArray(), rows)
        self.assertListEqual(matrix.getColArray(), [[] for i in range(n)])
        self.assertEqual(matrix.getRowAmount(), n)
        self.assertEqual(matrix.getColAmount(), m)
        self.assertEqual(matrix.getScalar(), 1)

    def test_matrix_creation_6(self):
        """Test random 0x10 matrix generation."""
        n = 0
        m = 10
        rows = self.__random_n_by_m_array(n, m)
        matrix = Matrix.Matrix(rows, n, m)
        self.assertListEqual(matrix.getRowArray(), rows)
        self.assertListEqual(matrix.getColArray(), [[] for i in range(n)])
        self.assertEqual(matrix.getRowAmount(), n)
        self.assertEqual(matrix.getColAmount(), m)
        self.assertEqual(matrix.getScalar(), 1)

    def test_small_matrix_determinant_1(self):
        """Test determinant calculator with a random 4x4 matrix."""
        matrix = Matrix.Matrix([[(8, 1), (-9, 1), (-2, 1), (-5, 1)],
                                [(9, 1), (6, 1), (-6, 1), (9, 1)],
                                [(-3, 1), (-9, 1), (4, 1), (-2, 1)],
                                [(0, 1), (-7, 1), (8, 1), (8, 1)]], 4, 4)
        ans = -5352
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_determinant_2(self):
        """Test determinant calculator with a 3x3 by matrix."""
        matrix = self.__small_3x3_matrix1()
        ans = 0
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_determinant_3(self):
        """Test determinant calculator with a 3x3 by matrix."""
        matrix = self.__small_3x3_matrix2()
        ans = 0
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_determinant_4(self):
        """Test determinant calculator with a 10x10 by matrix."""
        matrix = self.__small_10x10_matrix2()
        ans = 0
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_determinant_5(self):
        """Test determinant calculator with a 10x10 by identity matrix."""
        matrix = self.__n_by_n_identity_matrix(10)
        ans = 1
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_determinant_6(self):
        """Test determinant calculator when a matrix has 2 as its scalar."""
        matrix = self.__n_by_n_identity_matrix(10)
        matrix.multiplyScalar(2)
        ans = 2**10
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_determinant_7(self):
        """Test determinant calculator when a matrix has -1 as its scalar."""
        matrix = self.__n_by_n_identity_matrix(10)
        matrix.multiplyScalar(-1)
        ans = 1
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_determinant_8(self):
        """Test determinant calculator when a matrix has -1 as its scalar."""
        matrix = self.__n_by_n_identity_matrix(9)
        matrix.multiplyScalar(-1)
        ans = -1
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_determinant_9(self):
        """Test determinant calculator with a 1x1 matrix."""
        matrix = Matrix.Matrix([[(1, 1)]], 1, 1)
        ans = 1
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_determinant_10(self):
        """Test determinant calculator with a 10x10 zero matrix."""
        matrix = Matrix.Matrix([[(0, 1) for i in range(10)] for j in range(10)],
                               10,
                               10)
        ans = 0
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_determinant_11(self):
        """Test determinant calculator with a 4x4 matrix."""
        matrix = [[(0, 1), (2, 1), (8, 1), (11, 1)],
                  [(11, 1), (10, 1), (3, 1), (9, 1)],
                  [(8, 1), (5, 1), (2, 1), (8, 1)],
                  [(2, 1), (9, 1), (4, 1), (1, 1)]]
        matrix = Matrix.Matrix(matrix, 4, 4)
        ans = 108
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_determinant_12(self):
        matrix = [[(1, 1), (0, 1), (1, 1)],
                  [(1, 1), (0, 1), (0, 1)],
                  [(0, 1), (0, 1), (0, 1)]]
        matrix = Matrix.Matrix(matrix, 3, 3)
        ans = 0
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_determinant_13(self):
        matrix = [[(157, 50), (-157, 50)],
                  [(1, 2), (-1, 2)]]
        matrix = Matrix.Matrix(matrix, 2, 2)
        ans = 0
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)


    def test_small_matrix_inversion_ten_times_with_a_random_matrix(self):
        for test in range(10):
            size = random.randint(2, 20)
            # Let A be a random matrix of size sizeXsize.
            A = Matrix.Matrix(
                self.__random_n_by_m_array(
                    size, size), size, size)
            # Can't invert iff determinant is 0.
            if calculator.matrixDeterminant(A) == 0:
                continue
            B = calculator.matrixInverse(A)

            # Multiply A and B into C. After multiplying them, C should be an
            # identity matrix.
            C = calculator.matrixMultiplication(A, B)
            identityMatrix = self.__n_by_n_identity_matrix(size)
            self.assertListEqual(C.getRowArray(),
                                 identityMatrix.getRowArray())

    def test_AYY(self):
        matrix = [[(0, 1), (2, 1), (8, 1), (11, 1)],
                  [(11, 1), (10, 1), (3, 1), (9, 1)],
                  [(8, 1), (5, 1), (2, 1), (8, 1)],
                  [(2, 1), (9, 1), (4, 1), (1, 1)]]
        matrix = Matrix.Matrix(matrix, 4, 4)
        inverse = calculator.matrixInverse(matrix)
        ans = [[(-3, 4), (-83, 18), (215, 36), (71, 36)],
               [(1, 2), (31, 9), (-79, 18), (-25, 18)],
               [(-11, 12), (-349, 54), (883, 108), (307, 108)],
               [(2, 3), (110, 27), (-139, 27), (-49, 27)]]
        ans = Matrix.Matrix(ans, 4, 4)
        self.assertEqual(str(ans), str(inverse))

    def test_LMAO(self):
        matrix = [[(1, 1), (2, 1), (3, 1)],
                  [(4, 1), (5, 1), (6, 1)],
                  [(7, 1), (8, 1), (1, 1)]]
        matrix = Matrix.Matrix(matrix, 3, 3)
        inverse = calculator.matrixInverse(matrix)
        ans = [[(-43, 24), (11, 12), (-1, 8)],
               [(19, 12), (-5, 6), (1, 4)],
               [(-1, 8), (1, 4), (-1, 8)]]
        ans = Matrix.Matrix(ans, 3, 3)
        self.assertEqual(str(ans), str(inverse))

    def test_my_gcd_1(self):
        self.assertEqual(-609, my_gcd(0, -609))

    def test_my_gcd_2(self):
        self.assertEqual(-1, my_gcd(8, -609))

    def test_my_gcd_3(self):
        self.assertEqual(-7, my_gcd(1337, -609))

    def test_my_gcd_4(self):
        self.assertEqual(-6, my_gcd(-666, -420))

    def test_my_gcd_5(self):
        self.assertEqual(0, my_gcd(0, 0))

    def test_my_gcd_6(self):
        self.assertEqual(123, my_gcd(123, 123))

    def test_my_abs_1(self):
        a = -666
        self.assertEqual(-a, my_abs(a))

    def test_my_abs_2(self):
        a = 666
        self.assertEqual(a, my_abs(a))

    def test_my_abs_3(self):
        a = 0
        self.assertEqual(a, my_abs(a))

    def test_my_abs_4(self):
        a = -420.1337
        self.assertEqual(-a, my_abs(a))

    def test_my_abs_5(self):
        a = -1
        self.assertEqual(-a, my_abs(a))

    def test_my_abs_6(self):
        a = 1
        self.assertEqual(a, my_abs(a))

    def test_my_range_1(self):
        self.assertListEqual(list(range(10)), my_range(10))

    def test_my_range_2(self):
        self.assertListEqual(list(range(0)), my_range(0))

    def test_my_range_3(self):
        self.assertListEqual(list(range(-9, 0)), my_range(-9, 0))

    def test_my_range_4(self):
        self.assertListEqual(list(range(-10, 10)), my_range(-10, 10))

    def test_my_range_5(self):
        self.assertListEqual(list(range(10, -10)), my_range(10, -10))

    def test_my_range_6(self):
        self.assertListEqual(list(range(1, 0)), my_range(1, 0))

    def test_my_reversed_1(self):
        self.assertListEqual(list(reversed(range(10))),
                             my_reversed(my_range(10)))

    def test_my_reversed_2(self):
        self.assertListEqual(list(reversed(range(0))),
                             my_reversed(my_range(0)))

    def test_my_reversed_3(self):
        self.assertListEqual(list(reversed(range(-9, 0))),
                             my_reversed(my_range(-9, 0)))

    def test_my_reversed_4(self):
        self.assertListEqual(list(reversed(range(-10, 10))),
                             my_reversed(my_range(-10, 10)))

    def test_my_reversed_5(self):
        self.assertListEqual(list(reversed(range(10, -10))),
                             my_reversed(my_range(10, -10)))

    def test_my_reversed_6(self):
        self.assertListEqual(list(reversed(range(1, 0))),
                             my_reversed(my_range(1, 0)))

    def test_my_max_1(self):
        self.assertEqual(10, my_max(list(range(11))))

    def test_my_max_2(self):
        self.assertEqual(1, my_max(0, -1.2, -3, -666, 0, 1, 0))

    def test_my_max_3(self):
        self.assertEqual(9001, my_max([0, 1, 66, 42, 609, -1337, -2, 9001]))

    def test_my_max_4(self):
        with self.assertRaises(TypeError):
            my_max([])

    def test_my_max_5(self):
        self.assertEqual(9001, my_max(9001))

    def test_my_max_6(self):
        self.assertEqual(1, my_max(1, -1, 0))

    def test_my_split_1(self):
        with self.assertRaises(TypeError):
            my_split(609)

    def test_my_split_2(self):
        self.assertListEqual("".split(" "), my_split("", " "))

    def test_my_split_3(self):
        s = "This should work fine."
        c = " "
        self.assertListEqual(s.split(c), my_split(s, c))

    def test_my_split_4(self):
        s = "?This?hould?work?fine."
        c = "?"
        self.assertListEqual(s.split(c), my_split(s, c))

    def test_my_split_5(self):
        s = "Are you sure this thing actually works?"
        c = "t"
        self.assertListEqual(s.split(c), my_split(s, c))

    def test_my_split_6(self):
        s = "Positive. I don't make mistakes when coding."
        c = "."
        self.assertListEqual(s.split(c), my_split(s, c))

    def test_my_strip_1(self):
        s = "  Let's see if this thing actually works.    "
        self.assertEqual(s.strip(), my_strip(s))

    def test_my_strip_2(self):
        s = "     "
        self.assertEqual(s.strip(), my_strip(s))

    def test_my_strip_3(self):
        s = "Dis gonna be gud.     "
        self.assertEqual(s.strip(), my_strip(s))

    def test_my_strip_4(self):
        s = "   ayyy lmao"
        self.assertEqual(s.strip(), my_strip(s))

    def test_my_strip_5(self):
        s = "This string should stay the same after my_strip(s)"
        self.assertEqual(s.strip(), my_strip(s))

    def test_my_strip_6(self):
        s = ""
        self.assertEqual(s.strip(), my_strip(s))

    def test_my_strip_7(self):
        s = 609
        with self.assertRaises(TypeError):
            my_strip(s)

    def test_my_lower_1(self):
        s = "AYY LMAO"
        self.assertEqual(s.lower(), my_lower(s))

    def test_my_lower_2(self):
        s = "Lalalalaalaala tralalalalaaaaa"
        self.assertEqual(s.lower(), my_lower(s))

    def test_my_lower_3(self):
        s = u"Öykkäri käveli kauppan noutamaan Åkermanneille viinaa."
        self.assertEqual(s.lower(), my_lower(s))

    def test_my_lower_4(self):
        s = ""
        self.assertEqual(s.lower(), my_lower(s))

    def test_my_lower_5(self):
        s = u"ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
        self.assertEqual(s.lower(), my_lower(s))

    def test_my_lower_6(self):
        s = u" ⊃∨∈♥ı  abcdefghijklmnopqrstuvwxyzåäö  os~€→♥€°⊂→"
        self.assertEqual(s.lower(), my_lower(s))

    def test_frac_add_1(self):
        a = (1, 2)
        b = (3, 2)
        ans = (4, 2)
        self.assertEqual(ans, calculator.frac_add(a, b))

    def test_frac_add_2(self):
        a = (1, 3)
        b = (-2, 5)
        ans = (-1, 15)
        self.assertEqual(ans, calculator.frac_add(a, b))

    def test_frac_add_3(self):
        a = (0, 3)
        b = (0, 1)
        ans = (0, 3)
        self.assertEqual(ans, calculator.frac_add(a, b))

    def test_frac_add_4(self):
        a = (-1, 3)
        b = (-1, 1)
        ans = (-4, 3)
        self.assertEqual(ans, calculator.frac_add(a, b))

    def test_frac_mult_1(self):
        a = (420, 1337)
        b = (69, 666)
        ans = (28980, 890442)
        self.assertEqual(ans, calculator.frac_mult(a, b))

    def test_frac_mult_2(self):
        a = (0, 1)
        b = (69, 666)
        ans = (0, 666)
        self.assertEqual(ans, calculator.frac_mult(a, b))

    def test_frac_mult_3(self):
        a = (-2, 1)
        b = (9, -1)
        ans = (-18, -1)
        self.assertEqual(ans, calculator.frac_mult(a, b))

    def test_frac_mult_4(self):
        a = (1, 1)
        b = (1, 1)
        ans = (1, 1)
        self.assertEqual(ans, calculator.frac_mult(a, b))

    def test_frac_reduc_1(self):
        a = (1, 1)
        ans = (1, 1)
        self.assertEqual(ans, calculator.frac_reduc(a))

    def test_frac_reduc_2(self):
        a = (2**10, 2**2 * 3)
        ans = (2**8, 3)
        self.assertEqual(ans, calculator.frac_reduc(a))

    def test_frac_reduc_3(self):
        a = (2*3*5*7*11, 5*7*11*13)
        ans = (2*3, 13)
        self.assertEqual(ans, calculator.frac_reduc(a))

    def test_frac_reduc_4(self):
        a = (-2*3*5*7*11, -5*7*11*13)
        ans = (2*3, 13)
        self.assertEqual(ans, calculator.frac_reduc(a))

    def test_matrix_transpose_1(self):
        rows = [[(1, 1), (2, 1)],
                [(3, 1), (4, 1)],
                [(5, 1), (6, 1)]]
        rows = Matrix.Matrix(rows, 3, 2)

    def test_matrix_transpose_2(self):
        rows = [[(0, 1), (0, 1), (1, 1)],
                [(1, 1), (0, 1), (0, 1)],
                [(0, 1), (1, 1), (0, 1)]]
        rows = Matrix.Matrix(rows, 3, 3)


if __name__ == '__main__':
    unittest.main()
