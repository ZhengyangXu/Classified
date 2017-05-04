"""
Description
____________
Given a binary array, find the maximum length of a contiguous subarray
with equal number of 0 and 1.

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
"""


class Solution(object):

    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        dic = {0: 0}
        max_length = 0
        count = 0
        for i in xrange(1, len(nums) + 1):
            if nums[i - 1] == 0:
                count -= 1
            else:
                count += 1
            if count in dic:
                if i - dic[count] > max_length:
                    max_length = i - dic[count]
            else:
                dic[count] = i
        return max_length
