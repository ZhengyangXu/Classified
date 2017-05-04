"""
Description
================
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume NO duplicates in the array.

Example
=================
[1,3,5,6], 5 → 2

[1,3,5,6], 2 → 1

[1,3,5,6], 7 → 4 

[1,3,5,6], 0 → 0

Approach
______________
Standard Binary search
But be CAUTIONS ABOUT those three cases when not found

    if target <= A[start]:
        return start
    elif target > A[end]:
        return end + 1
    else:
        return end


Complexity
____________
Time - O(Lg(N))
Space - O(1)
"""


class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """

    def searchInsert(self, A, target):
        # write your code here
        if A is None or target is None:
            return -1
        if len(A) == 0:
            return 0
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            elif target < A[mid]:
                end = mid
            else:
                start = mid
        if target <= A[start]:
            return start
        elif target > A[end]:
            return end + 1
        else:
            return end
