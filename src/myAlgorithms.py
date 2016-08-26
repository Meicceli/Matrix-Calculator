def my_abs(n):
    """Calculate the absolute value of a given number."""
    if n < 0:
        return -n
    return n


def my_gcd(n, m):
    """Calculate the gcd of n and m using Stein's algorithm.

    For a description of Stein's algorithm, see for example
    https://en.wikipedia.org/wiki/Binary_GCD_algorithm
    """

    # Unit is needed to mimic the default Python's implementation of gcd. Python
    # thinks that if m < 0, then the gcd shall be negative.
    unit = 1
    if m < 0:
        unit = -1
    n = my_abs(n)
    m = my_abs(m)

    # Base cases.
    if n == m == 0:
        return 0
    if n == 0:
        return unit * m
    if m == 0:
        return n
    if n == m:
        return unit * n

    # For convenience, make sure n is the bigger one of the two.
    if n < m:
        n, m = m, n

    # The power of two that divides both n and m, i.e. if 8==2^3 divides n and m
    # but 16==2^4 doesn't, then exp will be set to 3.
    exp = 0
    # While n and m are both even, divide both by 2, and add one to exp.
    while (n | m) & 1 == 0:
        n >>= 1
        m >>= 1
        exp += 1

    # Remove leftover factors of 2 from n. This can be done since m is odd and
    # so has no factors of 2.
    while n & 1 == 0:
        n >>= 1

    while n != 0:
        # Again, remove any leftover factors of 2 from n since m now always
        # remains odd.
        while n & 1 == 0:
            n >>= 1
        # Here we ensure that n is always the bigger of the two. Thus n will be
        # positive until n == m.
        if n < m:
            n, m = m, n
        n -= m

    # At this point, n == 0 and hence gcd(n, m) == m. Multiply the resulting m
    # by 2^exp, which is also a common factor of the original n and m.
    return unit * (m << exp)


def my_max(x, *args):
    """Return the maximum of the given numbers or a given list."""

    # If x is a non-empty list, find the maximum value in it.
    if isinstance(x, list) and len(x) > 0:
        greatest = x[0]
        i = 0
        while i < len(x):
            # The list x must contain only numbers (floats and/or integeres.)
            if not (isinstance(x[i], float) or isinstance(x[i], int)):
                raise TypeError('Expected an integer or a float.')
            if x[i] > x[0]:
                greatest = x[i]
            i += 1
        return greatest

    # If x is a number (float/integer), find the maximum of the given
    # n-arguments.
    if isinstance(x, float) or isinstance(x, int):
        greatest = x
        i = 0
        # Iterate through the rest of the arguments given by the user.
        while i < len(args):
            # All arguments must be numbers.
            if not (isinstance(args[i], float) or isinstance(args[i], int)):
                raise TypeError('Expected an integer or a float.')
            if args[i] > x:
                greatest = args[i]
            i += 1
        return greatest

    raise TypeError(
        'Expected a list of ints/floats, or a sequence of ints/floats')


def my_range(x, *args):
    """Return a list of integers, mimicing the default range() call."""
    # By default, the lower bound is zero.
    lower = 0
    # By default, the upper bound is x.
    upper = x

    # User gave two arguments i.e. user gave also a lower bound. Then x is the
    # lower-bound and the second argument (args[0]) is the upper bound.
    if len(args) == 1:
        lower = x
        upper = args[0]

    # Here we generate the range.
    ret = []
    i = lower
    while i < upper:
        ret.append(i)
        i += 1

    return ret


def my_reversed(x):
    """Reverse a list."""

    # Copy the elements of x to ret, starting from the end of x.
    ret = []
    i = len(x) - 1
    while i >= 0:
        ret.append(x[i])
        i -= 1
    return ret


def my_split(s, char):
    pass


def my_strip(s):
    pass


def my_lower(s):
    pass
