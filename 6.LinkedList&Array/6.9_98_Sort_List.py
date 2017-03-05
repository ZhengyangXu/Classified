"""
Description
___________
Sort a linked list in O(n log n) time using constant space complexity.
Example
__________
Given 1->3->2->null, sort it to 1->2->3->null.

Approach
___________
Lined List version of inplace merge sort

The code is rather clear

Complexity
____________
Time- O(Nlg(n))
Space- O(1)
"""
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
# """


# MergeSort
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """

    def sortList(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        one = head
        two = head

        while two.next and two.next.next:
            one = one.next
            two = two.next.next
        mid = one.next
        one.next = None

        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        dummy = ListNode(0)
        tail = dummy
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1 is not None:
            tail.next = head1
        else:
            tail.next = head2
        return dummy.next
