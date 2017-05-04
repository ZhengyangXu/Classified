"""
Description
_____________
Given a string, find the length of the longest substring without repeating characters.
Examples
_____________
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
Approach
______________
two poitners + map
+++++++++=++++++++
maintain - i, j, max_length, map
1. use two pointers i, j starting at 0
2. move j forward
    a. if s[j] already in the map and ** dic[s[j]] is at further than i **
       i =  dic[s[j]] + 1
    b. else
       if j - i + 1> max_length:
           max_length = j - i + 1
    c. add map[s[j]] = j
3. return max_length

Complexity
______________
Time - O(N)
Space - O(N)
"""
 
class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 0
        max_length = 0
        dic = {}
        for j in xrange(len(s)):
            if s[j] in dic and dic[s[j]] >= i:
                i = dic[s[j]] + 1
            else:
                if j - i + 1 > max_length:
                    max_length = j - i + 1
            dic[s[j]] = j
        return max_length
