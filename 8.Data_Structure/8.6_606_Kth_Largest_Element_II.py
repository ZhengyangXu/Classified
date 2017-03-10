"""
Description
___________
Find K-th largest element in an array. and N is much larger than k.

Approach
___________
Since N is much larger than K, we can then maintain a k size minheap
which will filter out (n-k) smallest elements
then at the top is our kth largest element

Compleixty
__________
Time - O(NLg(K))
Space - O(Lg(K))
"""


class Solution:
    # @param nums {int[]} an integer unsorted array
    # @param k {int} an integer from 1 to n
    # @return {int} the kth largest element

    def kthLargestElement2(self, nums, k):
        # Write your code here
        import heapq
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)
