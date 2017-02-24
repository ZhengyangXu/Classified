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


public class Solution {
    int n, m; // size of the chessboard
    int[] deltaX = {1, 1, 2, 2, -1, -1, -2, -2};
    int[] deltaY = {2, -2, 1, -1, 2, -2, 1, -1};
    /**
     * @param grid a chessboard included 0 (false) and 1 (true)
     * @param source, destination a point
     * @return the shortest path
     */
    public int shortestPath(boolean[][] grid, Point source, Point destination) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return -1;
        }

        n = grid.length;
        m = grid[0].length;

        Queue<Point> queue = new LinkedList<>();
        queue.offer(source);

        int steps = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Point point = queue.poll();
                if (point.x == destination.x && point.y == destination.y) {
                    return steps;
                }

                for (int direction = 0; direction < 8; direction++) {
                    Point nextPoint = new Point(
                        point.x + deltaX[direction],
                        point.y + deltaY[direction]
                    );

                    if (!inBound(nextPoint, grid)) {
                        continue;
                    }

                    queue.offer(nextPoint);
                    // mark the point not accessible
                    grid[nextPoint.x][nextPoint.y] = true;
                }
            }
            steps++;
        }

        return -1;
    }

    private boolean inBound(Point point, boolean[][] grid) {
        if (point.x < 0 || point.x >= n) {
            return false;
        }
        if (point.y < 0 || point.y >= m) {
            return false;
        }
        return (grid[point.x][point.y] == false);
    }
}
"""


class Solution:
    # @param {boolean[][]} grid a chessboard included 0 (False) and 1 (True)
    # @param {Point} source a point
    # @param {Point} destination a point
    # @return {int} the shortest path

    def shortestPath(self, grid, source, destination):
        # Write your code here
        n = len(grid)
        m = len(grid[0])

        import sys
        record = [[sys.maxint for _ in xrange(m)] for i in xrange(n)]
        record[source.x][source.y] = 0

        from collections import deque
        q = deque()
        q.append(source)
        d = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        while q:
            cur = q.popleft()
            for dx, dy in d:
                x, y = cur.x + dx, cur.y + dy
                if x >= 0 and x < n and y >= 0 and y < m and not grid[x][y] and \
                        record[cur.x][cur.y] + 1 < record[x][y]:
                    record[x][y] = record[cur.x][cur.y] + 1

                    q.append(Point(x,y))

        if record[destination.x][destination.y] == sys.maxint:
            return -1

        return record[destination.x][destination.y]
# Plane my version check


class Solution:

    def shortestPath(self, grid, source, destination):
        directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        if grid is None or source is None or destination is None:
            return -1
        from collections import deque
        q = deque()
        q.append(source)
        steps = 0
        m = len(grid)
        n = len(grid[0])
        while not q.empty():
            size = len(q)
            for i in xrange(size):
                cur = q.popleft()
                if cur.x == destination.x and cur.y == destination.y:
                    return steps
                for i, j in directions:
                    new_x, new_y = i + cur.x, j + cur.y
                    if not(new_x < 0 or new_y < 0 or new_x >= m or new_y >= n):
                        q.append(Point(i + cur.x, j + cur.y))
            steps += 1

        return -1
