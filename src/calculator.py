from parser import Matrix
from fractions import gcd


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
    L = [[(0, 1) for col in range(A.getColAmount())]
         for row in range(A.getRowAmount())]
    for i in range(A.getRowAmount()):
        L[i][i] = (1, 1)

    # A copy of A's rows
    U = [[(A.getCell(row, col), 1) for col in range(A.getColAmount())]
         for row in range(A.getRowAmount())]

    for col in range(A.getColAmount()):
        for row in range(1+col, A.getRowAmount()):
            zeroWithThis = U[col][col]
            valueToZero = U[row][col]
            multiplier = (0, 1)
            if zeroWithThis[0] != 0:
                multiplier = (-1 * valueToZero[0] * zeroWithThis[1],
                              zeroWithThis[0] * valueToZero[1])

            L[row][col] = (-1 * multiplier[0], multiplier[1])

            for i in range(A.getColAmount()):
                toAdd = (multiplier[0] * U[col][i][0],
                         multiplier[1] * U[col][i][1])
                numerator = toAdd[0] * U[row][i][1] + U[row][i][0] * toAdd[1]
                denumerator = U[row][i][1] * toAdd[1]
                U[row][i] = (numerator, denumerator)

    """
    for row in range(A.getRowAmount()):
        for col in range(A.getColAmount()):
            syt = gcd(U[row][col][0], U[row][col][1])
            U[row][col] = (U[row][col][0] / syt) * 1.0 / (U[row][col][1] / syt)

            syt = gcd(L[row][col][0], L[row][col][1])
            L[row][col] = (L[row][col][0] / syt) * 1.0 / (L[row][col][1] / syt)
    """

    return (L, U)


def matrixDeterminant(A):
    """Calculate the determinant of A"""
    if (A.getRowAmount() != A.getColAmount()):
        return "ERRORRRRRR"

    decomposition = __LU_decomposition(A)
    U = decomposition[1]
    determinant = (1, 1)
    for i in range(A.getRowAmount()):
        syt = gcd(U[i][i][0], U[i][i][1])
        determinant = (determinant[0] * U[i][i][0] // syt,
                       determinant[1] * U[i][i][1] // syt)

    return determinant[0] // determinant[1]


def __forward_substitution(L):
    m = len(L[0])
    inverse = [[(0, 1) for i in range(m)]
               for j in range(m)]

    for a in range(m):
        bVector = [0 for i in range(m)]
        bVector[a] = 1

        xVector = []
        for x in range(m):
            stuff = (0, 1)
            for i in range(x):
                toAdd = (L[x][i][0] * xVector[i][0],
                         L[x][i][1] * xVector[i][1])
                stuff = (stuff[0] * toAdd[1] + toAdd[0] * stuff[1],
                         stuff[1] * toAdd[1])
            value = (bVector[x] * stuff[1] - stuff[0], stuff[1])
            value = (value[0] * L[x][x][1], value[1] * L[x][x][0])
            xVector.append(value)

        for i in range(m):
            inverse[i][a] = xVector[i]

    return inverse


def __backward_substitution(L):
    m = len(L[0])
    inverse = [[(0, 1) for i in range(m)]
               for j in range(m)]

    for a in range(m):
        bVector = [0 for i in range(m)]
        bVector[a] = 1

        xVector = []
        for x in reversed(range(m)):
            stuff = (0, 1)
            for i in reversed(range(x+1, m)):
                toAdd = (L[x][i][0] * xVector[m-1 - i][0],
                         L[x][i][1] * xVector[m-1 - i][1])
                stuff = (stuff[0] * toAdd[1] + toAdd[0] * stuff[1],
                         stuff[1] * toAdd[1])
            value = (bVector[x] * stuff[1] - stuff[0], stuff[1])
            value = (value[0] * L[x][x][1], value[1] * L[x][x][0])
            if value[1] == 0:
                value = (0, 1)
            xVector.append(value)

        for i in range(m):
            inverse[m-1-i][a] = xVector[i]

    return inverse


def accurateMatrixInverse(A):
    """Inverse A with 100% accuracy"""
    decomposition = __LU_decomposition(A)
    L = __forward_substitution(decomposition[0])
    U = __backward_substitution(decomposition[1])

    n = A.getRowAmount()

    C = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            cellValue = (0, 1)
            for k in range(n):
                toAdd = (U[i][k][0] * L[k][j][0],
                         U[i][k][1] * L[k][j][1])
                cellValue = (cellValue[0] * toAdd[1] + toAdd[0] * cellValue[1],
                             cellValue[1] * toAdd[1])
                syt = max(1, gcd(cellValue[0], cellValue[1]))
                cellValue = (cellValue[0] // syt, cellValue[1] // syt)
            C[i][j] = cellValue

    return C


def matrixInverse(A):
    """Invert matrix A"""
    n = A.getRowAmount()
    m = A.getColAmount()
    if n != m:
        return "ARRRRGHHHHH"
    if n == 1:
        return Matrix([[1/A.getCell(0, 0)]], 1, 1)

    accInverse = accurateMatrixInverse(A)
    inverse = [[0 for i in range(n)] for j in range(n)]
    for row in range(n):
        for col in range(n):
            inverse[row][col] = accInverse[row][col][0]
            inverse[row][col] /= accInverse[row][col][1]

    return Matrix(inverse, n, n)


if __name__ == '__main__':
    matrix = Matrix([[8, -9, -2, -5],
                     [9, 6, -6, 9],
                     [-3, -9, 4, -2],
                     [0, -7, 8, 8]], 4, 4)
    print(matrixInverse(matrix))
