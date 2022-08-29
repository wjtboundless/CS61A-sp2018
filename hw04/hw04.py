HW_SOURCE_FILE = 'hw04.py'
import math
###############
#  Questions  #
###############

#Q1
def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b))

#Q2
def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    perfect_squares = []
    for i in s:
        if math.sqrt(i) == round(math.sqrt(i)):
            return perfect_squares + math.sqrt(i)
    #return [round(i ** 0.5) for i in s if i ** 0.5 == round(i ** 0.5)]

#Q3
def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    return g(n - 1) + 2 * g(n - 2) + 3 * (n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    g = [1, 2, 3]
    for i in range(3, n):
        g.append(g[i-1] + 2*g[i-2] + 3*g[i-3])
    return g[n-1]


#Q4
def pingpong(n):
    """The ping-pong sequence counts up starting from 1 and is 
    always either counting up or counting down. 
    At element k, the direction switches if k is a multiple of 
    7 or contains the digit 7. 
    Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def pingpong_helper(i, direction, value):
        if i == n:
            return value
        if multiple_of_7(i) or contain_7(i):
            return pingpong_helper(i + 1, -direction, value + direction)
        else:
            return pingpong_helper(i + 1, direction, value + direction)
    return pingpong_helper(1, 1, 1)

def multiple_of_7(k):
    if k % 7 == 0:
        return True
    return False

def contain_7(k):
    if k < 7:
        return False
    k, last = k // 10, k % 10
    if last == 7:
        return True
    return contain_7(k)

""" #Iteration
def pingpong(n):
    i, curr, direction = 1, 1, 1
    while i < n:
        if i % 7 == 0 or has_seven(i):
            direction = -direction
        curr += direction
        i += 1
    return curr

#Alternate solution 1
def pingpong_next(x, i, step):
    if i == n:
        return x
    return pingpong_next(x + step, i + 1, next_dir(step, i+1))

def next_dir(step, i):
    if i % 7 == 0 or has_seven(i):
        return -step
    return step

return pingpong_next(1, 1, 1)

# Alternate solution 2 ???
def pingpong(n):
    if n <= 7:
        return n
    return direction(n) + pingpong(n-1)

def direction(n):
    if n < 7:
        return 1
    if (n-1) % 7 == 0 or has_seven(n-1):
        return -1 * direction(n-1)
    return direction(n-1)

"""
#Q5
def count_change(amount):
    """Return the number of ways to make change for amount.
    e.g. make change for 7:

    7 1-cent coins
    5 1-cent, 1 2-cent coins
    3 1-cent, 2 2-cent coins
    3 1-cent, 1 4-cent coins
    1 1-cent, 3 2-cent coins
    1 1-cent, 1 2-cent, 1 4-cent coins

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def biggest_coin(amount):
            coin = 1
            while coin <= amount:
                coin *= 2
            return  coin // 2

    def count_helper(amount, biggest_coin):
        if biggest_coin == 0 or amount < 0:
            return 0
        elif amount == 0:
            return 1
        else:
            return count_helper(amount-biggest_coin, biggest_coin) + count_helper(amount, biggest_coin//2)
            
    return count_helper(amount, biggest_coin(amount))

        

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True

     def function(x, function):
         if(x == 1):
             return 1
         else:
             return function(x - 1, function) * x
     return lambda n : function(n, function)
    """
    return lambda n: (lambda f, n: f(f, n))(lambda s, x: x*s(s, x-1) if x > 0 else 1, n)
    
    # Alternate solutions:
    #   return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))
    #   return (lambda f: f(f))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))