"""
Description
_________________
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:

Approach
__________________
dfs
+++


Complexity
__________________
Connecting point at
add in ')' if exceesive '(' is present

Complexity
_____________
Time - N!
Space - O(N)
"""


class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l, r = 0, 0
        result = []
        branch = ""
        self.dfs(l, r, branch, n, result)
        return result

    def dfs(self, l, r, branch, n, result):

        if(l == n and r == n):
            result.append(branch)
            return
        if l < n:
            self.dfs(l + 1, r, branch + '(', n, result)
        if l > r:
            self.dfs(l, r + 1, branch + ')', n, result)
