"""
(a)(Complete Choice): for every problem instance, at least one
choice is consistent with an optimal solution.
(b) (Inductive Structure): for each initial choice ck, show that
making choice c leaves one or more strictly smaller subproblems
with no external constraints relative to ck.
(c) (Optimal Substructure): for each initial choice ck, if its induced
subproblems are solved optimally, then combining their
solutions with choice ck yields a solution that is optimal among
all solutions that make choice ck.

Key is to find the recurrence function

Description
______________
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

Approach
________________
Define X[i....j] and Y[i.....j] as the two substrings of X and Y
Define D(i, j) as the minimum distance between X and Y to the index i and j

eg. X = abcd  Y = abcde

  | "" |a |b |
--|----|--|--|---------
""|    |  |  |
--|----|--|--|--------
a |    |  |  |
--|----|--|--|---------
Start at empty string


Initialization/Base Case
=====================

D(i,0) = i
D(0, j)= j

recurrence
=====================
D(i,j) = min (

        D(i-1, j) + 1,
        D(i, j-1) + 1,
        D(i-1, j-1) (+1 if X[i] == X[j] else 0)
)


Complexity
_____________________
Space: m*n
Time : O(m*n)

"""


class Solution(object):

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1) + 1
        n = len(word2) + 1
        DP = [[0 for _ in range(n)]for _ in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                if i == 0:
                    DP[i][j] = j
                elif j == 0:
                    DP[i][j] = i
                else:
                    if word1[i - 1] == word2[j - 1]:
                        cost = 0
                    else:
                        cost = 1
                    DP[i][j] = min(DP[i - 1][j] + 1, DP[i][j - 1] + 1, DP[i - 1][j - 1] + cost)
        return DP[m - 1][n - 1]
