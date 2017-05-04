"""
Description
______________
Find longest subsequence not substring

Approach
__________________
DP
++++++
Recurrence
___________
DP[i][j] - longest subsequence between S[i:j+1]
         if s[i] == s[j]:
             DP[i][j] = DP[i+1][j-1] + 2
             edge when i+1 > j-1, DP[i][j] = 2
        else:
            DP[i][j] = max(DP[i-1][j], DP[i+1][j])
Complexity 
__________
Time - O(N^2)
Space - O(N^2)
"""

class Solution(object):

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        DP = [[0 for _ in xrange(n)] for _ in xrange(n)]
        for i in xrange(n - 1, -1, -1):
            for j in xrange(i + 1, len(s)):
                DP[i][i] = 1
                if s[i] == s[j]:
                    DP[i][j] = 2 + (DP[i + 1][j - 1] if j - i >= 2 else 0)
                else:
                    DP[i][j] = max(DP[i + 1][j], DP[i][j - 1])
        # print DP
        return DP[0][n - 1]
#
#
# class Solution(object):
#     def longestPalindromeSubseq(self, s):
#         d = {}
#         def f(s):
#             if s not in d:
#                 maxL = 0
#                 for c in set(s):
#                     i, j = s.find(c), s.rfind(c)
#                     maxL = max(maxL, 1 if i==j else 2+f(s[i+1:j]))
#                 d[s] = maxL
#             return d[s]
#         return f(s)
