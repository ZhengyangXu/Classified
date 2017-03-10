"""
Given k sorted integer arrays, merge them into one sorted array.

Example
__________
Given 3 sorted arrays:

[
  [1, 3, 5, 7],
  [2, 4, 6],
  [0, 8, 9, 10, 11]
]
return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].


Approach
____________
heap
+++++++
Very similar approach to last one
use a minheap again (have to redefine the comparator though)


complexity
__________
Time - O(Nlg(k))
Space - O(Ki)
"""


class T:

    def __init__(self, l):
        self.l = l

    def __cmp__(self, other):
        return self.l[0] > other.l[0]


class Solution:
    # @param {int[][]} arrays k sorted integer arrays
    # @return {int[]} a sorted array

    def mergekSortedArrays(self, arrays):
        # Write your code here
        if arrays is None:
            return []
        import heapq
        minheap = []
        result = []
        for i in arrays:
            if i:
                heapq.heappush(minheap, i)
        while minheap:
            cur = heapq.heappop(minheap)
            result.append(cur.pop(0))
            if cur:
                heapq.heappush(minheap, cur)
        return result
