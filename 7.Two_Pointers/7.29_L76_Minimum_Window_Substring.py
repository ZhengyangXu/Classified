"""
Description
______________
Given a string S and a string T, find the minimum window in
S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows
you are guaranteed that there will always be only one unique minimum window in S.
"""


class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t)
        missing = len(t)
        opt_i, opt_j = 0, 0
        i = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1

            # print need
            if not missing:
                # print "===>", c
                while need[s[i]] < 0:
                    # print "++", s[i], need
                    need[s[i]] += 1
                    i += 1
                    # print "--", s[i], need
                if j - i < opt_j - opt_i or opt_j == 0:
                    opt_i, opt_j = i, j
        return s[opt_i:opt_j]
