"""
Description
____________
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.


Approach
___________
stack
+++++
maintain
start - start of most recent longest valid consecutive matched parentheses (inclusive)
maxLen - maximum length of valid consecutive matched parentheses
Loop through the string
1. when see '(', append the INDEX to the stack
2. when see ')'
    a. if len(stack) == 0, this means no match, we can skip this one by start = i + 1
    b. else: pop one off the stack. after that
        if len(stack) == 0, it means we have finished a set of match
            maxlen = max(maxlen, i - start + 1)
        else:
            maxlen = max(maxlen, i - stack[-1]) ( since poped one off, the top is one before the match)
return maxlen
"""
 

class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxlen = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    # has to do this instaed tof start = i becasue
                    # the LVP might start at 0
                    start = i + 1
                else:
                    stack.pop()
                    if len(stack) == 0:
                        maxlen = max(maxlen, i - start + 1)
                    else:
                        maxlen = max(maxlen, i - stack[-1])
        return maxlen
