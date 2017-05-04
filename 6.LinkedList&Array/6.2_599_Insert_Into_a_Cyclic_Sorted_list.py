"""
Description
_________________
Given a node from a cyclic linked list which has been sorted,
write a function to insert a value into the list such that it remains a cyclic sorted list.
The given node can be any single node in the list.
Return the inserted new node.

Example
________________
Given a list, and insert a value 4:
3->5->1
Return 5->1->3->4

Approach
________________
This is a simple problem but by no means trivial
to consider corner cases

Insert x into the list
There are three cases
1. x is in between prev, cur(two consective values in current list)
2. x is the extrema
3. It's neither 1,2 (did not find break and we looped back),duplicated list
(1->1->1)

We gracefully handle it by using prev, cur and loop through as following

Complexity
_______________
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
    # @param {ListNode} node a list node in the list
    # @param {int} x an integer
    # @return {ListNode} the inserted new list node

    def insert(self, node, x):
        # Write your code here

        if node is None:
            a = ListNode(x)
            a.next = a
            return a

        prev = None
        cur = node
        while True:
            prev = cur
            cur = cur.next
            # Case 1
            if x >= prev.val and x <= cur.val:
                break
            # Case 2
            # We detected the "end" of the list and check whether x
            # is the extrema
            # if not we have continue the looping to allow case 1 to be caught
            if prev.val > cur.val and (x > prev.val or x < cur.val):
                break
            # case 3
            if cur is node:
                break
        a = ListNode(x)
        prev.next = a
        a.next = cur

        return node
