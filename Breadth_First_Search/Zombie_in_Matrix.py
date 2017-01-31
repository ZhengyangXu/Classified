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
0. get all initial zombies and add to the queue
1. for each generation infect === for all current level of nodes, reach to its one degree seperation nodes
3. each generation we increment days by one

4. if no 0 left in the end, return days else None


Complexity
________________
Time
O(N)

space
O(1)
"""


class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer

    def zombie(self, grid):
        # Write your code here

        days = 0
        q = []

        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        if n == 0:
            return -1
        unit_vectors = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    code = i * n + j
                    q.insert(0, code)

        while len(q) != 0:
            days += 1
            size = len(q)
            for i in xrange(size):
                cur = q.pop()
                cur_i = cur / n
                cur_j = cur % n
                for v in unit_vectors:
                    new_i = cur_i + v[0]
                    new_j = cur_j + v[1]

                    if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and grid[new_i][new_j] == 0:
                        grid[new_i][new_j] = 1
                        q.insert(0, new_i * n + new_j)

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 0:
                    return -1
        return days - 1
