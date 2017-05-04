"""
Description
_________________
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

Example
__________________
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Approach
___________
Binary Searches
+++++++++++++++
Do a binary search to find the first position
Do a binary search to find the last position
"""

 
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        if len(A) == 0 or not A:
            return [-1, -1]

        start, end = 0, len(A) - 1
        # search for left boundary, first postion
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        if A[start] == target:
            left = start
        elif A[end] == target:
            left = end
        else:
            left = -1

        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            right = end
        elif A[start] == target:
            right = start
        else:
            right = -1
        return [left, right]
