"""
Description
_______________
Given an array of n integers where n > 1, nums,
return an array output such that output[i] is equal to the product
of all the elements of nums except nums[i].
Solve it without division and in O(n).
For example, given [1,2,3,4], return [24,12,8,6].
Approach
____________
1. give me left
2. give me right
3. return

Complexity
___________
Time - O(N)
Space - O(N)
"""

 
class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # left to me, right to me
        output = []
        p = 1
        for v in nums:
            output.append(p)
            p *= v
        p = 1
        for i in xrange(len(nums) - 1, -1, -1):
            output[i] *= p
            p *= nums[i]
        return output
