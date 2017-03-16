"""
Description
___________
Find the kth smallest number in at row and column sorted matrix.]]

Example
___________
Given k = 4 and a matrix:

[
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
return 5

Approach/Complexity
__________________
BFS + minheap
++++++++++++
0. Start from smallest element [0][0]
1. BFS on [(1,0),(0,1)] (only two choices to increase since sorted).
   *Add unvisited edge to a minheap
2. Return the node we popped at k time

Complexity
Time - O(K*Lg(K))
Space - O(K)


Binary Search
++++++++++++
count(mid) -- how many elements in matrix are less/equal to value mid
k -- target kth element
Constraint: count >= k
goal: first element satisefies the constraint
Range : min(matrix[0][0]), max(matrix[m-1][n-1])
although we are trying to find count == k because
0. not all number is in matrix while searching
1. there will be duplicates and count will count the last one

This simply translates to

    start, end = matrix[0][0], matrix[m-1][n-1]
    while start+1 < end:
        mid = start + (end-start)/2
        count = self.count(matrix,mid)
        if count == k:
            end = mid
        elif count > k:
            end = mid
        else:
            start = mid
    if self.count(matrix,start)>=k:
        return start
    else:
        return end


This binary search utilizes count method, here is how it works
we start from lower left corner where rowwise max, colwise smallest

[
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]

at the current position i,j all i+1 elements are <= matrix[i][j]
and  it's sorted
0. when matrix[i][j] <= target
    count += i+ 1
    j += 1 (go to the larger elements)
1. when matrix[i][j] > target:
    i-= 1 (go to smaller elements)

    def count(self,matrix,target):
        m = len(matrix)
        n = len(matrix[0])
        i = m-1
        j = 0
        count = 0
        while (i>=0 and j<n):
            if matrix[i][j] <= target:
                count += (i+1)
                j+=1
            else:
                i-=1
        return count

This is very similar to search in matrix



Time -  Count takes O(max(M,N)), binary search takes O(Lg(Maximum-Minimum))
        O((M+N) * O(Lg(Maximum-Minimum))= O( (M+N)*Lg(Maximum-Minimum)   )
Space - O(1)
"""


# BFS + minheap
class T:

    def __init__(self, pos, v):
        self.pos = pos
        self.v = v

    def __cmp__(self, other):
        return self.v - other.v


class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix

    def kthSmallest(self, matrix, k):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return

        m = len(matrix)
        if matrix[0] is None or len(matrix[0]) == 0:
            return
        n = len(matrix[0])

        directions = [(1, 0), (0, 1)]
        import heapq
        minheap = []
        count = 0
        s = set([])
        origin = T((0, 0), matrix[0][0])
        heapq.heappush(minheap, origin)
        s.add(origin.pos)
        while count <= k:
            cur = heapq.heappop(minheap)
            count += 1
            if count == k:
                return cur.v
            for dx, dy in directions:
                cur_x, cur_y = cur.pos
                new_x, new_y = (cur_x + dx, cur_y + dy)
                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and ((new_x, new_y) not in s):
                    s.add((new_x, new_y))
                    heapq.heappush(minheap, T((new_x, new_y), matrix[new_x][new_y]))


# Binary Search
class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix

    def kthSmallest(self, matrix, k):
        if matrix is None or len(matrix) == 0:
            return
        m = len(matrix)
        if matrix[0] is None or len(matrix[0]) == 0:
            return
        n = len(matrix[0])
        start, end = matrix[0][0], matrix[m - 1][n - 1]
        while start + 1 < end:
            mid = start + (end - start) / 2
            # print mid,start,end
            count = self.count(matrix, mid)
            # print "count",count
            if count == k:
                end = mid
            elif count > k:
                end = mid
            else:
                start = mid

        if self.count(matrix, start) >= k:
            return start
        else:
            return end

    def count(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        i = m - 1
        j = 0
        count = 0
        while (i >= 0 and j < n):
            if matrix[i][j] <= target:
                count += (i + 1)
                j += 1
            else:
                i -= 1
        return count
