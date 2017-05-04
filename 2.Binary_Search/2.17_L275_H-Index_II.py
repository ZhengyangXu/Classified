"""
Description
_____________

Follow up for H-Index: What if the citations array is sorted in ascending order?
Could you optimize your algorithm?

Approach
______________
Binary Search
++++++++++++++
If the array is already sorted, we just need to find the last position (reversely)
where the index (count) is larger than the current value
This translates to

First postion where value > len(citations) - index
Rest is straightforwad 
"""

# class Solution(object):
#     def hIndex(self, citations):
#         """
#         :type citations: List[int]
#         :rtype: int
#         """
#         for i,v in enumerate(reversed(citations)):
#             if i >= v:
#                 return i
#         return len(citations)


class Solution(object):

    def hIndex(self, citations):
        if not citations:
            return 0
        start, end = 0, len(citations) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if citations[mid] >= len(citations) - mid:
                end = mid
            else:
                start = mid
        if citations[start] >= len(citations) - start:
            return len(citations) - start
        elif citations[end] >= len(citations) - end:
            return len(citations) - end
        return 0
