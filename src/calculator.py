from .parser import Matrix
from .myAlgorithms import my_gcd, my_abs, my_range, my_reversed


def matrixAddition(A, B):
    """Add matrix B to matrix A if the sum matrix is defined."""

    # Addition undefined.
    if A.getColAmount() != B.getColAmount():
        return None
    # Addition undefined.
    if A.getRowAmount() != B.getRowAmount():
        return None

    # Resulting matrix.
    C = []
    for rowIndex in my_range(A.getRowAmount()):
        resultRow = []
        for colIndex in my_range(A.getColAmount()):
            cellOfA = A.getCell(rowIndex, colIndex)
            cellOfB = B.getCell(rowIndex, colIndex)
            resultRow.append(cellOfA + cellOfB)
        C.append(resultRow)

    return Matrix(C, A.getRowAmount(), A.getColAmount())


def matrixSubstraction(A, B):
    """Substract matrix B from A if the difference is defined."""

    # A very special case that should never happen (expect in my tests).
    if A == B:
        # Return a zero matrix of the same size as A.
        return Matrix(
            [[0 for i in my_range(A.getColAmount())]
             for j in my_range(A.getRowAmount())],
            A.getRowAmount(),
            A.getColAmount())

    # Multiply B by a scalar of -1. This is because A-B == A+(-1*B).
    B.multiplyScalar(-1)
    resultMatrix = matrixAddition(A, B)

    # Set B's scalar back to original.
    B.multiplyScalar(-1)

    return resultMatrix


def matrixScalarMultiplication(A, scalar):
    """Multiply a matrix by a scalar."""
    A.multiplyScalar(scalar)
    return A


def matrixMultiplication(A, B):
    """Multiply two matrices if the product is defined."""

    # Multiplication is undefined if this condition holds.
    if A.getColAmount() != B.getRowAmount():
        return None

    n = A.getRowAmount()
    m = A.getColAmount()
    p = B.getColAmount()

    # This will be the result matrix.
    C = [[0 for i in my_range(p)] for j in my_range(n)]

    for i in my_range(n):
        for j in my_range(p):
            # calculate the value of C[i][j] here.
            cellValue = 0
            for k in my_range(m):
                cellValue += A.getCell(i, k) * B.getCell(k, j)
            C[i][j] = cellValue

    return Matrix(C, n, p)


def __pivot(A):
    n = A.getRowAmount()
    P = [[int(i == j) for i in my_range(n)] for j in my_range(n)]
    totalPivots = 0
    for j in my_range(n):
        suurin = 0
        swapWith = j

        for row in my_range(j, n):
            if my_abs(A.getCell(row, j)) > suurin:
                suurin = my_abs(A.getCell(row, j))
                swapWith = row

        if swapWith != j:
            P[j], P[swapWith] = P[swapWith], P[j]
            totalPivots += 1

    return (Matrix(P, n, n), totalPivots)


def __LUP_decomposition(A):
    """Calculate the LUP decomposition of A."""
    n = A.getRowAmount()
    L = [[(int(i == j), 1) for i in my_range(n)] for j in my_range(n)]
    U = [[(0, 1) for i in my_range(n)] for j in my_range(n)]
    lol = __pivot(A)
    P = lol[0]
    # mult == determinant of P
    mult = lol[1]
    if mult % 2 == 0:
        mult = 1
    else:
        mult = -1
    Prod = matrixMultiplication(P, A)
    for j in my_range(n):
        for i in my_range(j+1):
            value = (0, 1)
            for k in my_range(i):
                toAdd = (L[i][k][0] * U[k][j][0],
                         L[i][k][1] * U[k][j][1])
                value = (value[0] * toAdd[1] + toAdd[0] * value[1],
                         value[1] * toAdd[1])
                syt = my_gcd(value[0], value[1])
                if syt == 0:
                    syt = 1
                value = (value[0] // syt, value[1] // syt)
            U[i][j] = (Prod.getCell(i, j) * value[1] - value[0], value[1])

        for i in my_range(j, n):
            value = (0, 1)
            for k in my_range(j):
                toAdd = (L[i][k][0] * U[k][j][0],
                         L[i][k][1] * U[k][j][1])
                value = (value[0] * toAdd[1] + toAdd[0] * value[1],
                         value[1] * toAdd[1])
                syt = my_gcd(value[0], value[1])
                if syt == 0:
                    syt = 1
                value = (value[0] // syt, value[1] // syt)
            L[i][j] = (Prod.getCell(i, j) * value[1] - value[0], value[1])
            L[i][j] = (L[i][j][0] * U[j][j][1], L[i][j][1] * U[j][j][0])

    return (L, U, P, mult)


def matrixDeterminant(A):
    """Calculate the determinant of A"""

    # Determinant is undefined is this condition holds.
    if A.getRowAmount() != A.getColAmount():
        return None

    # Decompose the matrix. Return value is (L, U, P, mult).
    decomposition = __LUP_decomposition(A)

    U = decomposition[1]

    # The determinant is the product of U's diagonal values. All values are
    # in pairs (x, y) representing a fraction. x is the nominator, and y the
    # denominator.
    ans = (1, 1)
    for i in my_range(len(U)):
        # Multiply ans by the fraction in U[i][i].
        ans = (ans[0] * U[i][i][0], ans[1] * U[i][i][1])

        # Reduce the fraction
        syt = my_gcd(ans[0], ans[1])
        if syt != 0 and syt != 1:
            ans = (ans[0] // syt, ans[1] // syt)

    # If the determinant is zero, ans[1] might also be zero so we treat this
    # case separately.
    if ans[1] == 0:
        return 0

    return ans[0] * decomposition[3] * 1.0 / ans[1]


def __forward_substitution(L):
    m = len(L[0])
    inverse = [[(0, 1) for i in my_range(m)]
               for j in my_range(m)]

    for a in my_range(m):
        bVector = [0 for i in my_range(m)]
        bVector[a] = 1

        xVector = []
        for x in my_range(m):
            stuff = (0, 1)
            for i in my_range(x):
                toAdd = (L[x][i][0] * xVector[i][0],
                         L[x][i][1] * xVector[i][1])
                stuff = (stuff[0] * toAdd[1] + toAdd[0] * stuff[1],
                         stuff[1] * toAdd[1])
                syt = my_gcd(stuff[0], stuff[1])
                if syt == 0:
                    syt = 1
                stuff = (stuff[0] // syt, stuff[1] // syt)
            value = (bVector[x] * stuff[1] - stuff[0], stuff[1])
            value = (value[0] * L[x][x][1], value[1] * L[x][x][0])
            syt = my_gcd(value[0], value[1])
            if syt == 0:
                syt = 1
            value = (value[0] // syt, value[1] // syt)
            xVector.append(value)

        for i in my_range(m):
            inverse[i][a] = xVector[i]

    return inverse


def __backward_substitution(L):
    m = len(L[0])
    inverse = [[(0, 1) for i in my_range(m)]
               for j in my_range(m)]

    for a in my_range(m):
        bVector = [0 for i in my_range(m)]
        bVector[a] = 1

        xVector = []
        for x in my_reversed(my_range(m)):
            stuff = (0, 1)
            for i in my_reversed(my_range(x+1, m)):
                toAdd = (L[x][i][0] * xVector[m-1 - i][0],
                         L[x][i][1] * xVector[m-1 - i][1])
                stuff = (stuff[0] * toAdd[1] + toAdd[0] * stuff[1],
                         stuff[1] * toAdd[1])
                syt = my_gcd(stuff[0], stuff[1])
                if syt == 0:
                    syt = 1
                stuff = (stuff[0] // syt, stuff[1] // syt)
            value = (bVector[x] * stuff[1] - stuff[0], stuff[1])
            value = (value[0] * L[x][x][1], value[1] * L[x][x][0])
            if value[1] == 0:
                value = (0, 1)
            syt = my_gcd(value[0], value[1])
            if syt == 0:
                syt = 1
            value = (value[0] // syt, value[1] // syt)
            xVector.append(value)

        for i in my_range(m):
            inverse[m-1-i][a] = xVector[i]

    return inverse


def accurateMatrixInverse(A):
    """Inverse A with 100% accuracy"""
    if matrixDeterminant(A) == 0:
        return None

    decomposition = __LUP_decomposition(A)

    L = __forward_substitution(decomposition[0])
    U = __backward_substitution(decomposition[1])
    P = decomposition[2]
    n = A.getRowAmount()

    C = [[0 for i in my_range(n)] for j in my_range(n)]

    for i in my_range(n):
        for j in my_range(n):
            cellValue = (0, 1)
            for k in my_range(n):
                toAdd = (U[i][k][0] * L[k][j][0],
                         U[i][k][1] * L[k][j][1])
                cellValue = (cellValue[0] * toAdd[1] + toAdd[0] * cellValue[1],
                             cellValue[1] * toAdd[1])
            syt = my_gcd(cellValue[0], cellValue[1])
            if syt == 0:
                syt = 1
            cellValue = (cellValue[0] // syt, cellValue[1] // syt)
            C[i][j] = cellValue

    Result = [[0 for i in my_range(n)] for j in my_range(n)]
    for i in my_range(n):
        for j in my_range(n):
            cellValue = 0
            for k in my_range(n):
                if P.getCell(k, j) == 1:
                    cellValue = C[i][k]
                    break
            Result[i][j] = cellValue
    return Result


def matrixInverse(A):
    """Invert matrix A"""
    n = A.getRowAmount()
    m = A.getColAmount()

    # A is not a square matrix, so it cannot be inverted.
    if n != m:
        return None

    # A is a 1x1 matrix. Treat this as a special case.
    if n == 1:
        return Matrix([[1.0 / A.getCell(0, 0)]], 1, 1)

    # Accurately inverse the matrix, i.e. invert using fractions instead of
    # floats.
    accInverse = accurateMatrixInverse(A)

    # Matrix cannot be inverted (it's singular)
    if not accInverse:
        return None

    # Calculate the result here. The for loops turn fractions into floats.
    inverse = [[0 for i in my_range(n)] for j in my_range(n)]
    for row in my_range(n):
        for col in my_range(n):
            inverse[row][col] = accInverse[row][col][0]
            inverse[row][col] /= 1.0 * accInverse[row][col][1]

    return Matrix(inverse, n, n)
