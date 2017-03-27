"""
Description
==============
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Approach
_____________
Stack
+++++++++++
Loop through the the string
1. when see a '(' or .. ,
    append to stack
2. when see a cur =  ')'. .,
    a. if stack is empty
        return false

    b. if match (stack.top(), cur)
        stack.pop()
    c. else:
        stack.append(cur)


Complexity
_____________

Time
O(N)
Space
O(N)
"""

"""
Stack approach
"""


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = ['(', '{', '[']
        b = [')', '}', ']']
        from collections import deque
        stack = deque()
        for i in s:
            if i in b:
                if len(stack) == 0:
                    return False
                elif self.isMatch(stack[-1], i, a, b):
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack) == 0

    def isMatch(self, s1, s2, a, b):
        if s1 in a:
            return a.index(s1) == b.index(s2)
        else:
            return False
