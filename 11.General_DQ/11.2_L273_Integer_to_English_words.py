"""
Description
______________
Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 231 - 1.
For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""


class Solution(object):

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        a = ["", "Thousand", "Million", "Billion"]
        result = self.helper(0, num, a)
        if result:
            return result.strip()
        else:
            return "Zero"

    def helper(self, passed, num,  a):
        # print "==>", num
        if num == 0:
            return ""

        b = num % 1000

        if b != 0 or num == 1:
            return self.helper(passed + 1, num / 1000,  a) + " " + self.convertHundred(b) + " " + a[passed]
        else:
            return self.helper(passed + 1, num / 1000,  a)

    def convertHundred(self, n):
        below20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                   "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        above20 = ["", "", "Twenty", "Thirty", "Forty",
                   "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        a = n / 100
        b = n % 100
        result = ""
        if b < 20:
            result += below20[b]
        else:
            result += above20[b / 10] + " " + below20[b % 10]
        if a > 0:
            result = below20[a] + " " + 'Hundred ' + result
        return result.strip()
