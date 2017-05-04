"""
Description
________________
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for better
legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number
of rows: string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
 
Approach
__________________
If we can have a matrix representation of whole it zigzaged, it can be solved
so we want to get hold of
result = ["" for _ in xrange(rows)]
"" will becomes row string
then just do a join


Now the only part left is just to put each char into the right row_string
USE THE GUIDER

    guider = range(numRows) + range(numRows - 2, 0, -1)
    Imagine row = 3
    guider = [0,1,2,1]

    index = i%len(guider) that's which row the current i should be in

Complexity
______________
Time - O(N)
Space - O(N)
"""


class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        guider = range(numRows) + range(numRows - 2, 0, -1)
        # print guider
        finder = ["" for _ in xrange(numRows)]
        for i in xrange(len(s)):
            finder[guider[i % len(guider)]] += s[i]
        # print finder
        return ''.join(finder)
