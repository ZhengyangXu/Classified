"""
Description
_____________
Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

Example
_____________
Given -21->10->4->5, tail connects to node index 1，return 10
  
Approach
_____________
procedure
++++++++++++++
The procedure is simple.
fast - 2x pointer
slow - 1x pointer
0. move fast and slow until they meet
1. move slow back to the begining
2. fast and slow all MOVE AT ONE STEP SPEED
3. When they meet, return the node, that's the begining


Proof
++++++++++++++

step 0 - 1
========================
Let flat list's length is m
let cycle part length is n

Let's say they meet at k away from starting point of the cycle
i as the steps of slow
(1) i = m + p*n + k
(2) 2i = m + q*n + k

==> 2(m + p*n + k) = m + q*n + k
==> m + k = (q-2p) n

============================
Step 2-3

after they first meet, we move slow back to the begining. fast will be at point
x where it is k away from the begining of the cylce

Given m + k = (q-2p) n
so when we move the slow (that is currently at the begining) m steps
0. slow will arrive at the begining of the cycle
1. fast will be k short of completing (q-2p) rotations if it also starts at
the begining. Howver, it was k ahead
2. so they will meet at the begininig of the cycle




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
    @return: The node where the cycle begins.
                if there is no cycle, return null
    """

    def detectCycle(self, head):
        # write your code here
        one = head
        two = head
        while two:
            one = one.next
            two = two.next
            if two:
                two = two.next
            if one is two and (one is not None):
                break

        if two is None:
            return

        one = head

        while True:
            one = one.next
            two = two.next
            if one is two:
                return one
