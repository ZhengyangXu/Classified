"""
Description
____________
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses
have security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house
determine the maximum amount of money you can rob tonight without alerting the police.

Approach
_____________
DP
++++++++++++
DP[i] - max profit robbing nums[:i+1]
i - rob till the ith house (include), 0 means robt the first house

DP[i] = max(DP[i-2] + nums[i], nums[i-1])
base cases are len(nums) <= 2 obviously 
"""


class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        n = len(nums)
        DP = n * [0]
        DP[0] = nums[0]
        DP[1] = max(nums[0], nums[1])
        for i in xrange(2, n):
            DP[i] = max(DP[i - 2] + nums[i], DP[i - 1])
        return DP[n - 1]
