"""
Write a program to find the node at which the intersection of two singly linked
lists begins.
For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
 
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nA = 0
        nB = 0
        curA = headA
        curB = headB
        while curA:
            nA += 1
            curA = curA.next
        while curB:
            nB += 1
            curB = curB.next
        diff = abs(nA - nB)
        if nA > nB:
            earlybird = headA
            smartbird = headB
        else:
            earlybird = headB
            smartbird = headA
        print diff
        while diff:
            earlybird = earlybird.next
            diff -= 1
        if earlybird:
            print earlybird.val, smartbird.val
        while earlybird:
            if earlybird is smartbird:
                return earlybird
            earlybird = earlybird.next
            smartbird = smartbird.next
