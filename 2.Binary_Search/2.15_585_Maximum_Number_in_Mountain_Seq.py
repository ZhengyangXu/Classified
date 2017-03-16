"""
Description
___________

Given a mountain sequence of
n integers which increase firstly and then decrease
find the mountain top.
Have you met this question in a real interview? Yes

Example
__________
Given nums = [1, 2, 4, 8, 6, 3] return 8
Given nums = [10, 9, 8, 7], return 10

Approach
_________
This translates to find the first element that has
nums[index] > nums[index-1]

Complexity
__________
Lg(N)
"""


class Solution:
    # @param {int[]} nums a mountain sequence which increase firstly and then decrease
    # @return {int} then mountain top

    def mountainSequence(self, nums):
        # Write your code here
        if nums is None or len(nums) == 0:
            return
        if len(nums) == 1:
            return nums[0]
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] >= nums[mid + 1]:
                end = mid
            else:
                start = mid
        if nums[start] > nums[start + 1]:
            return nums[start]
        else:
            return nums[end]
