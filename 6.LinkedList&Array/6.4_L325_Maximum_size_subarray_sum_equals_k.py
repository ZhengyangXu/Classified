"""
Description
___________
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?

Approach
________

Realizing that this problem is similar to the two sum what we can do is store in
a map, where the key to this map is the sum so far at the current index, taking
the subtraction of the sum and the desired value we can look up in the map at what index
the start for this sum occured, and check to see if the current minus the returned value
is greater than the current maximum.

For this problem the following relationship was utilized:
Sum[j] - Sum[i] + nums[j] = k

This algorithm can be done in a single pass if we calculate the sum as we go.

Complexity
----------
Time - O(N)
Space - O(N)
"""


class Solution(object):

    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        maximum = 0
        # This stores k- Prefix sum v- index
        # Sum[j] - Sum[i] + nums[j] = k
        sum_index_map = {}
        sum_index_map[0] = 0
        for i in range(1, len(nums) + 1):
            sum += nums[i - 1]
            seek = sum - k
            if seek in sum_index_map:
                maximum = max(maximum, i - sum_index_map[seek])
            if sum not in sum_index_map:
                sum_index_map[sum] = i

        return maximum
