
"""
Given an expression s includes numbers, letters and brackets. Number represents the number of repetitions inside the brackets(can be a string or another expression)．Please expand expression to be a string.

Have you met this question in a real interview? Yes
Example
s = abc3[a] return abcaaa
s = 3[abc] return abcabcabc
s = 4[ac]dy, return acacacacdy
s = 3[2[ad]3[pf]]xyz, return adadpfpfpfadadpfpfpfadadpfpfpfxyz
"""

# version 2


class Solution:
    # @param {string} s  an expression includes numbers, letters and brackets
    # @return {string} a string

    def expressionExpand(self, s):
        # Write your code here
        if '[' not in s:
            return s

        if not s[0].isdigit():
            index = 0
            while not s[index].isdigit():
                index += 1

            left_str = s[0: index]
            right_str = s[index:]
            times = 1
        else:
            left = s.find('[')
            times = int(s[0: left])
            pair = 0
            for index in xrange(left, len(s)):
                if s[index] == '[':
                    pair += 1
                elif s[index] == ']':
                    pair -= 1
                if pair == 0:
                    right = index
                    break

            left_str = s[left + 1: right]
            right_str = s[right + 1:]

        return self.expressionExpand(left_str) * times + \
            self.expressionExpand(right_str)
