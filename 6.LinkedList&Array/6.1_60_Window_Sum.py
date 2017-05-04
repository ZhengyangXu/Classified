"""
Description
____________
Given an array of n integer, and a moving window(size k),
move the window at each iteration from the start of the array
find the sum of the element inside the window at each moving.

Approach
____________
The naive approach is to scan through an every time re-calcuate k elements'
sum. This costs us O(KM)

A btter approach is to loop through and when we calcuate the current window sum
Do new_sum = old_sum + (nums[old_last+1] - nums[old_first])

That's it

Complexity
______________

Time- O(N)
Space- O(1)
"""


class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
 
    def winSum(self, nums, k):
        # Write your code here
        if nums is None or len(nums) == 0:
            return []
        result = []
        s = 0
        for i in xrange(len(nums) - k + 1):
            if i == 0:
                s = sum(nums[i:i + k])
            else:
                s = s + (nums[i + k - 1] - nums[i - 1])
            result.append(s)
        return result
