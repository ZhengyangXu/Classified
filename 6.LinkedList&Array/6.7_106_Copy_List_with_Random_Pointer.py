"""
Description
____________
A linked list is given such that each node contains an
additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.

Approach 
____________
original_list
new_list
dic ---> k-original_node v-new_node

0.loop through original_list and create dic[originnode] = newnode
(Use Dummy node approach)
1. loop through the dic to assign the correct new_random to new_node
dic[k].random = dic[k.random]

Complexity
_____________
Time - O(N)
Space - O(N)
"""
# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode

    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return
        dummy = RandomListNode(None)
        dic = {}
        start = head
        new_start = dummy
        while start:
            new = RandomListNode(start.label)
            dic[start] = new
            new_start.next = new
            new_start = new_start.next
            start = start.next

        for k in dic:
            if k.random:
                dic[k].random = dic[k.random]
        return dummy.next
