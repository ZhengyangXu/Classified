"""
Description
____________
Reverse a singly linked list.

Approach
____________
This is the same as the second part of the add_Two_numbers_II

See the code

Complexity
_____________
Time - O(N)
Space - O(1)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

 
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev
