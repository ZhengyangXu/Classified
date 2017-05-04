"""
Description
_____________
Given a positive integer,
return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""


class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""

        while n:
            lsb = n % 26
            if lsb:
                # print result, chr((lsb - 1) + ord('A'))
                result = chr((lsb - 1) + ord('A')) + result
                n = n / 26
            else:
                result = "Z" + result
                n = n / 26 - 1
        return result
