"""Lab 1: Expressions and Control Structures"""

# Coding Practice
from math import prod


def square(x):
    return x * x

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    "*** YOUR CODE HERE ***"
    while n > 0:
        n -= 1
        x = f(x)
    return repeated(f, n, x)
    print(x)

def sum_digits_recur(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits_recur(all_but_last) + last

def sum_digits(n):
    sum = 0
    while n > 0:
        n, last = n //10, n % 10
        sum += last
    return sum

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    if n < 88:
        return False 
    else:
        while n > 0:
            n, last = n // 10, n % 10
            new_last = n % 10
            if last & new_last == 8:
                return True
        return False    


def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    if x > 0 and y > 0:
        return True
    return False
         


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    else:
        product = 1
        while k > 0: 
            product = product * (n - k + 1)
            k -= 1
        print(product)


         