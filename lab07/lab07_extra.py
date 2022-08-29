""" Optional Questions for Lab 07 """

from lab07 import *

# Q6
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>


    # returned version
    if link is Link.empty:
        return link
    else:
        filtered = remove_all(link.rest, value)
        if link.first != value:
            return Link(link.first, filtered)
        else:
            return filtered
    """
    "*** YOUR CODE HERE ***"
    p1, p2 = link, link.rest
    while p2 is not Link.empty:
        if p2.first == value:
            p1.rest = p2.rest
        else:
            p1 = p1.rest
        p2 = p2.rest



# Q7
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    while link is not Link.empty:
        if isinstance(link.first, int):
            link.first = fn(link.first)
        else:
            link.first.first = fn(link.first.first)
        link = link.rest
        

# Q8
def has_cycle(link):
    """Return whether link contains a cycle. Hint: Iterate through
     the linked list and try keeping track of which Link objects 
     you've already seen.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False


    if link is Link.empty:
        return False
    else:
        slow = link
        fast = link.rest
        while fast is not Link.empty:
            if fast.rest is Link.empty:
                return False
            slow = slow.rest
            fast = fast.rest.rest
            if slow is fast:
                return True
        return False
    """
    "*** YOUR CODE HERE ***"
    l = link
    while link.rest is not Link.empty:
        if link.rest is l:
            return True
        link = link.rest
    return False



def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    fast = slow = link
    while fast.rest is not Link.empty and fast.rest.rest is not Link.empty:
        slow = slow.rest
        fast = fast.rest.rest
        if fast == slow:
            return True
    return False

# Q9
def reverse_other(t):
    """Mutates the tree such that nodes on every other (even_indexed) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    for branch in t.branches:
        for b in branch.branches:
            reverse_other(b)
    t1 = [branch.label for branch in t.branches] #[::-1]
    t1.reverse()
    for i in range(len(t1)):
        t.branches[i].label = t1[i]
    
        
""" #Alternate solution
    def reverse_helper(t, need_reverse):
        if t.is_leaf():
            return
        new_labels = [b.label for b in t.branches][::-1]
        for i in range(len(b.branches)):
            reverse_helper(b.branches[i], not need_reverse)
            if need_reverse:
                b.branches[i].label = new_labels[i]
    reverse_helper(t, True)



#test code
l = [b.label for b in t.branches]
        for element in l:
            for b in t.branches:
                b.label = l.pop()
"""
