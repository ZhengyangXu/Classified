"""
Description
___________
Given an array nums of n integers, find two integers in nums
such that the sum is closest to a given number, target.
Return the difference between the sum of the two integers and the target.

Example
___________
Given array nums = [-1, 2, 1, -4], and target = 4.
The minimum difference is 1. (4 - (2 + 1) = 1).

Approach
___________
Very Similar to the standard 2Sum except we do
min_dist = min(min_dist, abs(v - target)) when v < target or v>target

Complexity
____________
Time - O(N.Log(N))
Space - O(1)
"""

 
class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target

    def twoSumClosest(self, nums, target):
        # Write your code here
        nums.sort()
        left, right = 0, len(nums) - 1
        import sys
        min_dist = sys.maxint
        while left < right:
            v = nums[left] + nums[right]
            if v == target:
                return 0
            elif v < target:
                min_dist = min(min_dist, abs(v - target))
                left += 1
            else:
                min_dist = min(min_dist, abs(v - target))
                right -= 1
        return min_dist
