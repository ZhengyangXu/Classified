"""
Description
_______________
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Approach
___________
Code says it all

Complexity
___________
Time - O(N)
Space - O(1)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 

class Solution(object):

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        if head.next is None or head.next.next is None:
            return head
        dummy1 = ListNode(-1)
        cur1 = dummy1
        dummy2 = ListNode(-1)
        cur2 = dummy2
        while head:
            cur1.next = head
            cur2.next = head.next
            cur1 = cur1.next
            cur2 = cur2.next

            head = head.next.next if head.next else None

        cur1.next = dummy2.next
        return dummy1.next
