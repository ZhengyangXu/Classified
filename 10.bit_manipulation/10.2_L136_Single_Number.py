"""
Given an array of integers, every element appears twice except for one.
Find that single one.


Approach
___________

So if the array is {2,1,4,5,2,4,1} then it will be like we are performing this operation

((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5.
Hence picking the odd one out ( 5 in this case).

Complexity
______________
Time - O(N)
SPace - O(1)
"""


class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result = result ^ i
        return result
