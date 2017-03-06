"""
Description
_____________
Given an array of integers, find how many pairs in the array
such that their sum is less than or equal to a specific target number.
Please return the number of pairs.

Example
___________________
Given nums = [2, 7, 11, 15], target = 24.
Return 5.
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 25

Approach
___________________
0. Sort
1. Have two pointers, left, right = 0, len(nums) - 1; s = 0
2. while left < right
    when nums[left] + nums[right] <= target:
        (a). anything between right and left added with left
        will satsiefy <= target constraint so
        s += (right-left)
        (b). move left => left += 1
    else:
        right -= 1
return s

Complexity
____________
Time - O(N.Log(N))
Space - O(1)
"""

class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum5(self, nums, target):
        # Write your code here
        if nums is None or len(nums) == 0:
            return 0

        s = 0
        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            v = nums[left] + nums[right]
            if v <= target:
                s += (right - left)
                left += 1
            else:
                right -= 1
        return s
