"""
Description
___________
Given a string s, cut s into some substrings such that every substring is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example
_____________
Given s = "aab",
Return 1 since the palindrome partitioning ["aa", "b"] could be produced using 1 cut.

Approach
_____________
DP
++++++++++++
We solve two DPs to solve this question.
I. First we solve isPalindrome[i:j] where detects where S[i:j](inclusinon on both end)
is a palindrome
Recurrence
++++++++++++++
isPalindrome[i:j] (i<j)
if j == i:
    isPalindrome[i][j] = True
if j-i = 1:
    isPalindrome[i][j] = S[i] == S[j]
else:
    isPalindrome[i][j] = isPalindrome[i+1][j-1] && S[i] == S[j]

This translates to an efficient approach we
a. first loop through one time to set all diagonal (length 1) to be True
b. Then we loop through one time to check length 2
c. we check length 3 to n substrings (j-i = 2)


II. Then we use isPalindrome Matrix to solve DP[i] where returns how many minimum cuts S[:i](inclusion)
need to partition palindrome

Rembmer, we have both ends inclusive
Recurrence
++++++++++
DP[i]
j === 0 to i
if j == 0:
    DP[i] = 0 (the whole substring is a palindrome, 0 cut. we have to do this since inclusion on both side and we need DP[j-1])
else:
    DP[i] = min(dp[i],dp[j-1] +1) [adding one extra current cut]

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
