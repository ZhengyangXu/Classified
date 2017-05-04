"""
Description
____________
There are two sorted arrays A and B of size m and n respectively.
Find the median of the two sorted arrays.

Example
_____________
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.
Given A=[1,2,3] and B=[4,5], the median is 3.

Approach
_____________
The solution to his problem is solely based on solving another problem
Find kth element of two sorted arrays.


Find Kth element
++++++++++++++++++
Define Kth elements for array L as
L[k-1] (passed k element including k-1)


Divide and Conquer
++++++++++++++++++++
Two arrays
A[..a..] -- m long array
B[..b..] -- n long array
a -- k/2th element of A
b -- k/2th element of B

Base Cases:
if m == 0:
    return B[k-1]
if n == 0:
    return A[k-1]
if k==1:
    return min(A[0],B[0])

NOTES: 1. Always include k/2
       2. Notation follows python substring rules

Recurrence:
when m < k/2, it means, we spend at most k/2 - 1 at A.
==> so we DITCH  A, B[:k/2-1]
==> we recurse on None, B[k/2:]

When n < k/2, it means we spend at most k/2 -1 at B.
==> so we ditch A[:k/2-1], B
==> we recurse on A[k/2:], None

Now get a = [k/2-1], b = B[k/2 -1]

When a < b
==> [...a...]
==> [...b...]
==> elements B[k/2+1:] is at least larger than
    a. A[:k/2+1] (k/2 + 1 long)
    b. B[:k/2-1+1] (k/2 long)
    that's k+1 elements in total
    so it's at least 2 away from k-1 to the righ, we can DITCH it
==> Elements A[:k/2] is at least less than
    a. A[k/2:] (m - k/2 + 1 long)
    b. B[k/2:] (n - k/2 + 1 long)
    That's m+n -k +2 in total, at least 2 away from k-1 to the lfet,DITCH it
==> So we recurese on
    A[k/2:], B[:k/2+1], with new target k - k/2
    k-k/2 because we throw away A[:k/2] which is k/2 -1 long
    k - 1 - (k/2 -1) = k - k/2

Similar situation for a >b

After we know how to do findk, rest is trivial.


!!!!Technical notes

1. k-1 is the kth elements
2. just include k/2 whenever you can at recursion time

Compleixty
___________
Time - O(Lg(N))
Space - O(1)
"""





class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
 
    def findMedianSortedArrays(self, A, B):
        # write your code here
        if A is None or B is None:
            raise Exception
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findk(A, B, n / 2 + 1)
        else:
            return (self.findk(A, B, n / 2) + self.findk(A, B, n / 2 + 1)) / 2.0

    def findk(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])

        a = A[k / 2 - 1] if k / 2 <= len(A) else None
        b = B[k / 2 - 1] if k / 2 <= len(B) else None

        if a is None:
            return self.findk(A, B[k / 2:], k - k / 2)
        if b is None:
            return self.findk(A[k / 2:], B, k - k / 2)
        if a < b:
            return self.findk(A[k / 2:], B[:k / 2 + 1], k - k / 2)

        else:
            return self.findk(A[:k / 2 + 1], B[k / 2:], k - k / 2)
