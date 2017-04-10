"""
Description
____________

The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:
______________________
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

Approach
_________________________
Look at the previous problem, easy now
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x ^ y

        ones = 0
        while n:
            n = n & (n - 1)
            ones += 1
        return ones
