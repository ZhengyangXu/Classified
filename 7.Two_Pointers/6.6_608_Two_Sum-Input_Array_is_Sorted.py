"""
Description
____________
Given an array of integers that is already sorted in ascending order
find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers
such that they add up to the target, where index1 must be less than index2.
Please note that your returned answers (both index1 and index2)
are not zero-based.

Example
_____________
Given nums = [2, 7, 11, 15], target = 9
return [1, 2]
"""


class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} = nums[index1] + nums[index2]
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, nums, target):
        # Write your code here
        if nums is None or len(nums) == 0:
            return
        left, right = 0, len(nums) - 1
        while left < right:
            v = nums[left] + nums[right]

            if v == target:
                return [left + 1, right + 1]
            if v < target:
                left += 1
            else:
                right -= 1
        return
