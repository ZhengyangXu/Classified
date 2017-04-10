"""
Description
_______________
Write a function that takes an unsigned integer and returns
the number of ’1' bits it has (also known as the Hamming weight).
For example, the 32-bit integer ’11' has binary representation
00000000000000000000000000001011, so the function should return 3.

Approach
________________
key - n & (n-1) pops off one 1 each time

Complexity
________________
Time - O(Lg(N))
space - O(1)
"""
# class Solution(object):
#     def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         ones = 0
#         while n:
#             ones += n&1
#             n>>1
#         return ones


class Solution(object):
    def hammingWeight(self, n):
        ones = 0
        while n:
            n = n & (n - 1)
            ones += 1
        return ones
