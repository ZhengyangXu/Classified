"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Approach
______________
Same as fibancii

Complexity
____________
Time - T(N)
Space - O(N)
"""

 
class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is None or n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        DP = (n + 1) * [0]
        DP[1] = 1
        DP[2] = 2
        for i in xrange(3, n + 1):
            DP[i] = DP[i - 1] + DP[i - 2]

        return DP[n]
