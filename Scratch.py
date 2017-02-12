# class Solution:
#     # @param {boolean[][]} grid a boolean 2D matrix
#     # @return {int} an integer
#
#     def numIslands(self, grid):
#         print "hello world"
#         m = len(grid)
#         if m <= 0:
#             return 0
#         n = len(grid[0])
#         if n < 0:
#             return 0
#         counter = 0
#         for i in xrange(m):
#             for j in xrange(n):
#                 if grid[i][j]:
#                     print "enter"
#                     self.dfs(grid, i, j, m, n)
#                     counter += 1
#         return counter
#
#     def dfs(self, grid, i, j, m, n):
#         if i < 0 or i >= m or j < 0 or j >= n:
#             return
#
#         if grid[i][j]:
#             grid[i][j] = 0
#             self.dfs(grid, i + 1, j, m, n)
#             self.dfs(grid, i - 1, j, m, n)
#             self.dfs(grid, i, j + 1, m, n)
#             self.dfs(grid, i, j - 1, m, n)
#         else:
#             return


# class UndirectedGraphNode:
#
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
#
#
# class Solution:
#     # @param {UndirectedGraphNode[]} graph a list of undirected graph node
#     # @param {dict} values a dict, <UndirectedGraphNode, (int)value>
#     # @param {UndirectedGraphNode} node an Undirected graph node
#     # @param {int} target an integer
#     # @return {UndirectedGraphNode} a node
#
#     def searchNode(self, graph, values, node, target):
#         # Write your code here
#         if node is None or target is None or graph is None:
#             return
#         return self.dfs(graph, values, node, target)
#
#
#     def dfs(self, graph, values, node, target):
#         if node is None:
#             return
#         if values[node.label] == target:
#             return node
#         for n in node.neighbors:
#             self.dfs(graph, values, n, target)

#
# class Solution:
#     # @param {int} numCourses a total of n courses
#     # @param {int[][]} prerequisites a list of prerequisite pairs
#     # @return {boolean} true if can finish all courses or false
#
#     def canFinish(self, numCourses, prerequisites):
#         edges = {i: [] for i in xrange(numCourses)}
#         indegrees = [0 for i in xrange(numCourses)]
#
#         for i, j in prerequisites:
#             indegrees[i] += 1
#             edges[j].append(i)
#
#         import Queue
#         q = Queue.Queue()
#         count = 0
#
#         for i in xrange(len(indegrees)):
#             if indegrees[i] == 0:
#                 q.put(i)
#         while not q.empty():
#             cur = q.get()
#             count += 1
#
#             for next_course in edges[cur]:
#                 indegrees[next_course] -= 1
#                 if indegrees[next_course] == 0:
#                     q.put(next_course)
#         return count == numCourses


# class Solution:
#
#     def shortestPath(self, grid, source, destination):
#         directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
#         if grid is None or source is None or destination is None:
#             return -1
#         import Queue
#         q = Queue.Queue()
#         q.put(source)
#         steps = 0
#         m = len(grid)
#         n = len(grid[0])
#         while not q.empty():
#             size = q.qsize()
#             for i in xrange(size):
#                 cur = q.get()
#                 if cur.x == destination.x and cur.y == destination.y:
#                     return steps
#                 for i, j in directions:
#                     new_x, new_y = i + cur.x, j + cur.y
#                     if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n
#                     q.put(Point(i + cur.x, j + cur.y))
#             steps += 1
#
#         return -1

# col * x + y = a
# x = a/ col
# y = a% col

# class Solution:
#
#     def searchMatrix(self, matrix, target):
#
#         if matrix is None or len(matrix) == 0 or matrix[0] or target is None:
#             return False
#         row, col = len(matrix), len(matrix[0])
#         start, end = 0, (row - 1) * col + col - 1
#
#         while start + 1 < end:
#             mid = start + (end - start) / 2
#             mid_x, mid_y = mid / col, mid % col
#             if matrix[mid_x][mid_y] == target:
#                 return True
#             elif target > matrix[mid_x][mid_y]:
#                 start = mid
#             else:
#                 end = mid
#         if matrix[start / col][start % col] == target or matrix[end / col][end % col]:
#             return True
#         return False

#
# class Solution:
#
#     def woodcut(self, L, k):
#         if sum(L) < k:
#             return 0
#         start, end = 0, max(L)
#         while start + 1 < end:
#             mid = start + (end - start) / 2
#
#             mid_pieces = sum([l / mid for l in L])
#             if mid_pieces == k:
#                 start = mid
#             elif mid_pieces < k:
#                 end = mid
#             else:
#                 start = mid


"""

  0  1  2
0
1 w  w  X
2
3
4
"""
# Minimize the largest partition sum

#B[0....n]
# DP[i] = K<-0...i Min(DP[k],sum(B[k:i])

class Solution:
    def copyBooks(self, pages, k):
        import sys
        if len(pages) == 0:
            return 0
        prefix_sum = pages[:]
        for i in xrange(1,len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i-1] + prefix_sum[i]

        m = len(pages)
        DP = [[0 for _ in xrange(k)] for _ in xrange(m)]
        # 0 as 1 in DP
        for i in xrange(m):
            for j in xrange(k):

                if j == 0:
                    DP[i][j] = prefix_sum[i]
                elif i ==0 :
                    DP[i][j] = pages[0]
                else:
                    minimum = sys.maxint
                    for p in xrange(i):
                        minimum = min(minimum, max(prefix_sum[i]-prefix_sum[p], DP[p][j-1]))
                    DP[i][j] = minimum

        return DP[m-1][k-1]




# Smart as fuck binary search
# constraint copiers <= k
# searching the minimum max_page_per_person to satisefy constraint
class Solution:
    def copyBooks(self, pages, k):
        if len(pages) == 0:
            return 0
        start, end = max(pages), end = sum(pages)
        while start + 1 < end:
            mid = start + (end - start) / 2
            copiers = self.getRequiredCopiers(pages, mid)
            if copiers == k:
                end = mid
            elif copiers < k:
                end = mid
            else:
                start = mi
        # = k because we allow assign 0 to a copier
        if (self.getRequiredCopiers(pages,start) <=k )


    def getRequriedCopiers(pages, max_page_per_person):
        _sum = 0
        copiers = 0
        for p in pages:
            _sum += p
            if _sum > max_page_per_person:
                copiers += 1
                _sum = 0
        return copiers
