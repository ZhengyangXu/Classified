"""
Description
__________
Given an integer array, find the top k largest numbers in it.

Example
____________
Given [3,10,1000,-99,4,100] and k = 3.
Return [1000, 100, 10].


Approach
____________
Maintain a size k minheap to pop off n-k smallest element
(for loop through all elements pop on and when size >k, pop off)

The resulted heap contains top largest elements reversely ordered

Complexity
____________
Time - O(N.Lg(K))
Space - K
"""

import heapq


class T:

    def __init__(self, v):
        self.v = v

    def __cmp__(self, other):
        return -(other.v - self.v)


class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''

    def topk(self, nums, k):
        # Write your code here
        if nums is None:
            return
        import heapq
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)
        result = [0 for _ in xrange(k)]
        index = k - 1
        # print heap
        while heap:
            t = heapq.heappop(heap)
            # print t
            result[index] = t
            index -= 1

        return resultx
