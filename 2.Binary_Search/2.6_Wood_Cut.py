"""
Description
_______________________
Given n pieces of wood with length L[i] (integer array).
Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length.
What is the longest length you can get from the n pieces of wood? \Given L & k, return the maximum length of the small pieces.

Example
______________________
For L=[232, 124, 456], k=7, return 114.

Approach
______________________
Binary search
++++++++++++++
l - length of small piece
L - collections of all current piceces
maxlength - max(L)
Range:
Contraint: the pieces generated of current l is bigger or equal to k

Goal: find the largest (last position) of l

range: 1, maxlength

Compleixty
______________
N - length of L
k = max(L)

Time - O(Nlg(k))
Space - O(1)
"""

def woordcut(nums):
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start)/2
        pieces = [i/mid for i in L]
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """

    def woodCut(self, L, k):
        if sum(L) < k:
            return 0

        maxLen = max(L)
        start, end = 1, maxLen
        while start + 1 < end:
            mid = (start + end) / 2
            pieces = sum([l / mid for l in L])
            if pieces >= k:
                start = mid
            else:
                end = mid

        if sum([l / end for l in L]) >= k:
            return end
        return start
