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
    Dfs on current island to flip all 1s that constructed this island to 0
    count how many ones there are
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
                    self.dfs(grid, i, j)
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
