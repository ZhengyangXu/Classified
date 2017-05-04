
"""
Description
____________
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

Approach/Complexity
______________

map
++++
The core is to calculate the overlap.
Have a map where
1. key is the start and end time
2. initial value is 1 for start and -1 for end
3. +1, -1 for identical start, end time

Loop through the SORTED map
record
current_rooms === current opened rooms
rooms === maximum rooms opened

return rooms


Heap
+++++
heap = []
1. Sort the intervals by start
2. loop through intervals
    start, end = interval.start, interval.end
    a. when ending comes before the new start
       if len(heap) != 0 and heap[0] <= start:
           heapq.heappop()
    b.heapq.heappush(heap, end)


Two Arrays
++++++++++
1. create two arrays of sorted starttime and endtime
    ===> starts, ends
2. res, endpoint = 0, 0
for i in starts:
    when start comes before ending, increment res, else increment endpoint

return result

Complexity
++++++++++
Time - O(Nlog(N))
Space - O(N)
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# MAP


class Solution(object):

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        from collections import defaultdict
        dic = defaultdict(int)
        for i in intervals:
            dic[i.start] += 1
            dic[i.end] -= 1
        dic = sorted(dic.items())
        current_rooms, rooms = 0, 0
        for i in dic:
            current_rooms += i[1]
            rooms = max(rooms, current_rooms)
        return rooms

# Heap

 
class Solution(object):

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        import heapq
        intervals.sort(key=lambda x: x.start)
        heap = []
        for interval in intervals:
            start = interval.start
            if len(heap) != 0 and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
        return len(heap)

# Two arrays


class Solution(object):

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])
        res, endpoint = 0, 0
        for i in starts:
            if i < ends[endpoint]:
                res += 1
            else:
                endpoint += 1
        return res
