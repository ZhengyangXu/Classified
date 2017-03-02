"""
Description
_______________
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Have you met this question in a real interview? Yes

Example
________________
Given the list [[1,1],2,[1,1]], By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Given the list [1,[4,[6]]], By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

Approach
_________________
maintain a stack, initialize stack by
adding element in list to stack reversely

has_next will flatten the top nestList on stack and place the next
Int on top

next simply return the top of stack

note that next is not responsible for checking whether there exist a next
has_next has to be called before using next


"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return {boolean} True if this NestedInteger holds a single integer,
#        rather than a nested list.
#        """
#
#    def getInteger(self):
#        """
#        @return {int} the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return {NestedInteger[]} the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        from collections import deque
        self.stack = deque()
        for i in reversed(nestedList):
            self.stack.append(i)
    # @return {int} the next element in the iteration

    def next(self):
        # Write your code here
        return self.stack.pop().getInteger()

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True
            for i in reversed(self.stack.pop().getList()):
                self.stack.append(i)
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
