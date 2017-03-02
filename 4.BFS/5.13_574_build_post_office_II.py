"""
 Description
_________________

Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0 (the number zero, one, two), find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.

Return the smallest sum of distance. Return -1 if it is not possible.

Notes
_________
You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.
Have you met this question in a real interview? Yes

Example
___________
Given a grid:

0 1 0 0 0
1 0 0 2 1
0 1 0 0 0

Approach
____________
Compared to I, We cannot go through walls, have to use BFS now
BFS
++++++++++++++++
0. get all empty coordinates and houses => empites, houses
1. For each house, do a BFS
    maintian
    a. visitedCount -- hashmap where k->empty coord; v->num visited by houses
    b. DistanceSums -- hashmap where k->empty coord; v->sum(distance from each house)
2. loop through empties:
    if visitedCount[empty] == len(houses):
        minimum = min(minimum, distanceSums[empty])
3. Return minimum if it's not maxint
"""


class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer

    def shortestDistance(self, grid):
        # Write your code here
        if grid is None:
            return -1
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        m = len(grid)
        n = len(grid[0])
        empties = []
        houses = []
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 0:
                    empties.append((i, j))
                elif grid[i][j] == 1:
                    houses.append((i, j))

        distanceSums, visitedCount = {k: 0 for k in empties}, {k: 0 for k in empties}
        for house in houses:
            self.bfs(house, grid, distanceSums, visitedCount)

        import sys
        minimum = sys.maxint
        # print distanceSums
        # print visitedCount
        for empty in empties:
            if visitedCount[empty] == len(houses):
                minimum = min(minimum, distanceSums[empty])
        if minimum == sys.maxint:
            return -1
        return minimum

    def bfs(self, start, grid, distanceSums, visitedCount):
        # distanceSums is only accurate when visitedCount reach the value
        from collections import deque
        visited = set([])
        q = deque()
        m = len(grid)
        n = len(grid[0])

        q.append(start)
        visited.add(start)

        steps = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            size = len(q)
            for i in xrange(size):
                cur = q.popleft()
                if cur != start:
                    visitedCount[cur] += 1
                    distanceSums[cur] += steps
                cur_x, cur_y = cur
                for x, y in directions:
                    new_x, new_y = cur_x + x, cur_y + y
                    if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and (new_x, new_y) not in visited and grid[new_x][new_y] == 0:
                        q.append((new_x, new_y))
                        visited.add((new_x, new_y))
            steps += 1
