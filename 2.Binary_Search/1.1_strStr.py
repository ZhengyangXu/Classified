"""
Description
________________________
For a given source string and a target string, you should output the first index(from 0) of target string in source string.
If target does not exist in source, just return -1.

Example
=============================
If source = "source" and target = "target", return -1.
If source = "abcdabcdefg" and target = "bcd", return 1.

Approahch
___________________
0. The naive apporach is simply looping through source

   for i in xrange(len(source) - len(target) + 1):

1.      then at each i we compare source[i...j] to target[:]
        for j in xrange(len(target)):
            (a) when not equal, we go to next i and restart th ecomparison
            if source[i + j] != target[j]:
                break
            (b) if reached the end of target, all matches, we return i
            elif source[i + j] == target[j] and j == len(target) - 1:
                return i
2. if it escaped the for loops, we return -1

Complexity
_________________
m = len(source)
n = len(target)
Time - O(N*M)
Space - O(1)
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
