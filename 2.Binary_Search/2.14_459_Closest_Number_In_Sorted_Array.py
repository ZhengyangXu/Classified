"""
Description
__________
Given a target number and an integer array
A sorted in ascending order, find the index i in A
such that A[i] is closest to the given target.
Return -1 if there is no element in the array.

Example
________
Given [1, 2, 3] and target = 2, return 1.
Given [1, 4, 6] and target = 3, return 1.
Given [1, 4, 6] and target = 5, return 1 or 2.
Given [1, 3, 3, 4] and target = 2, return 0 or 1 or 2.

Approach
________
just a quick 
Compleixty
_________
Lg(N)
"""


class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer

    def closestNumber(self, A, target):
        # Write your code here
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            v = A[mid]
            if v == target:
                return mid
            elif v < target:
                start = mid
            else:
                end = mid

        if abs(A[start] - target) < abs(A[end] - target):
            return start
        else:
            return end
