"""
Description
________________

Given a 2D grid, each cell is either an house 1 or empty 0 (the number zero, one),
find the place to build a post office
the distance that post office to all the house sum is smallest.
Return the smallest distance. Return -1 if it is not possible.

Notice
_________________
You can pass through house and empty.
You only build post office on an empty.

Example
__________________
Given a grid:

0 1 0 0
1 0 1 1
0 1 0 0
return 6. (Placing a post office at (1,1),
the distance that post office to all the house sum is smallest.)

Appraoch
______________
The naive approach
++++++++++++++++++
0. get the position of all houses
1. loop through each point in the grid and calcualte Mahathan distance
   update res = min(res, cur_dist)
2. return minimum
This will have O(MN) worst case happen when num(houses) == num(empty)

The clever as fk Approach
+++++++++++++++++++++++++
When mahatthan distance, it's likely we can process Xs and Ys seperately

Let's call it (PS)prefix_sum, suffix_sum approach
Since we only want to know sum (distance between ech house, point) for each point
we can do
0. figure out sum(distance from each house to point's row)
1. figure out sum(distance from each house to point's col)
2. Sum 0 one 1 to get mahathan distance

EG. grid given above
(1). we use rowCoun to store how many houes per row -> rowCount = [1,3,1]
(2). sum of all house to row i should be
sum = 0
for j = 0 to numofrow
sum += abs(i-j)*rowCount[j]
in other words
sum = calcuate (i-j) * rowcount[j] where j is less than i + ............j is bigger than i

The way we actually calculate sum is
to calcuate where j is less than i

prefix_sum[i] = rowCount[i] + prefix_sum1[i-1]
prefix_sum_new[i] = prefix_sum_new[i-1]+prefix_sum[i-1]

This is how it works
(0). prefix_sum gives us prefix_sum till current i
                                                                                                    (previous level)      ( one more level)
(1). prefix_sum_new[i] is saying move all touhced elements down one more level from previous level ==> prefix_sum_new[i-1] + prefix_sum[i-1]

now do similar thing for j is bigger than i to increment prefix_sum_newii


So now given 0,1,2
we just need to loop through all empty coords and figure out the minimum


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

        rowCount = [0 for _ in xrange(m)]
        colCount = [0 for _ in xrange(n)]
        empties = []
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j]:
                    rowCount[i] += 1
                    colCount[j] += 1
                else:
                    empties.append((i, j))

        rowAns, colAns = self.getHouseSum(rowCount), self.getHouseSum(colCount)

        import sys
        minimum = sys.maxint

        for i, j in empties:
            minimum = min(minimum, rowAns[i] + colAns[j])

        return minimum

    def getresult(self, levelcount):
        # return housesum-[....]
        # housesum_x[i.x] + housesum_y[i.y] is the mahantahn distance sum for point
        # i to all houses
        n = len(levelcount)
        # j < i
        prefix_sum = [0 for _ in xrange(n)]
        prefix_sum[0] = levelcount[0]
        for i in xrange(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + levelcount[i]
        result = [0 for _ in xrange(n)]
        for i in xrange(1, n):
            result[i] = prefix_sum[i - 1] + result[i - 1]
        return result

    def getHouseSum(self, levelcount):
        n = len(levelcount)
        new_result = [0 for _ in xrange(n)]
        # j < i
        result = self.getresult(levelcount)

        # j >i
        levelcount.reverse()
        reversed_result = self.getresult(levelcount)
        reversed_result.reverse()
        for i in xrange(n):
            new_result[i] = result[i] + reversed_result[i]
        return new_result
