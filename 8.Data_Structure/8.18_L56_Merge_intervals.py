"""
Description
______________
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals is None or len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x.start)
        output = [intervals[0]]
        for i in xrange(1, len(intervals)):
            if intervals[i].start <= output[-1].end:
                output[-1].end = max(output[-1].end, intervals[i].end)
            else:
                output.append(intervals[i])
        # print output
        return output
