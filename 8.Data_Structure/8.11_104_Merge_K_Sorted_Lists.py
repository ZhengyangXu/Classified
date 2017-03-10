"""
Description
___________

Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Example
____________
Given lists:

[
  2->4->null,
  null,
  -1->null
],

Approach
+++++++++
0. Initialize a dummy node and a minheap
    dummy = ListNode(0)
    head = dummy
    minheap = []
1. put all heads in the list to the minheap
2. while heap's length is longer than 1
    a. pop the min node and connect it to head. THen iterate the head
    cur = heap.pop()
    head.next = cur_node
    head = head.next
    b. get the next_node of the poped off node
    next_node = cur_node.next
        (a) if it's not empty, put it back to the heap
            if next_node:
                heapq.heappush(minheap,T(next_node))

3. now heap has only one node left, connect it to head
    if minheap:
        last = heapq.heappop(minheap).node
        head.next = last

4. return dummy.next


complexity
__________
Time - O(Nlg(k))
Space - O(Ki)
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class T:

    def __init__(self, node):
        self.node = node

    def __cmp__(self, other):
        return self.node.val - other.node.val


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
        if lists is None or len(lists) == 0:
            return
        dummy = ListNode(0)
        head = dummy
        minheap = []
        import heapq
        for i in lists:
            if i is not None:
                heapq.heappush(minheap, T(i))
        while len(minheap) > 1:
            cur_node = heapq.heappop(minheap).node
            # print cur_node.val
            head.next = cur_node
            head = head.next
            next_node = cur_node.next
            if next_node:
                heapq.heappush(minheap, T(next_node))
        if minheap:
            last = heapq.heappop(minheap).node
            head.next = last
        return dummy.next
