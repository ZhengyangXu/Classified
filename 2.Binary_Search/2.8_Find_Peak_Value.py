"""
Description
_______________
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peek if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

Approach
_____________
Binary Search
+++++++++++++++
Range: 0 -> len(A) - 2
Constraint: A[mid] > A[mid+1] and A[mid] > A[mid-1]
Goal: return one

There are four situations

    # @ peak
    if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
        return mid
    # 左高右低 move left
    elif A[mid] < A[mid - 1] and A[mid] > A[mid + 1]:
        end = mid
    # 左低右高 move right
    elif A[mid] > A[mid - 1] and A[mid] < A[mid + 1]:
        start = mid
    # 谷底 move either way
    else:
        start = mid

Complexity 
___________

Time - O(Lg(N))
Space - O(1)
"""

class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.

    def findPeak(self, A):
        # write your code here
        if A is None:
            return -1
        start, end = 0, len(A) - 2
        while start + 1 < end:
            mid = start + (end - start) / 2
            # @ peak
            if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
                return mid
            # 左高右低
            elif A[mid] < A[mid - 1] and A[mid] > A[mid + 1]:
                end = mid
            # 左低右高
            elif A[mid] > A[mid - 1] and A[mid] < A[mid + 1]:
                start = mid
            # 谷底
            else:
                start = mid
        if A[start] > A[end]:
            return start
        else:
            return end
