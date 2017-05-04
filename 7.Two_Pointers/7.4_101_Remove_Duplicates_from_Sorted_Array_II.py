"""
Description
__________________________
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?
 
For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].

Approach
________________________
0. sort

1.
Initalize start = 0, s = 0
Loop through  i = 1 -> len(A) - 1
    a. when A[i] == A[start]
        s += 1
        if s < 2:
            start += 1
            A[start] = A[i]
    b. else(when A[i] == A[start])
        start += 1 (since we want to keep one copy of duplicates)
        A[start] = A[i]

Complexity
__________________________
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
        if A is None or len(A) == 0:
            return 0

        start = 0
        duplicate_num = 0
        for i in xrange(1, len(A)):
            if A[i] == A[start]:
                duplicate_num += 1
                if duplicate_num < 2:
                    start += 1
                    A[start] = A[i]
            else:
                start += 1
                A[start] = A[i]
                duplicate_num = 0
        return start + 1
