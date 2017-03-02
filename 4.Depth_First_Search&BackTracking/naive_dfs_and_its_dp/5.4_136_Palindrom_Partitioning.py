"""
Description
______________
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example
________________
Given s = "aab", return:

[
  ["aa","b"],
  ["a","a","b"]
]

Approach
_______________
obiviously we use DFS here
care
0. when append branch, make a copy
1. standard pop off branch procedure

Complexity
___________________
Exponential 
"""


class Solution:
    # @param s, a string
    # @return a list of lists of string

    def partition(self, s):
        # write your code here
        result = []
        branch = []
        self.dfs(s, 0, branch, result)
        return result

    def dfs(self, s, start, branch, result):
        if start == len(s):
            result.append(branch[:])
            return
        for i in xrange(start, len(s)):
            if self.isPalindrome(s[start:i + 1]):
                branch.append(s[start:i + 1])
                self.dfs(s, i + 1, branch, result)
                branch.pop()

    def isPalindrome(self, s):
        # since we donot want empty list, we treat length 2 strings as non-palindrome
        i, j = 0, len(s) - 1
        if len(s) > 1:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
        return True
