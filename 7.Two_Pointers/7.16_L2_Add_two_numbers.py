"""
Description
___________
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number
0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Approach
_____________
Maintain two pointers, start from the begining since reversed
Utilize the classical dummy node
so Initialize
dummy = ListNode(-1)
   cur = dummy
then use cur to 穿针引线 while still have dummynode whose next is the new head
in each iteration
    do cur.next = new
       cur = new
in the end, return dummy.next

Complexity
_____________
Time - O(N)
Space - O(N)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

 
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummyNode = ListNode(-1)
        cur = dummyNode
        while l1 or l2 or carry:
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            s += carry
            carry = s / 10
            cur.next = ListNode(s % 10)
            cur = cur.next
        return dummyNode.next
