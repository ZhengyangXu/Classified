"""
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Example
___________
Given graph:

[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
return 3.

Approach
___________
Loop through
    Dfs/BFS on current island to flip all 1s that constructed this island to 0
    count how many ones there are

Complexity
O(M*N)
"""


class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer

    def numIslands(self, grid):
        # Write your code here
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        count = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j]:
                    count += 1
                    self.bfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if grid[i][j]:
            grid[i][j] = 0
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i, j + 1)

    def bfs(self, grid, i, j):
        from collections import deque
        m = len(grid)
        n = len(grid[0])
        q = deque()
        q.append((i, j))
        while q:
            x, y = q.popleft()
            if grid[x][y]:
                grid[x][y] = 0
                if self.inbound(x - 1, y, m, n):
                    q.append((x - 1, y))
                if self.inbound(x + 1, y, m, n):
                    q.append((x + 1, y))
                if self.inbound(x, y - 1, m, n):
                    q.append((x, y - 1))
                if self.inbound(x, y + 1, m, n):
                    q.append((x, y + 1))

    def inbound(self, i, j, m, n):
        return i <= m - 1 and i >= 0 and j >= 0 and j <= n - 1
