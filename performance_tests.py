import unittest
import time
import random
from src import calculator
from src.parser import Matrix


# How many times each test is run
n = 10


class TestPerformanceOfMatrixOperations(unittest.TestCase):

    def __random_n_by_m_array(self, n, m, lowerBound=0, upperBound=10):
        rows = []
        for row in range(n):
            newRow = []
            for col in range(m):
                newRow.append(random.randint(lowerBound, upperBound+1))
            rows.append(newRow)
        return rows

    def test_matrix_inversion_performance_50x50(self):
        """Test matrix inversion ten times with a random 50x50 matrix"""
        global n
        size = 50
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 50, 50)
            start = time.clock()
            calculator.matrixInverse(matrix)
            end = time.clock()
            totaltime += end - start
        print("INVERTING 50x50 MATRIX WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_inversion_performance_40x40(self):
        """Test matrix inversion ten times with a random 40x40 matrix"""
        global n
        size = 40
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 40, 40)
            start = time.clock()
            calculator.matrixInverse(matrix)
            end = time.clock()
            totaltime += end - start
        print("INVERTING 40x40 MATRIX WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_inversion_performance_30x30(self):
        """Test matrix inversion ten times with a random 30x30 matrix"""
        global n
        size = 30
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 30, 30)
            start = time.clock()
            calculator.matrixInverse(matrix)
            end = time.clock()
            totaltime += end - start
        print("INVERTING 30x30 MATRIX WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_inversion_performance_20x20(self):
        """Test matrix inversion ten times with a random 20x20 matrix"""
        global n
        size = 20
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 20, 20)
            start = time.clock()
            calculator.matrixInverse(matrix)
            end = time.clock()
            totaltime += end - start
        print("INVERTING 20x20 MATRIX WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_inversion_performance_10x10(self):
        """Test matrix inversion ten times with a random 10x10 matrix"""
        global n
        size = 10
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 10, 10)
            start = time.clock()
            calculator.matrixInverse(matrix)
            end = time.clock()
            totaltime += end - start
        print("INVERTING 10x10 MATRIX WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_determinant_performance_50x50(self):
        """Test matrix determinant ten times with a random 50x50 matrix"""
        global n
        size = 50
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 50, 50)
            start = time.clock()
            calculator.matrixDeterminant(matrix)
            end = time.clock()
            totaltime += end - start
        print("CALCULATING THE DETERMINANT OF A 50x50 "
              "MATRIX WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_determinant_performance_40x40(self):
        """Test matrix determinant ten times with a random 40x40 matrix"""
        global n
        size = 40
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 40, 40)
            start = time.clock()
            calculator.matrixDeterminant(matrix)
            end = time.clock()
            totaltime += end - start
        print("CALCULATING THE DETERMINANT OF A 40x40 "
              "MATRIX WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_determinant_performance_30x30(self):
        """Test matrix determinant ten times with a random 30x30 matrix"""
        global n
        size = 30
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 30, 30)
            start = time.clock()
            calculator.matrixDeterminant(matrix)
            end = time.clock()
            totaltime += end - start
        print("CALCULATING THE DETERMINANT OF A 30x30 "
              "MATRIX WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_determinant_performance_20x20(self):
        """Test matrix determinant ten times with a random 20x20 matrix"""
        global n
        size = 20
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 20, 20)
            start = time.clock()
            calculator.matrixDeterminant(matrix)
            end = time.clock()
            totaltime += end - start
        print("CALCULATING THE DETERMINANT OF A 20x20 "
              "MATRIX WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_determinant_performance_10x10(self):
        """Test matrix determinant ten times with a random 10x10 matrix"""
        global n
        size = 10
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 10, 10)
            start = time.clock()
            calculator.matrixDeterminant(matrix)
            end = time.clock()
            totaltime += end - start
        print("CALCULATING THE DETERMINANT OF A 10x10 "
              "MATRIX WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_multiplication_performance_50x50(self):
        """Test matrix multiplication ten times with random 50x50 matrices"""
        global n
        size = 50
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 50, 50)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 50, 50)

            start = time.clock()
            calculator.matrixMultiplication(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("MULTIPLYING TWO 50x50 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_multiplication_performance_40x40(self):
        """Test matrix multiplication ten times with random 40x40 matrices"""
        global n
        size = 40
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 40, 40)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 40, 40)

            start = time.clock()
            calculator.matrixMultiplication(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("MULTIPLYING TWO 40x40 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_multiplication_performance_30x30(self):
        """Test matrix multiplication ten times with random 30x30 matrices"""
        global n
        size = 30
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 30, 30)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 30, 30)

            start = time.clock()
            calculator.matrixMultiplication(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("MULTIPLYING TWO 30x30 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_multiplication_performance_20x20(self):
        """Test matrix multiplication ten times with random 20x20 matrices"""
        global n
        size = 20
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 20, 20)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 20, 20)

            start = time.clock()
            calculator.matrixMultiplication(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("MULTIPLYING TWO 20x20 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_multiplication_performance_10x10(self):
        """Test matrix multiplication ten times with random 10x10 matrices"""
        global n
        size = 10
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 10, 10)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 10, 10)

            start = time.clock()
            calculator.matrixMultiplication(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("MULTIPLYING TWO 10x10 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_addition_performance_50x50(self):
        """Test matrix addition ten times with random 50x50 matrices"""
        global n
        size = 50
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 50, 50)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 50, 50)

            start = time.clock()
            calculator.matrixAddition(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("ADDING TWO 50x50 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_addition_performance_40x40(self):
        """Test matrix addition ten times with random 40x40 matrices"""
        global n
        size = 40
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 40, 40)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 40, 40)

            start = time.clock()
            calculator.matrixAddition(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("ADDING TWO 40x40 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_addition_performance_30x30(self):
        """Test matrix addition ten times with random 30x30 matrices"""
        global n
        size = 30
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 30, 30)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 30, 30)

            start = time.clock()
            calculator.matrixAddition(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("ADDING TWO 30x30 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_addition_performance_20x20(self):
        """Test matrix addition ten times with random 20x20 matrices"""
        global n
        size = 20
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 20, 20)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 20, 20)

            start = time.clock()
            calculator.matrixAddition(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("ADDING TWO 20x20 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_addition_performance_10x10(self):
        """Test matrix addition ten times with random 10x10 matrices"""
        global n
        size = 10
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 10, 10)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 10, 10)

            start = time.clock()
            calculator.matrixAddition(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("ADDING TWO 10x10 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_substraction_performance_50x50(self):
        """Test matrix substraction ten times with random 50x50 matrices"""
        global n
        size = 50
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 50, 50)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 50, 50)

            start = time.clock()
            calculator.matrixSubstraction(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("SUBSTRACTING TWO 50x50 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_substraction_performance_40x40(self):
        """Test matrix substraction ten times with random 40x40 matrices"""
        global n
        size = 40
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 40, 40)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 40, 40)

            start = time.clock()
            calculator.matrixSubstraction(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("SUBSTRACTING TWO 40x40 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_substraction_performance_30x30(self):
        """Test matrix substraction ten times with random 30x30 matrices"""
        global n
        size = 30
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 30, 30)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 30, 30)

            start = time.clock()
            calculator.matrixSubstraction(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("SUBSTRACTING TWO 30x30 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_substraction_performance_20x20(self):
        """Test matrix substraction ten times with random 20x20 matrices"""
        global n
        size = 20
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 20, 20)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 20, 20)

            start = time.clock()
            calculator.matrixSubstraction(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("SUBSTRACTING TWO 20x20 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")

    def test_matrix_substraction_performance_10x10(self):
        """Test matrix substraction ten times with random 10x10 matrices"""
        global n
        size = 10
        totaltime = 0
        for i in range(n):
            matrix = self.__random_n_by_m_array(size, size, -10, 10)
            matrix = Matrix(matrix, 10, 10)
            matrix2 = self.__random_n_by_m_array(size, size, -10, 10)
            matrix2 = Matrix(matrix2, 10, 10)

            start = time.clock()
            calculator.matrixSubstraction(matrix, matrix2)
            end = time.clock()
            totaltime += end - start
        print("SUBSTRACTING TWO 10x10 MATRICES WITH VALUES IN RANGE [-10, 10]")
        print("  total time: " + str(totaltime*1000) + "ms")
        print("average time: " + str(totaltime*1000.0/n) + "ms")
        print("")


if __name__ == '__main__':
    unittest.main()
