"""
Description
_____________
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""


class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'

        prev = self.countAndSay(n - 1)
        if len(prev) == 1:
            return '1' + prev
        res = ''
        c = 1
        for i in xrange(1, len(prev)):

            if prev[i] == prev[i - 1]:
                c += 1
            else:
                res += (str(c) + prev[i - 1])
                c = 1
            if i == len(prev) - 1:
                res += (str(c) + prev[i])
        return res
