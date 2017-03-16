"""
Description
________________________
Given a big sorted array with positive integers sorted by ascending order.
The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++). Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.

Approach
_______________________
*2 to find the upper bound
then do a standard binary search

Compleixty
_____________
Time - O(Lg(N))
Space - O(1)
"""


"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
"""


"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
"""


class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer

    def searchBigSortedArray(self, reader, target):
        # write your code here
        start, end = 0, 0
        while target > reader.get(end):
            end = end * 2 + 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            mid_value = reader.get(mid)
            if mid_value == target:
                end = mid
            elif target < mid_value:
                end = mid
            else:
                start = mid

        if reader.get(start) == target:
            return start
        elif reader.get(end) == target:
            return end
        else:
            return -1
