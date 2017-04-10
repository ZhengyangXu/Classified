"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

Approach
______________
Two Pointers
+++++++++++++++
Start from the end
while index1 >=0 or index2 >=0 or carry:
    maintain
        new_node = cur1 + cur2 + carry %2
        carry = carry + cur1 + cur2 /2


Complexity
_______________
Time - O(N)
Space - O(N)
"""
# class Solution(object):
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         return self.tento2(self.twoto10(a) + self.twoto10(b))

#     def twoto10(self,n):
#         base = 1
#         s = 0
#         for i in xrange(len(n)-1,-1,-1):
#             s += int(n[i]) * base
#             base *= 2
#         return s
#     def tento2(self,n):
#         if n == 0:
#             return '0'
#         if n == 1:
#             return '1'
#         return self.tento2(n/2) + str(n%2)



class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        indexa = len(a) - 1
        indexb = len(b) - 1
        carry = 0
        sum = ""
        while indexa >= 0 or indexb >=0  or carry:
            x = int(a[indexa]) if indexa >= 0 else 0
            y = int(b[indexb]) if indexb >= 0 else 0
            if (x + y + carry) % 2 == 0:
                sum = '0' + sum
            else:
                sum = '1' + sum
            carry = (x + y + carry) / 2
            indexa, indexb = indexa - 1, indexb - 1
        return sum
