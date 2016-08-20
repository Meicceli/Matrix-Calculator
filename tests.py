import unittest
import random
from src import calculator, parser
from src.myAlgorithms import my_gcd, my_abs, my_range, my_max, my_reversed


class TestMatrixCalculations(unittest.TestCase):

    def __random_n_by_m_array(self, n, m, lowerBound=0, upperBound=10):
        rows = []
        for row in range(n):
            newRow = []
            for col in range(m):
                newRow.append(random.randint(lowerBound, upperBound+1))
            rows.append(newRow)
        return rows

    def __n_by_n_identity_matrix(self, n):
        matrix = []
        for row in range(n):
            newRow = []
            for col in range(n):
                if row == col:
                    newRow.append(1)
                else:
                    newRow.append(0)
            matrix.append(newRow)
        return parser.Matrix(matrix, n, n)

    def __small_3x3_matrix1(self):
        matrix = parser.Matrix([[1, 2, 3],
                                [3, 4, 5],
                                [4, 5, 6]], 3, 3)
        return matrix

    def __small_3x3_matrix2(self):
        matrix = parser.Matrix([[1, 0, 1],
                                [1, 0, 0],
                                [0, 0, 1]], 3, 3)
        return matrix

    def __small_10x10_matrix1(self):
        """Matrix 0,..,99 from left to right, up-down"""
        matrix = [[] for i in range(10)]
        num = 0
        row = 0
        while row < 10:
            matrix[row].append(num)
            num += 1
            if num % 10 == 0:
                row += 1
        return parser.Matrix(matrix, 10, 10)

    def __small_10x10_matrix2(self):
        """Matrix 100,...,1"""
        matrix = [[] for i in range(10)]
        num = 100
        row = 0
        while row < 10:
            matrix[row].append(num)
            num -= 1
            if num % 10 == 0:
                row += 1
        return parser.Matrix(matrix, 10, 10)

    def test_small_matrix_addition_1(self):
        resultMatrix = parser.Matrix([[2, 2, 4],
                                      [4, 4, 5],
                                      [4, 5, 7]], 3, 3)
        matrix1 = self.__small_3x3_matrix1()
        matrix2 = self.__small_3x3_matrix2()
        self.assertEqual(
            str(calculator.matrixAddition(matrix1, matrix2)),
            str(resultMatrix))

    def test_small_matrix_addition_2(self):
        resultMatrix = parser.Matrix([[2, 4, 6],
                                      [6, 8, 10],
                                      [8, 10, 12]], 3, 3)
        matrix = self.__small_3x3_matrix1()
        self.assertEqual(str(calculator.matrixAddition(matrix, matrix)),
                         str(resultMatrix))

    def test_small_matrix_addition_3(self):
        resultMatrix = parser.Matrix(
            [[100 for i in range(10)] for j in range(10)], 10, 10)
        matrix1 = self.__small_10x10_matrix1()
        matrix2 = self.__small_10x10_matrix2()
        self.assertEqual(str(calculator.matrixAddition(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_addition_4(self):
        resultMatrix = [[col+10*row for col in range(10)] for row in range(10)]
        for j in range(10):
            resultMatrix[j][j] += 1
        resultMatrix = parser.Matrix(resultMatrix, 10, 10)
        matrix1 = self.__n_by_n_identity_matrix(10)
        matrix2 = self.__small_10x10_matrix1()
        self.assertEqual(str(calculator.matrixAddition(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_addition_5(self):
        """See what happens if we try adding the same matrix object to itself"""
        resultMatrix = parser.Matrix([[2, 0, 2],
                                      [2, 0, 0],
                                      [0, 0, 2]], 3, 3)
        matrix = self.__small_3x3_matrix2()
        self.assertEqual(str(calculator.matrixAddition(matrix, matrix)),
                         str(resultMatrix))

    def test_small_matrix_addition_6(self):
        """See what happens if we try adding the same matrix object to itself"""
        resultMatrix = parser.Matrix([[2, 4, 6],
                                      [6, 8, 10],
                                      [8, 10, 12]], 3, 3)
        matrix1 = self.__small_3x3_matrix1()
        self.assertEqual(str(calculator.matrixAddition(matrix1, matrix1)),
                         str(resultMatrix))

    def test_small_matrix_substraction_1(self):
        """Basic sanity test"""
        resultMatrix = parser.Matrix([[0, 2, 2],
                                      [2, 4, 5],
                                      [4, 5, 5]], 3, 3)
        matrix1 = self.__small_3x3_matrix1()
        matrix2 = self.__small_3x3_matrix2()
        self.assertEqual(str(calculator.matrixSubstraction(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_substraction_2(self):
        """Basic sanity test"""
        resultMatrix = parser.Matrix([[-0, -2, -2],
                                      [-2, -4, -5],
                                      [-4, -5, -5]], 3, 3)
        matrix1 = self.__small_3x3_matrix2()
        matrix2 = self.__small_3x3_matrix1()
        self.assertEqual(str(calculator.matrixSubstraction(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_substraction_3(self):
        """Test substraction when given matrixes are the same object."""
        resultMatrix = parser.Matrix([[0, 0, 0],
                                      [0, 0, 0],
                                      [0, 0, 0]], 3, 3)
        matrix1 = self.__small_3x3_matrix1()
        self.assertEqual(str(calculator.matrixSubstraction(matrix1, matrix1)),
                         str(resultMatrix))

    def test_small_matrix_substraction_4(self):
        """Test substraction with just the 10x10 identity matrix"""
        resultMatrix = parser.Matrix(
            [[0 for i in range(10)] for j in range(10)], 10, 10)

        matrix1 = self.__n_by_n_identity_matrix(10)
        matrix2 = self.__n_by_n_identity_matrix(10)
        self.assertEqual(str(calculator.matrixSubstraction(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_substraction_5(self):
        """Test substraction with two different 10x10 matrices"""
        resultMatrix = parser.Matrix(
            [[100 - 2 * (col + 10 * row) for col in range(10)]
             for row in range(10)],
            10, 10)
        matrix1 = self.__small_10x10_matrix2()
        matrix2 = self.__small_10x10_matrix1()
        self.assertEqual(str(calculator.matrixSubstraction(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_substraction_6(self):
        """Test substraction with two different 10x10 matrices"""
        resultMatrix = parser.Matrix(
            [[-100 + 2 * (col + 10 * row) for col in range(10)]
             for row in range(10)],
            10, 10)
        matrix1 = self.__small_10x10_matrix1()
        matrix2 = self.__small_10x10_matrix2()
        self.assertEqual(str(calculator.matrixSubstraction(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_multiplication_1(self):
        """Test multiplying identity matrices together"""
        matrix1 = self.__n_by_n_identity_matrix(20)
        self.assertEqual(str(calculator.matrixMultplication(matrix1, matrix1)),
                         str(matrix1))

    def test_small_matrix_multiplication_2(self):
        """Test multiplying two different matrices together"""
        resultMatrix = parser.Matrix([[3, 0, 4],
                                      [7, 0, 8],
                                      [9, 0, 10]], 3, 3)
        matrix1 = self.__small_3x3_matrix1()
        matrix2 = self.__small_3x3_matrix2()
        self.assertEqual(str(calculator.matrixMultplication(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_multiplication_3(self):
        """Test multiplying two different matrices together"""
        resultMatrix = parser.Matrix([[5, 7, 9],
                                      [1, 2, 3],
                                      [4, 5, 6]], 3, 3)
        matrix1 = self.__small_3x3_matrix2()
        matrix2 = self.__small_3x3_matrix1()
        self.assertEqual(str(calculator.matrixMultplication(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_multiplication_4(self):
        """Test multiplying two different matrices together"""
        resultMatrix = parser.Matrix(
            [[1650, 1605, 1560, 1515, 1470, 1425, 1380, 1335, 1290, 1245],
             [7150, 7005, 6860, 6715, 6570, 6425, 6280, 6135, 5990, 5845],
             [12650, 12405, 12160, 11915, 11670, 11425, 11180, 10935, 10690,
              10445],
             [18150, 17805, 17460, 17115, 16770, 16425, 16080, 15735, 15390,
              15045],
             [23650, 23205, 22760, 22315, 21870, 21425, 20980, 20535, 20090,
              19645],
             [29150, 28605, 28060, 27515, 26970, 26425, 25880, 25335, 24790,
              24245],
             [34650, 34005, 33360, 32715, 32070, 31425, 30780, 30135, 29490,
              28845],
             [40150, 39405, 38660, 37915, 37170, 36425, 35680, 34935, 34190,
              33445],
             [45650, 44805, 43960, 43115, 42270, 41425, 40580, 39735, 38890,
              38045],
             [51150, 50205, 49260, 48315, 47370, 46425, 45480, 44535, 43590,
              42645]],
            10, 10)
        matrix1 = self.__small_10x10_matrix1()
        matrix2 = self.__small_10x10_matrix2()
        self.assertEqual(str(calculator.matrixMultplication(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_multiplication_5(self):
        """Test multiplying a matrix by the identity matrix"""
        resultMatrix = self.__small_10x10_matrix2()
        matrix1 = self.__n_by_n_identity_matrix(10)
        matrix2 = self.__small_10x10_matrix2()
        self.assertEqual(str(calculator.matrixMultplication(matrix1, matrix2)),
                         str(resultMatrix))

    def test_small_matrix_multiplication_6(self):
        """Test multiplying by a zero matrix"""
        matrix1 = self.__small_10x10_matrix1()
        matrix2 = parser.Matrix([[0 for i in range(10)]
                                 for j in range(10)], 10, 10)
        self.assertEqual(str(calculator.matrixMultplication(matrix1, matrix2)),
                         str(matrix2))

    def test_small_matrix_scalar_multiplication_1(self):
        """Test multiplying a matrix by 0"""
        scalar = 0
        matrix = self.__small_10x10_matrix1()
        result = []
        for i in range(matrix.rowAmount):
            row = []
            for j in range(matrix.colAmount):
                row.append(scalar * matrix.getCell(i, j))
            result.append(row)
        self.assertEqual(str(calculator.matrixScalarMultiplication(matrix,
                                                                   scalar)),
                         str(parser.Matrix(result, 10, 10)))

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
                         str(parser.Matrix(result, 10, 10)))

    def test_small_matrix_scalar_multiplication_3(self):
        """Test multiplying by -1"""
        scalar = -1
        matrix = self.__small_10x10_matrix2()
        result = []
        for i in range(matrix.rowAmount):
            row = []
            for j in range(matrix.colAmount):
                row.append(scalar * matrix.getCell(i, j))
            result.append(row)
        self.assertEqual(str(calculator.matrixScalarMultiplication(matrix,
                                                                   scalar)),
                         str(parser.Matrix(result, 10, 10)))

    def test_small_matrix_scalar_multiplication_4(self):
        """Test multiplying by 10"""
        scalar = 10
        matrix = self.__small_10x10_matrix2()
        result = []
        for i in range(matrix.rowAmount):
            row = []
            for j in range(matrix.colAmount):
                row.append(scalar * matrix.getCell(i, j))
            result.append(row)
        self.assertEqual(str(calculator.matrixScalarMultiplication(matrix,
                                                                   scalar)),
                         str(parser.Matrix(result, 10, 10)))

    def test_small_matrix_scalar_multiplication_5(self):
        """Test multiplying by -10"""
        scalar = -10
        matrix = self.__small_10x10_matrix2()
        result = []
        for i in range(matrix.rowAmount):
            row = []
            for j in range(matrix.colAmount):
                row.append(scalar * matrix.getCell(i, j))
            result.append(row)
        self.assertEqual(str(calculator.matrixScalarMultiplication(matrix,
                                                                   scalar)),
                         str(parser.Matrix(result, 10, 10)))

    def test_small_matrix_scalar_multiplication_6(self):
        """Test multiplying by 8"""
        scalar = 2**3
        matrix = self.__small_10x10_matrix2()
        result = []
        for i in range(matrix.rowAmount):
            row = []
            for j in range(matrix.colAmount):
                row.append(scalar * matrix.getCell(i, j))
            result.append(row)
        self.assertEqual(str(calculator.matrixScalarMultiplication(matrix,
                                                                   scalar)),
                         str(parser.Matrix(result, 10, 10)))

    def test_matrix_class_getCell_1(self):
        """Test getCell of the Matrix class for correct value returns."""
        matrix = self.__small_3x3_matrix1()
        self.assertEqual(matrix.getCell(0, 0), 1)

    def test_matrix_class_getCell_2(self):
        """Test getCell of the Matrix class for correct value returns."""
        matrix = self.__small_3x3_matrix2()
        self.assertEqual(matrix.getCell(2, 1), 0)

    def test_matrix_class_getCell_3(self):
        """Test getCell of the Matrix class for correct value returns."""
        matrix = self.__small_10x10_matrix1()
        self.assertEqual(matrix.getCell(4, 4), 44)

    def test_matrix_class_getCell_4(self):
        """Test getCell of the Matrix class for correct value returns."""
        matrix = self.__small_10x10_matrix2()
        self.assertEqual(matrix.getCell(9, 9), 1)

    def test_matrix_class_getCell_5(self):
        """Test getCell of the Matrix class for correct value returns."""
        matrix = self.__n_by_n_identity_matrix(20)
        self.assertEqual(matrix.getCell(10, 10), 1)

    def test_matrix_class_getCell_6(self):
        """Test getCell of the Matrix class for correct value returns."""
        matrix = self.__n_by_n_identity_matrix(20)
        self.assertEqual(matrix.getCell(10, 11), 0)

    def test_matrix_class_getCell_7(self):
        """Test getCell of the Matrix class for correct value returns.

        Now with scalar multiplication."""
        matrix = self.__small_10x10_matrix1()
        matrix.multiplyScalar(0)
        self.assertEqual(matrix.getCell(9, 3), 0)

    def test_matrix_class_getRow_1(self):
        """Test getRow of the Matrix class for correct value returns."""
        matrix = self.__n_by_n_identity_matrix(20)
        result = [0 for i in range(20)]
        result[10] = 1
        self.assertEqual(matrix.getRow(10), result)

    def test_matrix_class_getRow_2(self):
        """Test getRow of the Matrix class for correct value returns."""
        matrix = self.__n_by_n_identity_matrix(20)
        self.assertEqual(matrix.getRow(19), [0 for i in range(19)] + [1])

    def test_matrix_class_getRow_3(self):
        """Test getRow of the Matrix class for correct value returns."""
        matrix = self.__small_10x10_matrix1()
        self.assertEqual(matrix.getRow(5), [50+i for i in range(10)])

    def test_matrix_class_getRow_4(self):
        """Test getRow of the Matrix class for correct value returns."""
        matrix = self.__small_10x10_matrix1()
        self.assertEqual(matrix.getRow(5), [50+i for i in range(10)])

    def test_matrix_class_getRow_5(self):
        """Test getRow of the Matrix class for correct value returns."""
        matrix = self.__small_10x10_matrix2()
        self.assertEqual(matrix.getRow(5), [50-i for i in range(10)])

    def test_matrix_class_getRow_6(self):
        """Test getRow of the Matrix class for correct value returns."""
        matrix = self.__small_3x3_matrix1()
        self.assertEqual(matrix.getRow(0), [1, 2, 3])

    def test_matrix_class_getRow_7(self):
        """Test getRow of the Matrix class for correct value returns.

        Testing now with scalar multiplication."""
        matrix = self.__small_3x3_matrix1()
        matrix.multiplyScalar(-2)
        self.assertEqual(matrix.getRow(0), [-2, -4, -6])

    def test_matrix_class_getCol_1(self):
        """Test getCol of the Matrix class for correct value returns."""
        matrix = self.__small_3x3_matrix1()
        self.assertEqual(matrix.getCol(0), [1, 3, 4])

    def test_matrix_class_getCol_2(self):
        """Test getCol of the Matrix class for correct value returns."""
        matrix = self.__small_3x3_matrix1()
        self.assertEqual(matrix.getCol(2), [3, 5, 6])

    def test_matrix_class_getCol_3(self):
        """Test getCol of the Matrix class for correct value returns."""
        matrix = self.__small_10x10_matrix2()
        self.assertEqual(matrix.getCol(0), [100 - 10*i for i in range(10)])

    def test_matrix_class_getCol_4(self):
        """Test getCol of the Matrix class for correct value returns."""
        matrix = self.__small_10x10_matrix2()
        matrix.multiplyScalar(10)
        self.assertEqual(matrix.getCol(0), [1000 - 100*i for i in range(10)])

    def test_matrix_class_getCol_5(self):
        """Test getCol of the Matrix class for correct value returns.

        This one also tests that the method works as expected when scalar
        multiplication has taken place.
        """
        matrix = self.__small_10x10_matrix1()
        matrix.multiplyScalar(-1)
        self.assertEqual(matrix.getCol(3), [-3 - (10*i) for i in range(10)])

    def test_matrix_class_getCol_6(self):
        """Test getCol of the Matrix class for correct value returns.

        This one also tests that the method works as expected when scalar
        multiplication has taken place.
        """
        matrix = self.__small_10x10_matrix1()
        matrix.multiplyScalar(0)
        self.assertEqual(matrix.getCol(7), [0 for i in range(10)])

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
        matrix = parser.Matrix(rows, n, m)
        self.assertEqual(matrix.getRowArray(), rows)
        self.assertEqual(matrix.getColArray(), [[] for i in range(n)])
        self.assertEqual(matrix.getRowAmount(), n)
        self.assertEqual(matrix.getColAmount(), m)
        self.assertEqual(matrix.getScalar(), 1)

    def test_matrix_creation_2(self):
        """Test random 5x10 matrix generation."""
        n = 5
        m = 10
        rows = self.__random_n_by_m_array(n, m)
        matrix = parser.Matrix(rows, n, m)
        self.assertEqual(matrix.getRowArray(), rows)
        self.assertEqual(matrix.getColArray(), [[] for i in range(n)])
        self.assertEqual(matrix.getRowAmount(), n)
        self.assertEqual(matrix.getColAmount(), m)
        self.assertEqual(matrix.getScalar(), 1)

    def test_matrix_creation_3(self):
        """Test random 1x1 matrix generation."""
        n = 1
        m = 1
        rows = self.__random_n_by_m_array(n, m)
        matrix = parser.Matrix(rows, n, m)
        self.assertEqual(matrix.getRowArray(), rows)
        self.assertEqual(matrix.getColArray(), [[] for i in range(n)])
        self.assertEqual(matrix.getRowAmount(), n)
        self.assertEqual(matrix.getColAmount(), m)
        self.assertEqual(matrix.getScalar(), 1)

    def test_matrix_creation_4(self):
        """Test random 10x2 matrix generation."""
        n = 10
        m = 2
        rows = self.__random_n_by_m_array(n, m)
        matrix = parser.Matrix(rows, n, m)
        self.assertEqual(matrix.getRowArray(), rows)
        self.assertEqual(matrix.getColArray(), [[] for i in range(n)])
        self.assertEqual(matrix.getRowAmount(), n)
        self.assertEqual(matrix.getColAmount(), m)
        self.assertEqual(matrix.getScalar(), 1)

    def test_matrix_creation_5(self):
        """Test random 0x0 matrix generation."""
        n = 0
        m = 0
        rows = self.__random_n_by_m_array(n, m)
        matrix = parser.Matrix(rows, n, m)
        self.assertEqual(matrix.getRowArray(), rows)
        self.assertEqual(matrix.getColArray(), [[] for i in range(n)])
        self.assertEqual(matrix.getRowAmount(), n)
        self.assertEqual(matrix.getColAmount(), m)
        self.assertEqual(matrix.getScalar(), 1)

    def test_matrix_creation_6(self):
        """Test random 0x10 matrix generation."""
        n = 0
        m = 10
        rows = self.__random_n_by_m_array(n, m)
        matrix = parser.Matrix(rows, n, m)
        self.assertEqual(matrix.getRowArray(), rows)
        self.assertEqual(matrix.getColArray(), [[] for i in range(n)])
        self.assertEqual(matrix.getRowAmount(), n)
        self.assertEqual(matrix.getColAmount(), m)
        self.assertEqual(matrix.getScalar(), 1)

    def test_small_matrix_determinant_1(self):
        """Test determinant calculator with a random 4x4 matrix."""
        matrix = parser.Matrix([[8, -9, -2, -5],
                                [9, 6, -6, 9],
                                [-3, -9, 4, -2],
                                [0, -7, 8, 8]], 4, 4)
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
        matrix = parser.Matrix([[1]], 1, 1)
        ans = 1
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_determinant_10(self):
        """Test determinant calculator with a 10x10 zero matrix."""
        matrix = parser.Matrix([[0 for i in range(10)] for j in range(10)],
                               10,
                               10)
        ans = 0
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_determinant_11(self):
        """Test determinant calculator with a 4x4 matrix."""
        matrix = [[0, 2, 8, 11],
                  [11, 10, 3, 9],
                  [8, 5, 2, 8],
                  [2, 9, 4, 1]]
        matrix = parser.Matrix(matrix, 4, 4)
        ans = 108
        result = calculator.matrixDeterminant(matrix)
        self.assertEqual(ans, result)

    def test_small_matrix_inversion_ten_times_with_a_random_matrix(self):
        for test in range(10):
            size = random.randint(2, 7)
            A = parser.Matrix(
                self.__random_n_by_m_array(
                    size, size), size, size)
            if calculator.matrixDeterminant(A) == 0:
                continue
            B = calculator.accurateMatrixInverse(A)
            C = [[0 for i in range(size)] for j in range(size)]
            identityMatrix = self.__n_by_n_identity_matrix(size)
            for i in range(size):
                for j in range(size):
                    cellValue = (0, 1)
                    for k in range(size):
                        toAdd = (A.getCell(i, k) * B[k][j][0], B[k][j][1])
                        cellValue = (cellValue[0] * toAdd[1]
                                     + toAdd[0] * cellValue[1],
                                     cellValue[1] * toAdd[1])
                    syt = my_gcd(cellValue[0], cellValue[1])
                    if syt == 0:
                        syt = 1
                    C[i][j] = (cellValue[0] / syt) / (cellValue[1] / syt)
                    if C[i][j] % 1 == 0:
                        C[i][j] = int(C[i][j])
            A_times_inverse = parser.Matrix(C, size, size)
            self.assertListEqual(A_times_inverse.getRowArray(),
                                 identityMatrix.getRowArray())

    def test_AYY(self):
        matrix = [[0, 2, 8, 11],
                  [11, 10, 3, 9],
                  [8, 5, 2, 8],
                  [2, 9, 4, 1]]
        matrix = parser.Matrix(matrix, 4, 4)
        inverse = calculator.accurateMatrixInverse(matrix)
        ans = [[(-3, 4), (-83, 18), (215, 36), (71, 36)],
               [(1, 2), (31, 9), (-79, 18), (-25, 18)],
               [(-11, 12), (-349, 54), (883, 108), (307, 108)],
               [(2, 3), (110, 27), (-139, 27), (-49, 27)]]
        self.assertListEqual(ans, inverse)

    def test_LMAO(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 1]]
        matrix = parser.Matrix(matrix, 3, 3)
        inverse = calculator.accurateMatrixInverse(matrix)
        ans = [[(-43, 24), (11, 12), (-1, 8)],
               [(19, 12), (-5, 6), (1, 4)],
               [(-1, 8), (1, 4), (-1, 8)]]
        self.assertListEqual(ans, inverse)

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


if __name__ == '__main__':
    unittest.main()
