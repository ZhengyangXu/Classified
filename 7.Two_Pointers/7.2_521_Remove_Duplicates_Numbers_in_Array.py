"""
Description
_____________
Given an array of integers, remove the duplicate numbers in it.

You should:
1. Do it in place in the array.
2. Move the unique numbers to the front of the array.
3. Return the total number of the unique numbers.

Given nums = [1,3,1,4,4,2], you should:

Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?
we only care about the part which has no duplicate integers.

Approach
_____________
Use set is trivial

Complexity
______________
Time - O(N)
Space - O(N)
 
Approach
_______________
0. sort
1.
Initalize start = 0
Loop through  i = 1 -> len(A) - 1
    a. when A[i] == A[start], do nothing
    b. else(when A[i] == A[start])
        start += 1 (since we want to keep one copy of duplicates)
        A[start] = A[i]

Complexity
_______________
Time - O(N.Lg(N))
Space - O(1)
"""


class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers

    def deduplication(self, nums):
        # Write your code here
        if nums is None or len(nums) == 0:
            return 0

        nums.sort()
        start = 0
        for i in xrange(1, len(nums)):
            if nums[i] != nums[start]:
                start += 1
                nums[start] = nums[i]
        return start + 1
