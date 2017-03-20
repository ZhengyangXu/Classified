"""
Description
_____________
Design an iterator over a binary search tree with the following rules:

Elements are visited in ascending order (i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.

Example
______________
For the following binary search tree, in-order traversal by using iterator is [1, 6, 10, 11, 12]

   10
 /    \
1      11
 \       \
  6       12


Approach
______________
This solution is totally based upon in-order traversal
see SUM0_Three_ways_of_traversal

"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""
from collections import deque

class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        # write your code here
        self.stack = deque()
        self.cur = root
    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        return (self.cur or self.stack)
    #@return: return next node
    def next(self):
        #write your code here
        while self.cur is not None:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        node = self.cur
        if self.cur:
            self.cur = self.cur.right
        return node
