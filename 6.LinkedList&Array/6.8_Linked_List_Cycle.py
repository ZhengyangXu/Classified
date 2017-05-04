"""
Description
____________
Given a linked list, determine if it has a cycle in it.

Example
____________
Given -21->10->4->5, tail connects to node index 1, return true
 
Approach
____________
0. run a 2-step pointer
1. run a 1-step pointer
2. if they meet, True ,else False

Be careful how we took care of the edge cases here
while two.next and two.next.next to enforce 2-step pointer
and
check null at the begining

Complexity
___________
Time - O(N)
Space - O(1)
"""


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """

    def hasCycle(self, head):
        # write your code here
        if head is None:
            return False
        one = head
        two = head
        while two.next and two.next.next:
            one = one.next
            two = two.next.next
            if one is two:
                return True
        return False
