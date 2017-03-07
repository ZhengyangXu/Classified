"""
Description
___________
Given an array with n objects colored red, white or blue
sort them so that objects of the same color are adjacent
with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color
red, white, and blue respectively.

Approach/Compleixty
______________
quickSort
+++++++++++
Randomized quicksort
Time - Average NlogN, Worst Case N^2
Space - Lg(N)

Counting Sort
++++++++++++++
n = len(nums)
0. Initialize output <-- [0 for xrange(n)]; c <-- [0 for xrange(k+1)]
1. count freq of element to c
2. prefix_sum for c (value then indicates which position that element should
occur in the final sorted array)
3. Loop through nums
    output[c[nums[i]] - 1] = nums[i]
    c[nums[i]] -= 1
Time - O(N)
Space - O(N)

Two Pointer Sort
++++++++++++++++
take advantage of there are only 0, 1 , 2. In the sorted array, it will always
be 0....0,1....1,2....2
So maintain left <-- that is just pass region of 0s
and right <-- that is just pass region of 1s

Initialize i = 0; left =0 ; right = len(nums) - 1
While i <= right (= because we care about the boundary element)

    0......0,  1......1,  x1 x2 .... xm,  2.....2
               |          |          |
              left        i         right

    (a) when nums[i] == 1:
        nums[i] is at the right position, go deal with next element

        i += 1
    (b) when nums[i] == 0:
        need to put current element to the left boundary, since the left boundary
        element is always 1, we know after swap, the new element at i will be at
        the right position So
        Swap, then update the left boundary and continue to deal with the next element

        swap(nums,left,i)
        left += 1
        i += 1
    (c) When nums[i] == 2
        Need to put current element to the right boundary. We donot know what
        element is at right boundary. After swap, we need to deal with the element
        that is then at i So
        Swap, then update right boundary and stay at i to deal with the swapped
        element

        Swap(nums,right,i)
        right -=1

Time - O(N)
Space - O(1)
"""

# QuickSort
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors(self, nums):
        self.quickSort(nums)

    def quickSort(self, alist):
        self.quickSortHelper(alist, 0, len(alist) - 1)

    def quickSortHelper(self, alist, first, last):
        if first <= last:

            splitpoint = self.partition(alist, first, last)

            self.quickSortHelper(alist, first, splitpoint - 1)
            self.quickSortHelper(alist, splitpoint + 1, last)

    def quick_swap(self, alist, index_a, index_b):
        temp = alist[index_a]
        alist[index_a] = alist[index_b]
        alist[index_b] = temp

    def partition(self, alist, first, last):
        from random import randint
        pivot = randint(first, last)
        self.quick_swap(alist, first, pivot)

        pivotvalue = alist[first]
        leftmark = first + 1
        rightmark = last
        while leftmark <= rightmark:

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if leftmark <= rightmark:
                self.quick_swap(alist, leftmark, rightmark)
        self.quick_swap(alist, first, rightmark)

        return rightmark

# Counting Sort
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors(self, nums):
        n = len(nums)
        k = 3
        output = [0 for _ in xrange(n)]
        c = [0 for _ in xrange(k + 1)]
        for v in nums:
            c[v] += 1
        for i in xrange(1, k + 1):
            c[i] = c[i] + c[i - 1]
        for i in xrange(n):
            output[c[nums[i]] - 1] = nums[i]
            c[nums[i]] -= 1
        for i in xrange(n):
            nums[i] = output[i]


# Two Pointer Sort
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):
        # write your code here
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                self.swap(nums, i, left)
                left += 1
                i += 1
            elif nums[i] == 2:
                self.swap(nums, i, right)
                right -= 1
            else:
                i += 1

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
