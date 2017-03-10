"""
Description
___________
Find K-th largest element in an array.

Example
__________
In array [9,3,2,4,8], the 3rd largest element is 4.
In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4
3rd largest element is 3 and etc.

Approach
__________
Reversed QuickSelect
+++++++++++++++++++++
We are essentially quickselecting from behind

When D & Q do this
if k == len(alist) - split:
    return alist[split]
elif len(alist) - split < k:
    return self.quickselecthelper(alist, start, split - 1, k)
else:
    return self.quickselecthelper(alist, split + 1, end, k)

Complexity
___________
Time - AVG O(N). WrostCase O(N^2)
Sapce - O(1)
"""

class Solution:
    # @param k & A a integer and an array
    # @return ans a integer

    def kthLargestElement(self, k, A):
        return self.quickselect(A, k)

    def quickselect(self, alist, k):
        start, end = 0, len(alist) - 1
        return self.quickselecthelper(alist, start, end, k)

    def quickselecthelper(self, alist, start, end, k):
        if start <= end:

            split = self.random_partition(alist, start, end)
            # print start,end, split
            if k == len(alist) - split:
                return alist[split]
            elif len(alist) - split < k:
                return self.quickselecthelper(alist, start, split - 1, k)
            else:
                return self.quickselecthelper(alist, split + 1, end, k)

    def random_partition(self, alist, start, end):
        from random import randint
        pivot = randint(start, end)
        temp = alist[start]
        alist[start] = alist[pivot]
        alist[pivot] = temp

        leftmark = start + 1
        rightmark = end
        pivotvalue = alist[start]

        while leftmark <= rightmark:
            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark += 1
            while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
                rightmark -= 1
            if leftmark <= rightmark:
                self.swap(alist, leftmark, rightmark)

        self.swap(alist, start, rightmark)
        return rightmark

    def swap(self, alist, a, b):
        temp = alist[a]
        alist[a] = alist[b]
        alist[b] = temp
