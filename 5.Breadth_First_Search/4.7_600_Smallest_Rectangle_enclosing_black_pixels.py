"""
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region.
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
根据已有的black pixel的左边，分别找到上下左右含有1的边界，利用binary search查找。
在discuss里有很pythonic的写法，可以学习一下。 这里我根据我记忆的binary search的模板进行了修改。 基本上就是利用search for a range的写法。

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
        while start + 1 < end:
            mid = start + (end - start) / 2
            if ("1" in image[mid]) == True:
                end = mid
            else:
                start = mid
        if ("1" in image[start]) == True:
            return start
        elif ("1" in image[end]) == True:
            return end
        return end

    def searchBottom(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if ("1" in image[mid]) == True:
                start = mid
            else:
                end = mid
        if ("1" in image[end]) == True:
            return end
        elif ("1" in image[start]) == True:
            return start
        return start

    def searchLeft(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if any(image[k][mid] == "1" for k in range(len(image))) == True:
                end = mid
            else:
                start = mid
        if any(image[k][start] == "1" for k in range(len(image))) == True:
            return start
        elif any(image[k][start] == "1" for k in range(len(image))) == True:
            return end
        return end

    def searchRight(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if any(image[k][mid] == "1" for k in range(len(image))) == True:
                start = mid
            else:
                end = mid
        if any(image[k][end] == "1" for k in range(len(image))) == True:
            return end
        elif any(image[k][start] == "1"for k in range(len(image))) == True:
            return start
        return start
