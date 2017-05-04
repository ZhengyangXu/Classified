"""
Description
____________
Given a sorted array, remove the duplicates in place such that each element
appear only once and return the new length.
Do not allocate extra space for another array
you must do this in place with constant memory.
 
Example
____________
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].

Approach
____________
Same as last one except no need to sort first

Complexity
___________
Time - O(N)
Space - O(1)
"""


class Solution:
    """
    @param A: a list of integers
    @return an integer
    """

    def removeDuplicates(self, A):
        # write your code here
        if A is None and len(A) == 0:
            return 0

        start = 0
        for i in xrange(1, len(A)):
            if A[i] != A[start]:
                start += 1
                A[start] = A[i]
        return start + 1
