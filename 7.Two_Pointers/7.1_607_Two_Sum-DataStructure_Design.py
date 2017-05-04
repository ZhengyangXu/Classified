"""
Description
___________
Design and implement a TwoSum class.
It should support the following operations: add and find.
add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
 
Example
_________
add(1); add(3); add(5);
find(4) // return true
find(7) // return false
"""


class TwoSum(object):

    def __init__(self):
        # initialize your data structure here
        self.nums = []

    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing
    def add(self, number):
        # Write your code here
        self.nums.append(number)

    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        # Write your code here
        s = set([])
        for i in self.nums:
            target = value - i
            if target in s:
                return True
            s.add(i)
        return False
