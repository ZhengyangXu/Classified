"""
Description
_____________
For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

Example
_____________
If source = "source" and target = "target", return -1.

If source = "abcdabcdefg" and target = "bcd", return 1.
"""


class Solution:

    def strStr(self, source, target):
        # write your code here
        if source == None or target == None:
            return -1
        if len(target) == 0:
            return 0
        if len(source) == 0:
            return -1
        for i, s_i in enumerate(source[:len(source) - len(target) + 1]):
            for j, s_j in enumerate(target):
                if target[j] == source[i + j] and j == len(target) - 1:
                    return i
        return -1
