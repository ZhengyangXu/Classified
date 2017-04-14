"""
Description
___________
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Approach
_____________
When smaller appear before larger, means it's minus

Complexity
___________
Time - O(N)
Space - O(1)
"""

class Solution(object):

    def romanToInt(self, s):
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]
