"""
Description
____________
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Approach/ Complexity
______________
stack
++++++
idea is always maintain a decreasing wall, when see a increasing wall at i
bot = height[stack[-1].pop]
lh = height[stack[-1]]
rh = height[i]
cur_area = (min(lh, rh) - bot) * (i - stack[-1] -1 )
Edge case, when there is no lh, cur_area = 0

Thinks about different with the rectangle problem

Time - O(N)
Space - O(N)


Two pointers
++++++++++++++
maintain - leftmax, rightmax, water
two pointers
left,right = 0 , len(N) -1

when leftmax < rightmax:
    we can collect leftmax - height[left]
    left += 1
similar to rightmax > leftmax

"""
 

class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack, maxwater = collections.deque(), 0
        for i in xrange(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bot = height[stack.pop()]
                cur_area = ((min(height[stack[-1]], height[i]) - bot)
                            * (i - stack[-1] - 1))if stack else 0
                maxwater += cur_area
            stack.append(i)
        return maxwater


class Solution(object):

    def trap(self, height):
        left, right = 0, len(height) - 1
        leftmax, rightmax = 0, 0
        water = 0
        while left < right:
            leftmax, rightmax = max(height[left], leftmax), max(height[right], rightmax)
            if leftmax < rightmax:
                water += leftmax - height[left]
                left += 1
            else:
                water += rightmax - height[right]
                right -= 1

        return water
