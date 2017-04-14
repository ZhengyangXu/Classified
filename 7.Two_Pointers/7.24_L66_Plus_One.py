"""
Description
____________
Given a non-negative integer represented as a non-empty array of digits
plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.

Approach
______________
Same as add two numbers

Complexity
_______________
Time - O(N)
Space - O(1)
"""


class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None or len(digits) == 0:
            return []
        digits.reverse()
        adding = [1]
        while len(adding) < len(digits):
            adding.append(0)

        carry = 0
        i, j = 0, 0
        while i < len(digits) or carry:
            s = 0
            if i < len(digits):
                s = digits[i] + adding[j]
            s += carry
            if i < len(digits):
                digits[i] = s % 10
            else:
                digits.append(s % 10)
            carry = s / 10
            i += 1
            j += 1
        digits.reverse()
        return digits
