
"""
Given an expression s includes numbers, letters and brackets. Number represents the number of repetitions inside the brackets(can be a string or another expression)．Please expand expression to be a string.

Have you met this question in a real interview? Yes
Example
s = abc3[a] return abcaaa
s = 3[abc] return abcabcabc
s = 4[ac]dy, return acacacacdy
s = 3[2[ad]3[pf]]xyz, return adadpfpfpfadadpfpfpfadadpfpfpfxyz
"""

# version 1 -- Recursion


class Solution:
    # @param {string} s  an expression includes numbers, letters and brackets
    # @return {string} a string

    def expressionExpand(self, s):
        # Write your code here
        if s is None or not s:
            return ""
        if '[' not in s:
            return s
        if s[0].isdigit():
            left = s.find('[')
            pair = 0
            times = int(s[:left])
            for right in xrange(left, len(s)):
                if s[right] == '[':
                    pair += 1
                if s[right] == ']':
                    pair -= 1
                if pair == 0:
                    break

            leftstring = s[left + 1:right]
            rightstring = s[right + 1:]
        else:
            times = 1
            for right in xrange(len(s)):
                if s[right].isdigit():
                    break
            leftstring = s[:right]
            rightstring = s[right:]
        return self.expressionExpand(leftstring) * times + self.expressionExpand(rightstring)

# Version 2 -- Stack


class Solution:
    # @param {string} s  an expression includes numbers, letters and brackets
    # @return {string} a string

    def expressionExpand(self, s):
        from collections import deque
        stack = deque()
        number = 0
        for char in s:
            if char.isdigit():
                number = int(char) + number * 10
            elif char == '[':
                stack.append(number)
                number = 0
            elif char == ']':
                s = []
                while stack:
                    cur = stack.pop()
                    if type(cur) == int:
                        stack.append(''.join(reversed(s)) * cur)
                        break
                    s.append(cur)
            else:
                stack.append(char)

        return ''.join(stack)
