"""
Description
_____________
Implement int sqrt(int x).

Compute and return the square root of x.

Example
______________
sqrt(3) = 1

sqrt(4) = 2

sqrt(5) = 2

sqrt(10) = 3
"""

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        # write your code here
        if x < 0:
            return -1
        start, end = 0, x
        while start + 1 < end:
            mid = start + (end - start) / 2
            v = mid * mid
            if v == x:
                return mid
            elif x > v:
                start = mid
            else:
                end = mid
        if end * end == x:
            return end
        return start
