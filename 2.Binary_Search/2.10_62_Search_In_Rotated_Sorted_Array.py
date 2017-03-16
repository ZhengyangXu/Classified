"""
Description
_____________
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

Example
____________
For [4, 5, 1, 2, 3] and target=1, return 2.
For [4, 5, 1, 2, 3] and target=0, return -1.

Approach
____________
Binary Search
++++++++++++++
Constraint: A[mid] == target
Goal: find target

Strategy: The goal is to ditch half of the target each iteration

There are five situations we need to perform correspondingly(actions might be
duplicative but nice to distinquish between them)

    1. if find the target return it

    if A[mid] == target:
        return mid

    2. mid land at index 3 of [9,1,2,3,4,5,6]

    elif A[mid] < A[end]:

    now there are two sections, at right, it's a normal sorted array, at left
    it's a rotated sorted array again. We can both essentially recursively handle
    them and ditch the other half after knowing where target lands

        2(a). target is in the right section (sorted array)
        if target >= A[mid] and target <= A[end]:
            start = mid
        2(b). target is in the left section (rotated array)
        else:
            end = mid

    3. mid land at index 3 of [3,4,5,6,7,1,2]
    else:
        Now similarly, there are two sections
        3(b). left sections of sorted array
        if target >= A[start] and target <= A[mid]:
            end = mid
        3(c). right section of rotated arrays
        else:
            start = mid
Complexity
______________
Time - O(Lg(N))
Space - O(1)
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
