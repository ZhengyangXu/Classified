"""
Description
_________________________
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.

Notice
________________________
You may assume no duplicate exists in the array.

Example
_______________________
Given [4, 5, 6, 7, 0, 1, 2] return 0

Approach
_______________________
Binary search
+++++++++++++
Range: 0, len(nums) - 1
Constraint: nums[mid] <= nums[-1]
Goal: find the first position

Notice we donot use first position of nums[mid] <= nums[0] because when
it's not rotated, it does not work

Compleixty 
____________
Time - O(Lg(N))
Space - O(1)
"""


class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array

    def findMin(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] <= nums[-1]:
                end = mid
            else:
                start = mid
        if nums[start] <= nums[-1]:
            return nums[start]
        else:
            return nums[end]
