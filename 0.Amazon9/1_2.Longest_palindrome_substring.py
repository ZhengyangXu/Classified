"""
Description
_________________
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Note
_______________
substring -  连贯
subsequence - 不用连贯

Approach & Complexity
_______________

DP
++++++++++
Recurrence -
DP[i][j] - whether string from i to j is palindromic or not
         = S[i] == S[j] and DP[i+1][j-1]

Direction -
From back and maintain j expanding from i, so it's a sparse matrix
&
makes more sense, since i to j

Edge - when i and j are only 1 or less away, DP[i][j] is true whenever S[i] == S[j]


Now maintain a gloabal maximum for length

Complexity
____________
Time - O(N^2)
SPace - O(N^2)


expanding
++++++++++++
for each index, expand from the middle until s[left-1] != s[right+1] return right, left
right- left is the current max
maintain a gloabal max

Note:
++++++++++++
while left > 0 and right < len(s) - 1:
    # print left, right
    if s[left - 1] != s[right + 1]:
        break

Complexity
____________
Time - O(N^2)
Space - O(1)
"""
# DP


class Solution(object):

    def longestPalindrome(self, s):
        n = len(s)
        DP = [[0 for _ in xrange(n)] for _ in xrange(n)]
        max_length = 0
        maxl, maxr = 0, 0
        for i in xrange(n - 1, -1, -1):
            DP[i][i] = 1
            for j in xrange(i + 1, n):
                if s[i] == s[j] and (j - i < 2 or DP[i + 1][j - 1]):
                    DP[i][j] = 1
                    if max_length < j - i:
                        max_length = j - i
                        maxl = i
                        maxr = j

        return s[maxl:maxr + 1]

# Middle expansion


class Solution(object):

    def longestPalindrome(self, s):
        maxl, maxr = 0, 0
        for i in xrange(len(s) - 1):
            if s[i] == s[i + 1]:
                left, right = self.expand(s, i, i + 1)
                left_alt, right_alt = self.expand(s, i, i)
                if right_alt - left_alt > right - left:
                    left, right = left_alt, right_alt
            else:
                left, right = self.expand(s, i, i)
            if right - left > maxr - maxl:
                maxl, maxr = left, right
        return s[maxl:maxr + 1]

    def expand(self, s, left, right):
        # return expanded_left and expanded_right
        while left > 0 and right < len(s) - 1:
            # print left, right
            if s[left - 1] != s[right + 1]:
                break
            left -= 1
            right += 1
        return left, right
