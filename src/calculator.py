from parser import Matrix


def matrixAddition(A, B):
    """Add matrix B to matrix A if the sum matrix is defined."""

    if A.colAmount != B.colAmount or A.rowAmount != B.rowAmount:
        return -1

    C = []
    for rowIndex in range(A.rowAmount):
        resultRow = []
        for colIndex in range(A.colAmount):
            cellOfA = A.getCell(rowIndex, colIndex)
            cellOfB = B.getCell(rowIndex, colIndex)
            resultRow.append(cellOfA + cellOfB)
        C.append(resultRow)

    return Matrix(C, A.rowAmount, A.colAmount)


def matrixSubstraction(A, B):
    """Substract matrix B from A if the difference is defined."""

    # Special case
    if A == B:
        return Matrix([[0 for i in range(A.colAmount)]
                       for j in range(A.rowAmount)], A.rowAmount, A.colAmount)
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

    if A.colAmount != B.rowAmount:
        return -1

    n = A.rowAmount
    m = A.colAmount
    p = B.colAmount
    C = [[0 for i in range(p)] for j in range(n)]

    for i in range(n):
        for j in range(p):
            cellValue = 0
            for k in range(m):
                cellValue += A.getCell(i, k) * B.getCell(k, j)
            C[i][j] = cellValue

    return Matrix(C, n, p)


def matrixDeterminant(A):
    """TODO"""
    return -1
