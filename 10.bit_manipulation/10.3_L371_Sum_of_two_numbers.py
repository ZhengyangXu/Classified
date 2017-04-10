"""
Description
_______________
Calculate the sum of two integers a and b
but you are not allowed to use the operator + and -.

Example
_____________
Given a = 1 and b = 2, return 3.

Approach
______________
a&b - gives you the carry digits
a^b - gives you distinctive digits (equals to plus without caring about carry)

Now see the code, you will understand

write this in python have extra complication since python does not use 2^32 Int

Complexity
__________
Time - ?
Space - O(1)
"""


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        if b == 0:
            return a

        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
