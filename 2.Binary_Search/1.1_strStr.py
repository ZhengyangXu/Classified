"""
Description
=========================
For a given source string and a target string, you should output the first index(from 0) of target string in source string.
If target does not exist in source, just return -1.

Clarification
=============================
Do I need to implement KMP Algorithm in a real interview?
Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure your confirm with the interviewer first.

Example
=============================
If source = "source" and target = "target", return -1.
If source = "abcdabcdefg" and target = "bcd", return 1.
"""


class Solution:

    def strStr(self, source, target):
        # write your code here
        if target is None:
            return -1
        if len(target) == 0:
            return 0
        if source is None or len(source) == 0:
            return -1

        for i in xrange(len(source) - len(target) + 1):
            for j in xrange(len(target)):
                if source[i + j] != target[j]:
                    break
                elif source[i + j] == target[j] and j == len(target) - 1:
                    return i

        return -1
