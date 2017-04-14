"""
Description
_____________
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

Complexity
_____________
Time - O(1)
Space - O(1)
"""


class Solution(object):

    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""
        for i, v in enumerate(values):
            res += (num / v) * numerals[i]
            num %= v
        return res
