"""
Description
==========================
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example
============================
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.
================================
Due to the constraint, this is can be flattened to a 1D sequence with equation

col*x + y = a
x = a/col
y = a%col


2 binary search is to

search column wise find last position <= targret

then search rowwise first postion == target 
"""


class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix == None or len(matrix) == 0 or matrix[0] == None or len(matrix[0]) == 0:
            return False
        row, col = len(matrix), len(matrix[0])
        start, end = 0, col * (row - 1) + col - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            mid_x, mid_y = mid / col, mid % col
            if matrix[mid_x][mid_y] == target:
                return True
            elif matrix[mid_x][mid_y] < target:
                start = mid
            else:
                end = mid
        if matrix[start / col][start % col] == target or matrix[end / col][end % col] == target:
            return True
        return False
