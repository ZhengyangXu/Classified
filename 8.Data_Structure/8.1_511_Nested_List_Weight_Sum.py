"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth. Each element is either an integer, or a list --
whose elements may also be integers or other lists.

Have you met this question in a real interview? Yes
Example
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1, 4 * 1 * 2 + 1 * 2 * 1 = 10)
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 42 + 63 = 27)

Appproach
______________________
DFS
Version 1. recursive
def dfs(NL, level)
    base case:
        if this element is an int, return Nl.v * level
    loop through nl in NL.getList():
        DFS(nl, level + 1)


Version 2.Iterative
 append every thing to stack as a tuple (v, level = 1)
 then pop stack
 if it's a value increment sum by int(v) * level
 else:
     append everything inside v.list with (e, level+1) back to stack


Complexity
____________
Time - O(N)
Space - O(N)
"""
# Version 1

class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer

    def depthSum(self, nestedList):
        # Write your code here
        if nestedList is None:
            return 0
        result = 0
        for i in nestedList:
            result += self.getSum(i, 1)
        return result

    def getSum(self, nestedinteger, level):
        if nestedinteger.isInteger():
            return nestedinteger.getInteger() * level
        result = 0
        for i in nestedinteger.getList():
            result += self.getSum(i, level + 1)
        return result

# Version 2
class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer

    def depthSum(self, nestedList):
        if nestedList is None or len(nestedList) == 0:
            return 0
        from collections import deque
        stack = deque()
        result = 0
        for i in nestedList:
            stack.append((i, 1))
        while stack:
            cur, level = stack.pop()
            if cur.isInteger():
                result += cur.getInteger() * level
            else:
                for i in cur.getList():
                    stack.append((i, level + 1))
        return result
