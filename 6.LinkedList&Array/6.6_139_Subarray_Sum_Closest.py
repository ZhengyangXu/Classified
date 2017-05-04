"""
Description
____________
Given an integer array, find a subarray with sum closest to zero.
Return the indexes of the first number and last number.

Example
_____________
Given [-3, 1, 1, -3, 5],
return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4].
 
Approach
_____________
0. get dictionary
key(prefix_sum)->index O(N)
1. sort the dictionaries key O(N)
2. get closest two key and return corresponding indexes (also need to sort)

Complexity
_____________
Time - O(N*(LgN))
Space -O(N)
"""


class Solution:

    def subarraySumClosest(self, nums):
        dic = {0: -1}
        s = 0
        for i in xrange(len(nums)):
            s += nums[i]
            if s in dic:
                return [dic[s] + 1, i]
            dic[s] = i
        sorted_keys = sorted(dic.keys())
        import sys
        min_dist = sys.maxint
        result = []
        for i in xrange(len(sorted_keys) - 1):
            if abs(sorted_keys[i] - sorted_keys[i + 1]) < min_dist:
                min_dist = abs(sorted_keys[i] - sorted_keys[i + 1])
                result = [dic[sorted_keys[i]], dic[sorted_keys[i + 1]]]
        result = sorted(result)
        return [result[0] + 1, result[1]]
