"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.

Approach
______________________
Key is we want to caculate for each bar say X, we want to get the rectangle consists
of X as the smallest bar
Now, we can use a stack to accomplish this

- when we meet a height, say h, that is lower than the stack's top ==>
 all the bars stored in the stack that has height >= h will be right bounded by h
 (Remember we are calculating the area with ‘x’ as the smallest bar in the rectangle.
- At that moment, since in the stack, we are maintaining a increasing height in the stack
 every time we check a bar that is right bounded by h
 will also be left bounded by the height that is previous stored in the stack.
 So the width would go from stack[-1] + 1 to i - 1 included, which is i - stack[-1] - 1
- If we are examing the last element in the stack, t
his means he is the lowest till the leftmost of the histogram,
so the width would become index 0 through index i-1 included, which is i


Edge cases
- when stack empty, width = i
- add a 0 to height to get the last rectangle


Complexity
___________
Time - O(N)
Space - O(N)
"""
 

class Solution(object):

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        from collections import deque
        heights += [0]
        stack = deque()
        maxarea = 0

        for i in xrange(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                h = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                maxarea = max(maxarea, h * width)
            stack.append(i)
        return maxarea
