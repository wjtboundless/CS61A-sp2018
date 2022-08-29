
class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8

        def __init__(self, value=0):
        self.value = value
        self.pre_value_close = 0
        self.pre_value_far = 0

    def next(self):
        "*** YOUR CODE HERE ***"
        if self.value == 0:
            self.pre_value_close = self.value
            self.value = 1
            return self
        else:
            self.pre_value_far = self.pre_value_close
            self.pre_value_close = self.value
            self.value = self.pre_value_close + self.pre_value_far
            return self
        
    def __repr__(self):
        return str(self.value)
    """
    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** YOUR CODE HERE ***"
        if self.value == 0:
            next_fib = Fib(1)
        else:
            next_fib = Fib(self.previous + self.value)
        next_fib.previous = self.value
        return next_fib

    def __repr__(self):
        return str(self.value)


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.stock = 0
        self.balance = 0

    def vend(self):
        if self.stock < 1:
            return 'Machine is out of stock.'
        else:
            if self.balance < self.price:
                return 'You must deposit ${0} more.'.format(self.price - self.balance)
            else:
                self.stock -= 1
                if self.balance == self.price:
                    return 'Here is your {0}.'.format(self.item)
                    
                else:
                    self.change = self.balance - self.price
                    self.balance = 0
                    return 'Here is your {0} and ${1} change.'.format(self.item, self.change)
                    
    def restock(self, num):
        self.stock += num
        return 'Current {0} stock: {1}'.format(self.item, self.stock)
    
    def deposit(self, money):
        if self.stock < 1:
            return 'Machine is out of stock. Here is your ${0}.'.format(money)
        else:
            self.balance += money
            return 'Current balance: ${0}'.format(self.balance)