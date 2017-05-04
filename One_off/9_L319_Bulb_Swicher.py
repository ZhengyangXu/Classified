"""
There are n bulbs that are initially off. You first turn on all the bulbs. Then
you turn off every second bulb. On the third round, you toggle every third bulb
(turning on if it's off or turning off if it's on). For the ith round
you toggle every i bulb. For the nth round, you only toggle the last bulb
Find how many bulbs are on after n rounds.


Given n = 3.

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.



Let R = int(sqrt(n)). That's the root of the largest square in the range [1,n]
. And 1 is the smallest root. So you have the roots from 1 to R, that's R roots
 Which correspond to the R squares. So int(sqrt(n)) is the answer
 (C++ does the conversion to int automatically, because of the specified return type).
"""
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # see why in the first solution
        from math import sqrt
        return int(sqrt(n))
