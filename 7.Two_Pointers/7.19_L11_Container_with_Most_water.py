"""
Description
______________
Given n non-negative integers a1, a2, ..., an, where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines
which together with x-axis forms a container
such that the container contains the most water.

Approach
_______________
two pointers
++++++++++++++
maintain - maxArea

left, right = 0, len(nums) - 1

moving of the higher wall does not affect the area, so at every iteration
we just need to move the shorter wall

See code

complexity
_____________
Time - O(N)
Space - O(1)
"""


class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxarea = 0
        while left < right:
            if height[left] < height[right]:
                maxarea = max(height[left] * (right - left), maxarea)
                left += 1
            else:
                maxarea = max(height[right] * (right - left), maxarea)
                right -= 1
        return maxarea
