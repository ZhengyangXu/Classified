"""
Description
____________
Follow up for Search in Rotated Sorted Array:
What if duplicates are allowed?

Example
____________
Given [1, 1, 0, 1, 1, 1] and target = 0, return true.
Given [1, 1, 1, 1, 1, 1] and target = 0, return false.

Approach
____________
Binary Search + worst case handling
++++++++++++++++++++
When A[mid] == A[end] and A[mid]!= target we can only ditch end
when not, it's the same thing as last problem I


Compelxity
____________
Time - WOrst case [0,1,1,1,1,1,1,1,1] O(N)
"""


class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """

    def search(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return False
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return True
            elif A[mid] < A[end]:
                if target >= A[mid] and target <= A[end]:
                    start = mid
                else:
                    end = mid

            elif A[mid] > A[end]:
                if target >= A[start] and target <= A[mid]:
                    end = mid
                else:
                    start = mid

            else:
                end -= 1
        if A[start] == target:
            return True
        if A[end] == target:
            return True
        return False
