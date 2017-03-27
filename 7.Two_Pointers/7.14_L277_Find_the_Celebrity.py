"""
Description
_____________
Suppose you are at a party with n people (labeled from 0 to n - 1)
and among them, there may exist one celebrity.
The definition of a celebrity is that
 - all the other n - 1 people know him/her but he/she does not know any of them.
Now you want to find out who the celebrity is or verify that there is not one.
The only thing you are allowed to do is to ask questions like:
Hi, A. Do you know B?" to get information of whether A knows B.
You need to find out the celebrity (or verify there is not one) by asking as
few questions as possible (in the asymptotic sense).
You are given a helper function bool knows(a, b)
which tells you whether A knows B. Implement a function int findCelebrity(n)
your function should minimize the number of calls to knows.
Note: There will be exactly one celebrity if he/she is in the party.
Return the celebrity's label if there is a celebrity in the party.
If there is no celebrity, return -1.

Approach
_____________
Two_pointers
+++++++++++++
The naive approach obviously results in a N^2 method
the key insight here is that imagine A, B
if knows(A,B):
    A cannot be the celebrity
else:
    B cannot be the celebrity

So each ask can help us at least rule out one non-celebrity. Now we can use
two pointers
    left, right = 0 , n-1

    use left, right because we want to examine each pair
    while left < right:
        if knows(left, right):
            left += 1
        else:
            right -= 1

    In the end, if exists, left will be the celebrity exist
    a for loop to check whether left is the celebrity index

    for i in xrange(n):
        if i != left and (knows(left, i) or not knows(i, left)):
            return -1

Complexity
_______________
Time - O(N)
Space - O(1)
"""


class Solution(object):

    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n - 1
        while left < right:
            if knows(left, right):
                left += 1
            else:
                right -= 1
        for i in xrange(n):
            if i != left and (knows(left, i) or not knows(i, left)):
                return -1
        return left
