"""
Description
_______________
Given an integer array, find a subarray where the sum of numbers is zero.
Your code should return the index of the first number and the index of the last number.

Example
_______________________________________________
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].

Approach
________________________________________
Let's try to solve a more general problem
Any subarray for any target value x?

For example x = 3 and input same as given example
If we look up the prefix
pre = [-3, -2, 0, -3, 1]

difference between pre[4] - pre[1] stands for sum(2,5)(inclusive) eqauls to 3
We can do two loops, but sing hashmap is a better solution with only one loop Obviously

Complexity
___________________
Time - O(N)
Space - O(N)
"""


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        prefix_sum = {0: -1}
        sum = 0
        for i in xrange(len(nums)):
            sum += nums[i]
            if sum in prefix_sum:
                return [prefix_sum[sum] + 1, i]
            else:
                prefix_sum[sum] = i
