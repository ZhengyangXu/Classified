"""
Description
_____________________________
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position,
find the shortest path to a destination position, return the length of the route.
Return -1 if knight can not reached.

Example
_______________________________

[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 2

[[0,1,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 6

[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return -1

Approach
____________________________________________
Standard BFS
++++++++++++
use standard BFS here, a few things to notice here
0. knight walks the sun so directions are like that
1. instead of using visited, every time we visit, a point at grid
we mark that as 1
"""


class Solution:
    # @param {boolean[][]} grid a chessboard included 0 (False) and 1 (True)
    # @param {Point} source a point
    # @param {Point} destination a point
    # @return {int} the shortest path

    def shortestPath(self, grid, source, destination):
        directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        m, n = len(grid), len(grid[0])
        import sys
        from collections import deque
        q = deque()
        s_x, s_y = source.x, source.y
        d_x, d_y = destination.x, destination.y
        end = (d_x, d_y)
        q.append((s_x, s_y)) 
        steps = 0
        while q:
            size = len(q)
            for i in xrange(size):
                cur = q.popleft()
                if cur == end:
                    return steps
                for d in directions:
                    new_x = cur[0] + d[0]
                    new_y = cur[1] + d[1]
                    if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and not grid[new_x][new_y]:
                        grid[new_x][new_y] = 1
                        q.append((new_x, new_y))
            steps += 1
        return -1
