"""
Description
____________
Given an array of size n, find the majority element. The majority element is the
element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Approach/ complexity
__________
1. Moore's voting
Time - O(N)
Space -O(1)
2. sorting
Time - NLg(N)
Space - O(1)
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]


class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, maj_index = 1, 0
        for i in xrange(1, len(nums)):
            if nums[i] == nums[maj_index]:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj_index = i
                count = 1
        return nums[maj_index]
