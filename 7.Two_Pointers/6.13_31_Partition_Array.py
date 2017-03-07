"""
Description
_____________
Given an array nums of integers and an int k, partition the array
(i.e move the elements in "nums") such that:
All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Approach
____________
This is eseentially the parition step of quicksort

Notes
0. Use left<=right for everything to ensure it crosses (left > right)
1. after crossing
   left stops at first index that is nums[i] >= k (not constraint 1)
   right terminates at last index that is nums[i] < k (not constraint 2)

0. Initialize left, right = 0, len(nums) - 1
1. While left <= right:
       (a) Move left to the first index that number[index] >= k

           while left <= right and nums[left] < k:
              left += 1
       (b) Move right to the last index (first from right) that number[index] <k

       while left <= right and nums[right] >= k:
           right -= 1
       (c) when left <= right
            We swap make left, right go to correct position

            if left<=right:
                swap(nubers, left, right)
        (d) when left > right , they alreday cross, we have the situation we want

            else:
                do nothing
2. return left (see notes about why)

Complexity
______________
Time - O(N)
Space - O(1)
"""


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if nums is None or len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:

            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                self.swap(nums, left, right)

        return left

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
