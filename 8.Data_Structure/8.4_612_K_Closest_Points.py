
"""
Description
___________
Given some points and a point origin in two dimensional space,
find k points out of the some points which are nearest to origin.
Return these points sorted by distance, if they are same with distance,
sorted by x-axis, otherwise sorted by y-axis.

Example
___________
Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
return [[1,1],[2,5],[4,4]]

Appproach
____________
Similar heappop Approach
0. maintain a size k MAXHEAP, so we will pop out (n-k) largest distance points
1. then get all left k closest points on the heap

Note:
0. when find small, create maxheap, vice versa
1. to implement maxheap we have to havea wrapper object T


Complexity
___________
Time - O(N.Lg(K))
Space - O(Lg(K))
"""
class T:

    def __init__(self, dist, point):
        self.dist = dist
        self.point = point

    def __cmp__(self, other):
        if self.dist != other.dist:
            return other.dist - self.dist
        if other.point.x != self.point.x:
            return other.point.x - self.point.x
        return other.point.y - self.point.y

 
class Solution:
    # @param {Pint[]} points a list of points
    # @param {Point} origin a point
    # @param {int} k an integer
    # @return {Pint[]} the k closest points

    def kClosest(self, points, origin, k):
        # Write your code here
        if points is None:
            return -1
        heap = []
        import heapq
        for point in points:
            dist = self.getDistance(origin, point)
            heapq.heappush(heap, T(dist, point))
            if len(heap) > k:
                heapq.heappop(heap)

        result = [0 for _ in range(k)]
        for i in xrange(k - 1, -1, -1):
            result[i] = heapq.heappop(heap).point
        return result

    def getDistance(self, origin, point):
        return (origin.x - point.x) * (origin.x - point.x) + (origin.y - point.y) * (origin.y - point.y)
