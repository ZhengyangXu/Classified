"""
Description
___________________
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

Integers in each row are sorted from left to right.
Integers in each column are sorted from up to bottom.
No duplicate integers in each row or column.


Example
Consider the following matrix:

[
  [1, 3, 5, 7],
  [2, 4, 7, 8],
  [3, 5, 9, 10]
]
Given target = 3, return 2.

Approach
_____________________
search from row's max and col's mnimum
to
row's max and cols' minimum
"""


class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return 0

        if matrix[0] is None or len(matrix[0]) == 0:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        x = m - 1
        y = 0
        count = 0
        while x >= 0 and y < n:
            if target > matrix[x][y]:
                y += 1
            elif target < matrix[x][y]:
                x -= 1
            else:
                y += 1
                x -= 1
                count += 1
        return count
