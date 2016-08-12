from parser import Matrix


def matrixAddition(A, B):
    """Add matrix B to matrix A if the sum matrix is defined."""

    if A.getColAmount() != B.getColAmount():
        return -1
    if A.getRowAmount() != B.getRowAmount():
        return -1

    C = []
    for rowIndex in range(A.getRowAmount()):
        resultRow = []
        for colIndex in range(A.getColAmount()):
            cellOfA = A.getCell(rowIndex, colIndex)
            cellOfB = B.getCell(rowIndex, colIndex)
            resultRow.append(cellOfA + cellOfB)
        C.append(resultRow)

    return Matrix(C, A.getRowAmount(), A.getColAmount())


def matrixSubstraction(A, B):
    """Substract matrix B from A if the difference is defined."""

    # Special case
    if A == B:
        return Matrix(
            [[0 for i in range(A.getColAmount())]
             for j in range(A.getRowAmount())],
            A.getRowAmount(),
            A.getColAmount())
    B.multiplyScalar(-1)
    resultMatrix = matrixAddition(A, B)
    B.multiplyScalar(-1)
    return resultMatrix


def matrixScalarMultiplication(A, scalar):
    """Multiply a matrix by a scalar"""
    A.multiplyScalar(scalar)
    return A


def matrixMultplication(A, B):
    """Multiply two matrices if the product is defined."""

    if A.getColAmount() != B.getRowAmount():
        return -1

    n = A.getRowAmount()
    m = A.getColAmount()
    p = B.getColAmount()
    C = [[0 for i in range(p)] for j in range(n)]

    for i in range(n):
        for j in range(p):
            cellValue = 0
            for k in range(m):
                cellValue += A.getCell(i, k) * B.getCell(k, j)
            C[i][j] = cellValue

    return Matrix(C, n, p)


def __LU_decomposition(A):
    L = [[0 for col in range(A.getColAmount())]
         for row in range(A.getRowAmount())]
    for i in range(A.getRowAmount()):
        L[i][i] = 1

    # A copy of A's rows
    U = A.getRowArray()

    for col in range(A.getColAmount()):
        for row in range(1+col, A.getRowAmount()):
            zeroWithThis = U[col][col]
            valueToZero = U[row][col]
            multiplier = 0
            if zeroWithThis != 0:
                multiplier = -1.0 * valueToZero / zeroWithThis

            L[row][col] = -multiplier

            for i in range(A.getColAmount()):
                U[row][i] = U[row][i] + multiplier * U[col][i]
    return (Matrix(L, A.getRowAmount(), A.getColAmount()),
            Matrix(U, A.getRowAmount(), A.getColAmount()))


def matrixDeterminant(A):
    if (A.getRowAmount() != A.getColAmount()):
        return "ERRORRRRRR"

    decomposition = __LU_decomposition(A)
    U = decomposition[1]
    determinant = 1
    for i in range(A.getRowAmount()):
        determinant *= U.getCell(i, i)

    return determinant


def __forward_substitution(L):
    m = L.getColAmount()
    inverse = [[0 for i in range(m)]
               for j in range(m)]

    for a in range(m):
        bVector = [0 for i in range(m)]
        bVector[a] = 1

        xVector = []
        for x in range(m):
            stuff = 0
            for i in range(x):
                stuff += L.getCell(x, i) * xVector[i]
            value = bVector[x] - stuff
            value /= L.getCell(x, x)
            xVector.append(value)

        for i in range(m):
            inverse[i][a] = xVector[i]

    return Matrix(inverse, m, m)


def __backward_substitution(L):
    m = L.getColAmount()
    inverse = [[0 for i in range(m)]
               for j in range(m)]

    for a in range(m):
        bVector = [0 for i in range(m)]
        bVector[a] = 1

        xVector = []
        for x in reversed(range(m)):
            stuff = 0
            for i in reversed(range(x+1, m)):
                stuff += L.getCell(x, i) * xVector[m-1 - i]
            value = bVector[x] - stuff
            value /= L.getCell(x, x)
            xVector.append(value)

        for i in range(m):
            inverse[m-1-i][a] = xVector[i]

    return Matrix(inverse, m, m)


def matrixInverse(A):
    decomposition = __LU_decomposition(A)
    L = decomposition[0]
    U = decomposition[1]
    return matrixMultplication(__backward_substitution(U),
                               __forward_substitution(L))


if __name__ == '__main__':
    matrix = Matrix([[8, -9, -2, -5],
                     [9, 6, -6, 9],
                     [-3, -9, 4, -2],
                     [0, -7, 8, 8]], 4, 4)
    print(matrixInverse(matrix))
