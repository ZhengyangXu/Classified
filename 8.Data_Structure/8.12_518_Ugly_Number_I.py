"""
Description
_____________
Write a program to check whether a given number is an ugly number
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 6, 8 are ugly
while 14 is not ugly since it includes another prime factor 7.

Example
——————————————
Given num = 8 return true
Given num = 14 return false

Approach
___________
Recursion
+++++++++
CHeck Base - [2,3,5] (not including 1 since 1 will divide anything and not incur subproblem)

Base Cases -  0 -> False; 1-> True
 
Recursion
        for i in bases:
            if num % i == 0:
                result = num / i
                break
        if result is None:
            return False
        else:
            return self.isUgly(result)


complexity
__________
Time - O(lg(N))
Space - O(Lg(N))

"""


class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false

    def isUgly(self, num):
        # Write your code here
        bases = [2, 3, 5]
        if num is None or num == 0:
            return False
        if num in bases or num == 1:
            return True
        result = None
        for i in bases:
            if num % i == 0:
                result = num / i
                break
        if result is None:
            return False
        else:
            return self.isUgly(result)
