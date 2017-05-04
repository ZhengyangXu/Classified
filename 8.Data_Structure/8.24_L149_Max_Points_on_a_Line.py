"""
Given n points on a 2D plane, find the maximum number of points
that lie on the same straight line.
"""


class Solution(object):

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        maximum = 0
        for i in xrange(len(points)):
            cur = self.helper(i, points)
            if cur > maximum:
                maximum = cur
        return maximum

    def helper(self, index, points):
        slopes = []
        origin_count = 0
        origin = points[index]
        for i in xrange(len(points)):
            cur_slope = self.slope(points[i], origin)
            if cur_slope == 'dummy':
                origin_count += 1
            else:
                slopes.append(cur_slope)
        # print slopes
        if slopes:
            r = origin_count + sorted((collections.Counter(slopes)).values())[-1]
        else:
            r = origin_count
        return r

    def slope(self, a, b):
        from decimal import Decimal
        if a.x == b.x and a.y == b.y:
            return "dummy"
        if a.x == b.x:
            return sys.maxint
        return Decimal(b.y - a.y) / (a.x - b.x)
