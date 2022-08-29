""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def g(n):
        def h(x):
            m = 1
            while m <= n:
                if m % 3 == 1:
                    x = f1(x)
                elif m % 3 == 2:
                    x = f2(x)
                else:
                    x = f3(x)
                m += 1
            return x
              
        return h
    return g

## Lambda expressions
def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: x % 10 + y * 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2 or n == 1:
        return n
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    def check(i):
        if i == n:
            return True
        if n % i == 0:
            return False
        return check(i + 1)
    return check(2)

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    """if n == 0:
        return 0
    elif n % 2 == 1:
        return interleaved_sum(n-1, odd_term, even_term) + odd_term(n)
    else:
        return interleaved_sum(n-1, odd_term, even_term) + even_term(n)
    """
    def sum_from_1_to_n(i, n, odd_term, even_term):
        if i == n + 1:
            return 0
        elif i < n:
            return odd_term(i) + even_term(i + 1) + sum_from_1_to_n(i + 2, n, odd_term, even_term)
        else: # i == n
            return odd_term(i) + sum_from_1_to_n(i + 1, n, odd_term, even_term)
    return sum_from_1_to_n(1, n, odd_term, even_term)
    

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def count():
        pair_number = 0
        list_n = [int(x) for x in str(n)]
        for i in list_n:
            index = 0
            while index < len(list_n):
                if list_n[index] + i == 10 and list_n.index(i) != index:
                    pair_number += 1    
                index += 1
        return pair_number// 2
    return count()

    """def count_digits(m, k):
        if m == 0:
            return 0
        elif m % 10 == k:
            return count_digits(m // 10, k) + 1
        return count_digits(m // 10, k)
    return count_digits(n, 5) * (count_digits(n, 5) - 1) // 2\
        + count_digits(n, 1) * count_digits(n, 9)\
        + count_digits(n, 2) * count_digits(n, 8)\
        + count_digits(n, 3) * count_digits(n, 7)\
        + count_digits(n, 4) * count_digits(n, 6)
    """
    