"""
Description
__________________
Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.


Example
____________________
Given s = "lintcode", dict = ["lint", "code"].

Return true because "lintcode" can be break as "lint code".

Approach
___________________
DP
+++++++++++
We define DP[i] as for Substring S[:i] (not including i), it has a
word break or not

Recurrence
+++++++++++

DP[0] = True (null break to true to allow bottom up buidling)
DP[i] = any(S[i-j:i] in dict and DP[i-j]  for j in xrange(1, i+1))


Detail
++++++++++++
for python we have to do 1 trick that is to only look back to
min(i, maxLength) + 1 to save time

Complexity
__________
m = length of maxlength word in dict
n = length of string

Time - O(MN)
Space - O(N)
"""


class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    # def wordBreak(self, s, dict):
    #     # write your code here
    #     DP = [False for _ in xrange(len(s)+1)]
    #     DP[0] = True
    #     for i in xrange(1, len(s)+1):
    #         flag = False
    #         for j in xrange(i):
    #             if s[j:i] in dict and DP[j]:
    #                 flag = True
    #                 break
    #         DP[i] = flag
    #     return DP[len(s)]
 
    def wordBreak(self, s, dict):
        if len(dict) == 0:
            return len(s) == 0

        n = len(s)
        f = [False] * (n + 1)
        f[0] = True

        maxLength = max([len(w) for w in dict])
        for i in xrange(1, n + 1):
            for j in range(1, min(i, maxLength) + 1):
                if not f[i - j]:
                    continue
                if s[i - j:i] in dict:
                    f[i] = True
                    break

        return f[n]
