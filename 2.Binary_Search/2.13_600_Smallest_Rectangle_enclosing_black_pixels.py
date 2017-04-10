"""
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel.jiu The black pixels are connected, i.e., there is only one black region.
Pixels are connected horizontally and vertically.
Given the location (x, y) of one of the black pixels,
return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Have you met this question in a real interview? Yes
Example
For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2,
Return 6.


Approach
_________________________
Binary search
++++++++++++
Perform 4 binary searches to get 4 boundaries
0. top boundary ---> rowwise to search for the first 1 (0 to x)
1. bottom bounday ---> rowsie to earch for last 1 (x to end)
2. left boundary ---> colwise to search for first 1 (0 to y)
3. right boundaty ---> colwise to search for last 1 (y to end)

Compleixty
___________
O(Lg(M*N))
"""


class Solution(object):

    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: intz
        :type y: int
        :rtype: int
        """
        if not image:
            return 0

        top = self.searchTop(image, 0, x)
        bottom = self.searchBottom(image, x, len(image) - 1)
        left = self.searchLeft(image, 0, y)
        right = self.searchRight(image, y, len(image[0]) - 1)
        return (right - left + 1) * (bottom - top + 1)

    def searchTop(self, image, start, end):
        # Rowwise
        # search for first position with start =0 and end as x
        while start + 1 < end:
            mid = start + (end - start) / 2
            if '1' in image[mid]:
                end = mid
            else:
                start = mid
        if '1' in image[start]:
            return start
        return end

    def searchBottom(self, image, start, end):
        # RowWise
        # search for last position with start as x and end as end of rows
        while start + 1 < end:
            mid = start + (end - start) / 2
            if '1' in image[mid]:
                start = mid
            else:
                end = mid
        if '1' in image[end]:
            return end
        return start

    def searchLeft(self, image, start, end):
        # ColumnWise
        # search for first position  with start as 0 and y as end

        while start + 1 < end:
            mid = start + (end - start) / 2
            if '1' in [row[mid] for row in image]:
                end = mid
            else:
                start = mid
        if '1' in [row[start] for row in image]:
            return start
        return end

    def searchRight(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if '1' in [row[mid] for row in image]:
                start = mid
            else:
                end = mid

        if '1' in [row[end] for row in image]:
            return end
        return start
