"""
Description
____________
Given an array of integers
find how many unique pairs in the array
such that their sum is equal to a specific target number.
Please return the number of pairs.

Example
____________
Given nums = [1,1,2,45,46,46], target = 47
return 2

1 + 46 = 47
2 + 45 = 47

Approach
_____________
Two pointers + skip duplicates
Notes:
(1) Skip step has to happen after detect v == target
because situation like A = [1, 2, 3, 4, 4], target = 8
0. Sort
1. initialize left, right = 0, len(nums) -1; s = 0
2. while left < right
    v = nums[left] + nums[right]
    a. when v == target:
        (1) Skip duplicates
            while left < right and nums[left + 1] == nums[left]:
                left += 1
            while left < right and nums[right - 1] == nums[right]:
                right -= 1
        (2) s += 1; left += 1, right -= 1
    b. when v < target:
        left += 1
    c. when v > target:
        right -= 1
3. return s

Complexity
____________
Time - O(N.Log(N))
Space - O(1)

"""

 
class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer

    def twoSum6(self, nums, target):
        # Write your code here
        if nums is None or len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1
        nums.sort()
        s = 0
        while left < right:
            # print "begin==>",left, right

            v = nums[left] + nums[right]
            # print left, right, v
            if v == target:
                while left < right and nums[left + 1] == nums[left]:
                    left += 1
                while left < right and nums[right - 1] == nums[right]:
                    right -= 1
                s += 1
                left += 1
                right -= 1

                # print left, right
            elif v < target:
                # print "no"
                left += 1
            else:
                right -= 1
        return s
