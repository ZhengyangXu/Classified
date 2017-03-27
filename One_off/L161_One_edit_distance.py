"""
Description
___________
Given two strings S and T, determine if they are both one edit distance apart.

Approach
________
Break problem into two seperate cases.

1) If the size of the two strings is equal then iterate through both the strings
and determine if they differ by exactly one letter.

2) If the size of the two strings differs by exactly one we can apply deletion/insertion.
In this problem deletion and insertion can be thought of as the same thing.
Determine the smaller of the two strings. Looping according to the shorter one,
at index i, determine if short[i:] == long[i+1:].

Complexity
__________
O(n)
"""


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # One delete === one insert
        if len(s)==len(t):
            return self.oneReplace(s,t)
        elif abs(len(s) - len(t)) ==1:
            return self.oneDelete(s,t)
        else:
            return False

    def oneReplace(self,s1, s2):
        counter = 0
        for i in xrange(len(s1)):
            if s1[i] != s2[i]:
                counter += 1
        if counter == 1:
            return True
        else:
            return False

    def oneDelete(self,s1, s2):
        if len(s1) > len(s2):
            long = s1
            short = s2
        else:
            long = s2
            short = s1
        # smartly handlles short = "" ; long = "*"
        for i in range(len(short)):
            if short[i] != long[i]:
                return short[i:] == long[i+1:]
        return True
