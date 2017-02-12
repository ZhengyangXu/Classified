"""
Description
=============
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Example
==============
For [4, 5, 1, 2, 3] and target=1, return 2.
For [4, 5, 1, 2, 3] and target=0, return -1.
"""


class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """

    def search(self, A, target):
        # write your code here
        if A is None or len(A) == 0 or target is None:
            return -1
        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            elif A[mid] < A[end]:
                if target >= A[mid] and target <= A[end]:
                    start = mid
                else:
                    end = mid
            else:
                if target >= A[start] and target <= A[mid]:
                    end = mid
                else:
                    start = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
