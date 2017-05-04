"""
Description
___________
Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 (the number zero, one, two).Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to turn all people into zombies?
 Return -1 if can not turn all people into zombies.

Example
___________
Example
Given a matrix:

0 1 2 0 0
1 0 0 2 1
0 1 0 0 0
return 2


Approach
______________
BFS is a clear path
+++++++++++++++++++++
This is very similar to knights shortest path problem
except, days have to start from -1
0. get all initial zombies and add to the queue
1. for each generation infect === for all current level of nodes, reach to its one degree seperation nodes
3. each generation we increment days by one

4. if no 0 left in the end, return days - 1 else None


Complexity
________________
Time
O(M*N)

space
O(M*N)
"""


class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer

    def zombie(self, grid):
        from collections import deque
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        if n == 0:
            return -1
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        q = deque()
        days = -1
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    q.append((i, j))
  
        while q:
            size = len(q)
            for i in xrange(size):
                cur_x, cur_y = q.popleft()
                for x, y in directions:
                    new_x, new_y = cur_x + x, cur_y + y
                    if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and grid[new_x][new_y] == 0:
                        grid[new_x][new_y] = 1
                        q.append((new_x, new_y))

            days += 1

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 0:
                    return -1
        return days
