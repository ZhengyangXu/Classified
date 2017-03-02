"""
Description
___________
Merge two sorted (ascending) linked lists and return it as a new sorted list.
The new sorted list should be made by splicing together
the nodes of the two lists and sorted in ascending order.

Example
____________
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.

Approach
_____________
穿针引线
"""


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1 != None:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next
