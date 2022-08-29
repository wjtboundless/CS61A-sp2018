""" Lab 3: Recursion and Midterm Review """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.
    
    if a % b == 0:
        return b
    elif b > a:
        return gcd(b, a)
    else:
        return gcd(a - b, b)

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if b == 0:
        return a
    return gcd(b, a % b)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence. If n is even, divide it by 2. 
    If n is odd, multiply it by 3 and add 1. Repeat this process until 
    n is 1.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return hailstone(n//2) + 1
    return hailstone(3 * n + 1) + 1