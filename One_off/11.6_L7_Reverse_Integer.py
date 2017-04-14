"""
Description
______________
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Complexity
_______________
Time - O(N)
"""


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x is None:
            return
        mask = 0x7FFFFFFF
        if x < 0:
            sign = (-1)
            s = str((-1) * x)
        else:
            sign = 1
            s = str(x)
        left, right = 0, len(s) - 1
        l = self.getList(s)
        while left < right:
            self.swap(l, left, right)
            left += 1
            right -= 1
        s = ''.join(l)
        return sign * int(s) if int(s) <= mask else 0

    def getList(self, s):
        result = []
        for i in s:
            result.append(i)
        return result

    def swap(self, s, i, j):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp


# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         digits = []


#         if x==0:
#             return 0

#         remains = abs(x)
#         sign = -1 if x < 0 else 1

#         while(True):
#             # remains is not zero
#             digit = remains % 10
#             remains = remains / 10
#             digits.append(digit)
#             if remains == 0:
#                 break

#         ret = 0
#         for i in digits:
#             ret *= 10
#             ret += i

#         ret *= sign
#         if abs(ret) > 0x7FFFFFFF:
#             return 0
#         else:
#             return ret
