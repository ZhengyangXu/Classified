"""
Description
____________ 
Given a string which consists of lowercase or uppercase letters, find the length
of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.


Example:
___________
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.


Approach
_________________
All letters can be used excpet odd freq appearing ones (since pairs is the building
block for palindrome ). + one of the odd freq (put in the middle)
1. build freq_dic
2. counter number of odd-freq element
3. return len(s) - odds + (1 if odds else 0)

Extra
___________________
x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
~ x
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.


Complexity
__________________
Time - O(N)
Space - O(N)
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        freq_dic = Counter(s)
        odds = sum(i & 1 for i in freq_dic.values())
        return len(s) - odds + (1 if odds else 0)
