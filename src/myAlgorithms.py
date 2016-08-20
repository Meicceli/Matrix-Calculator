def my_abs(n):
    if n < 0:
        return -n
    return n


def my_gcd(n, m):
    """Calculate the gcd of two numbers using the Euclidean algorithm."""
    if n == m == 0:
        return 0
    if n == 0:
        return m
    if m == 0:
        return n

    unit = 1
    if m < 0:
        unit = -1

    n = my_abs(n)
    m = my_abs(m)
    while n != m:
        if n > m:
            n -= m
        else:
            m -= n

    return n * unit


def my_max(x, *args):
    if isinstance(x, list) and len(x) > 0:
        greatest = x[0]
        i = 0
        while i < len(x):
            if not (isinstance(x[i], float) or isinstance(x[i], int)):
                raise TypeError('Expected an integer or a float.')
            if x[i] > x[0]:
                greatest = x[i]
            i += 1
        return greatest

    if isinstance(x, float) or isinstance(x, int):
        greatest = x
        i = 0
        while i < len(args):
            if not (isinstance(args[i], float) or isinstance(args[i], int)):
                raise TypeError('Expected an integer or a float.')
            if x < args[i]:
                greatest = args[i]
            i += 1
        return greatest

    raise TypeError(
        'Expected a list of ints/floats, or a sequence of ints/floats')


def my_range(x, *args):
    lower = 0
    upper = x
    if len(args) == 1:
        lower = x
        upper = args[0]

    ret = []
    i = lower
    while i < upper:
        ret.append(i)
        i += 1

    return ret


def my_reversed(x):
    ret = []
    i = len(x) - 1
    while i >= 0:
        ret.append(x[i])
        i -= 1
    return ret
