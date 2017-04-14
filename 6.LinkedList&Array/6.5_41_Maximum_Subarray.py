"""
Description
___________
Given an array of integers, find a contiguous subarray which has the largest sum.

Example
_____________
Given the array [−2,2,−3,4,−1,2,1,−5,3],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

Approach
_____________
DP
++++++++++
This can be solved using dynamic programming
let s[i] be the maximum sum ending at nums[i]
s[0] = 0
s[i] = max(s[i-1]+s[i],nums[i])

Complexity
_____________
Time - O(N)
Space - O(N)


Kadine's Algo
+++++++++++
This is essentially DP
However, we only need to keep track of a local sum and a global sum

we keep an accumulating sum and a pointer initialized to be zero and pointing to
the start of the array
if the sum becomes negaive, we reset
0. make sum 0
1. set pointer to i + 1 (if we need to know the indexes)

keep comparing global sum with local sum and update global with larger one

Complexity
___________
Time - O(N)
Space - O(1)
"""


# DP
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        if nums is None:
            return None
        a = [0 for _ in xrange(len(nums))]
        a[0] = nums[0]
        for i in xrange(1, len(a)):
            a[i] = max(a[i - 1], 0) + nums[i]
        return max(a)

# Kadine's algo


class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        if nums is None:
            return None

        import sys
        start = 0
        s = 0
        maximum = -sys.maxint - 1
        for i in xrange(len(nums)):
            s += nums[i]
            maximum = max(maximum, s)
            if s < 0:
                start = i + 1
                s = 0
        return maximum
