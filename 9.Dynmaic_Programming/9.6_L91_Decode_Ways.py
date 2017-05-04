"""
Description
______________
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


class Solution:
    # @param s, a string
    # @return an integer

    def numDecodings(self, s):
        if s is None or len(s) == 0:
            return 0
        DP = [0 for _ in xrange(len(s))]
        DP[0] = 0 if s[0] == '0' else 1
        for i in xrange(1, len(s)):
            first = s[i:i + 1]
            second = s[i - 1:i + 1]
            if int(first) != 0:
                DP[i] += DP[i - 1]
            if int(second) >= 10 and int(second) <= 26:
                DP[i] += DP[i - 2] if i >= 2 else 1
        return DP[-1]
