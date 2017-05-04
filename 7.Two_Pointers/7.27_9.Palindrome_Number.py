"""
Determine whether an integer is a palindrome.
Do this without extra space.
"""

class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        msn = 1
        while msn * 10 < x:
            msn *= 10
        cur_l = x
        cur_r = x
        while msn:
            if cur_l / msn != cur_r % 10:
                return False
            cur_l = cur_l % msn
            cur_r = cur_r / 10
            msn /= 10
        return True
 
