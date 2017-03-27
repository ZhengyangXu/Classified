"""
Description
===========
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.

Approach
===========
0. Sort the array by start time
1. scan through the array and terminate if we see any comflict

Complexity
===========
Time - O(N.Lg(N))
Space - O(1)
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        def sorter(interval):
            return interval.start
        intervals = sorted(intervals, key=sorter)
        # for interval in sorted_starting_time:
        #     print interval.start, interval.end
        for i in xrange(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True
