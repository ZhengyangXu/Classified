"""
Description
___________
Given a string s, cut s into some substrings such that every substring is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example
_____________
Given s = "aab",
Return 1 since the palindrome partitioning ["aa", "b"] could be produced using 1 cut.
"""


class Solution:
    # @param s, a string
    # @return an integer

    def minCut(self, s):
        # write your code here
        # return self.isPalindrome(s)
        n = len(s)
        dp = [i for i in xrange(n)]
        isPalindrome = self.isPalindrome(s)

        for i in xrange(1, n):
            # print i, "==>"
            for j in xrange(i + 1):
                # print j,i,isPalindrome[j][i]
                if isPalindrome[j][i]:
                    if j == 0:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[j - 1] + 1)
        # print dp
        return dp[n - 1]

    def isPalindrome(self, s):
        DP = [[False for _ in xrange(len(s))] for _ in xrange(len(s))]
        # length 1
        for i in xrange(len(s)):
            DP[i][i] = True
        for i in xrange(len(s) - 1):
            DP[i][i + 1] = (s[i] == s[i + 1])
        for l in xrange(2, len(s)):
            for i in xrange(len(s) - l):
                DP[i][i + l] = (s[i] == s[i + l] and DP[i + 1][i + l - 1])
        return DP
