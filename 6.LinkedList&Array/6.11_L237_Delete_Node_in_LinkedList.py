"""
Description
_______________
Write a function to delete a node (except the tail) in a singly linked list
given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value
the linked list should become 1 -> 2 -> 4 after calling your function.

Approach
_______________
Make the target node the next node (change value)
Then skip the next one

Complexity
_______________
Time - O(1)
Space - O(1)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

 
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
