"""
Related to question Excel Sheet Column Title
Given a column title as appear in an Excel sheet
return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""


class Solution(object):

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        n = len(s)
        for i in xrange(n - 1, -1, -1):
            result += (26**(n - 1 - i)) * (ord(s[i]) - ord('A') + 1)
        return result
