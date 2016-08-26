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


def __reduce_fraction(frac):
    """Reduce the given fraction."""
    # Calculate the gcd of the numerator and denominator.
    syt = my_gcd(frac[0], frac[1])
    # This condition here ensures we don't end up dividing by 0. Namely, in
    # Python gcd(0, 0) == 0.
    if syt == 0:
        syt = 1
    # Floor divide the numerator and denominator by syt. We can safely floor
    # divide, because by the definition of gcd, syt divides frac[0] and frac[1].
    # Floor division then ensures frac[0] // syt is an integer, since in Python
    # 3, x / y is by default a float.
    return (frac[0] // syt, frac[1] // syt)


def __pivot(A):
    """Pivot A so that largest element of each column is on the diagonal."""
    n = A.getRowAmount()

    # At first, P is the identity matrix.
    P = [[int(i == j) for i in my_range(n)] for j in my_range(n)]

    # Store the number of times pivoting is needed here.
    totalPivots = 0
    # Iterate through columns.
    for j in my_range(n):
        greatest = 0
        swapWith = j

        # We don't have to care about column values above the diagonal.
        for row in my_range(j+1, n):
            if my_abs(A.getCell(row, j)) > greatest:
                greatest = my_abs(A.getCell(row, j))
                swapWith = row

        # True if we need to swap rows.
        if swapWith != j:
            # Swap rows so that the greatest element is now on the diagonal.
            P[j], P[swapWith] = P[swapWith], P[j]
            totalPivots += 1

    return (Matrix(P, n, n), totalPivots)


def __LUP_decomposition(A):
    """Calculate the LUP decomposition of A."""
    n = A.getRowAmount()

    # Format L and U as the zero matrix. Note that we are dealing with fractions
    # here for 100% accuracy.
    L = [[(0, 1) for i in my_range(n)] for j in my_range(n)]
    U = [[(0, 1) for i in my_range(n)] for j in my_range(n)]

    # Pivot A.
    pivot_info = __pivot(A)
    P = pivot_info[0]

    # Set mult equal to the determinant of P.
    mult = pivot_info[1]
    if mult % 2 == 0:
        mult = 1
    else:
        mult = -1

    # This is the matrix P*A
    Prod = matrixMultiplication(P, A)

    # We use the general algorithm described here:
    # https://rosettacode.org/wiki/LU_decomposition to calculate cell values for
    # U and L. There is a summation formula given for U_ij and L_ij, which is
    # implemented here.
    for j in my_range(n):
        # Calculate U[i][j].
        for i in my_range(j+1):
            the_sum = (0, 1)

            for k in my_range(i):
                # U_kj + L_ik
                toAdd = (U[k][j][0] * L[i][k][0],
                         U[k][j][1] * L[i][k][1])
                # Add the fraction toAdd into the_sum
                the_sum = (the_sum[0] * toAdd[1] + toAdd[0] * the_sum[1],
                           the_sum[1] * toAdd[1])

            the_sum = __reduce_fraction(the_sum)
            # U_ij == Prod_ij - the_sum
            U[i][j] = (Prod.getCell(i, j) * the_sum[1] - the_sum[0], the_sum[1])

        # Calculate L[i][j], similarly as U[i][j].
        for i in my_range(j, n):
            the_sum = (0, 1)

            for k in my_range(j):
                toAdd = (L[i][k][0] * U[k][j][0],
                         L[i][k][1] * U[k][j][1])
                the_sum = (the_sum[0] * toAdd[1] + toAdd[0] * the_sum[1],
                           the_sum[1] * toAdd[1])

            the_sum = __reduce_fraction(the_sum)
            L[i][j] = (Prod.getCell(i, j) * the_sum[1] - the_sum[0], the_sum[1])
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
    """Invert L using forward substitution.

    For more information, see for example
    en.wikipedia.org/wiki/Triangular_matrix#Forward_and_back_substitution """
    m = len(L[0])
    inverse = [[(0, 1) for i in my_range(m)] for j in my_range(m)]

    # bVector is the a:th column of the identity matrix. Solve the a:th column
    # of the inverse of L.
    for a in my_range(m):
        bVector = [0 for i in my_range(m)]
        bVector[a] = 1

        # This will be the a:th column of the inverse matrix of L.
        xVector = []
        for x in my_range(m):
            # Calculate the summation of x_index using the formula given for x_m
            # in the article above.
            the_sum = (0, 1)

            for i in my_range(x):
                toAdd = (L[x][i][0] * xVector[i][0],
                         L[x][i][1] * xVector[i][1])
                the_sum = (the_sum[0] * toAdd[1] + toAdd[0] * the_sum[1],
                           the_sum[1] * toAdd[1])

            the_sum = __reduce_fraction(the_sum)
            value = (bVector[x] * the_sum[1] - the_sum[0], the_sum[1])
            value = (value[0] * L[x][x][1], value[1] * L[x][x][0])
            value = __reduce_fraction(value)
            xVector.append(value)

        # xVector is now the a:th column of L's inverse.
        for i in my_range(m):
            inverse[i][a] = xVector[i]

    return inverse


def __backward_substitution(U):
    """Invert U using backward substitution.

    This is basically the same as forward substitution, but done working
    backwards."""
    m = len(U[0])
    inverse = [[(0, 1) for i in my_range(m)]
               for j in my_range(m)]

    for a in my_range(m):
        bVector = [0 for i in my_range(m)]
        bVector[a] = 1

        xVector = []
        for x in my_reversed(my_range(m)):
            stuff = (0, 1)

            for i in my_reversed(my_range(x+1, m)):
                toAdd = (U[x][i][0] * xVector[m-1 - i][0],
                         U[x][i][1] * xVector[m-1 - i][1])
                stuff = (stuff[0] * toAdd[1] + toAdd[0] * stuff[1],
                         stuff[1] * toAdd[1])

            stuff = __reduce_fraction(stuff)
            value = (bVector[x] * stuff[1] - stuff[0], stuff[1])
            value = (value[0] * U[x][x][1], value[1] * U[x][x][0])
            value = __reduce_fraction(value)
            xVector.append(value)

        for i in my_range(m):
            inverse[m-1-i][a] = xVector[i]

    return inverse


def accurateMatrixInverse(A):
    """Inverse A with 100% accuracy"""
    # Inverse not defined iff the determinant is zero.
    if matrixDeterminant(A) == 0:
        return None

    # Calculate the LUP decomposition of A.
    decomposition = __LUP_decomposition(A)

    # Inverse L using forward substitution.
    L = __forward_substitution(decomposition[0])
    # Inverse U using forward substitution.
    U = __backward_substitution(decomposition[1])
    P = decomposition[2]
    n = A.getRowAmount()

    # Calculate the product of L^-1 and U^-1 here.
    C = [[0 for i in my_range(n)] for j in my_range(n)]

    # Do the multiplication.
    for i in my_range(n):
        for j in my_range(n):
            cellValue = (0, 1)

            for k in my_range(n):
                toAdd = (U[i][k][0] * L[k][j][0],
                         U[i][k][1] * L[k][j][1])
                cellValue = (cellValue[0] * toAdd[1] + toAdd[0] * cellValue[1],
                             cellValue[1] * toAdd[1])

            cellValue = __reduce_fraction(cellValue)
            C[i][j] = cellValue

    # Result is L^-1 * U^-1 = C times the inverse of P. We use the fact that for
    # permutation matrices, P^-1 == P^T i.e. the inverse of P is it's transpose.
    # So we multiply C by the transpose of P.
    Result = [[0 for i in my_range(n)] for j in my_range(n)]
    for i in my_range(n):
        for j in my_range(n):
            cellValue = 0
            for k in my_range(n):
                # Note the order of k and j. The order ensures we are
                # multiplying by the transpose of P, and not with P.
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
