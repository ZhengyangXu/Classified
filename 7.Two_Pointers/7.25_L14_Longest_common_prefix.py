"""
Description
_____________
Write a function to find the longest common prefix string amongst an array of strings.
Approach
______________
assume strs[0] to be the prefix, then gradually decrease it
"""


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in xrange(1, len(strs)):
            j = 0
            while j < min(len(strs[i]), len(prefix)):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix
