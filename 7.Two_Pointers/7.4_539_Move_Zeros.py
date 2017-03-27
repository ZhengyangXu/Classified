class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place

    def moveZeroes(self, nums):
        # Write your code here
        i = 0
        j = 0

        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        for i in range(i, len(nums)):
            nums[i] = 0
