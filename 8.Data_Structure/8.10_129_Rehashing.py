"""
Description
____________
The size of the hash table is not determinate at the very beginning.
If the total size of keys is too large (e.g. size >= capacity / 10)
 we should double the size of the hash table and rehash every keys.
 Say you have a hash table looks like below:


 size=3, capacity=4

[null, 21, 14, null]
       ↓    ↓
       9   null
       ↓
      null

The hash function is:

int hashcode(int key, int capacity) {
    return key % capacity;
}

here we have three numbers, 9, 14 and 21, where 21 and 9
share the same position as they all have the same hashcode 1 (21 % 4 = 9 % 4 = 1).
We store them in the hash table by linked list.

rehashing this hash table, double the capacity, you will get:

size=3, capacity=8

index:   0    1    2    3     4    5    6   7
hash : [null, 9, null, null, null, 21, 14, null]

Approach
_________
dummy dummy
++++++++++++++
0. Have two arrays result, newTable initialized with dummy nodes
Point result's dummy nodes to newTable's dummynodes
1. use newTable to 穿针引线
2. iterate all result's dummy to .next.next
3. return result


0. Init resultTable, newTable
    resultTable = [ListNode(-1) for _ in xrange(n)]
    newTable = [ListNode(0) for _ in xrange(n)]
1.  Point dummynodes in resultTable to newTable
    for i in xrange(n):
        resultTable[i].next = newTable[i]
2. Loop through old table
   a. get the cur
      while cur is not None
      (1). recalculate the hashcode according to cur.val
      (2). create a new node and place it to corresponding position at newTable
      (3) cur = cur.next
      (4) newTalbe[new_pos] = newTable[new_pos].next

     for i in hashTable:
            cur = i
            while cur:
                new_code = cur.val%n
                new_node = ListNode(cur.val)
                cur = cur.next

                newTable[new_code].next = new_node
                newTable[new_code] = newTable[new_code].next


Complexity
_____________
Time - O(N)
Space - O(N)
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
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """

    def rehashing(self, hashTable):
        # write your code here
        n = len(hashTable) * 2

        resultTable = [ListNode(-1) for _ in xrange(n)]
        newTable = [ListNode(0) for _ in xrange(n)]
        for i in xrange(n):
            resultTable[i].next = newTable[i]

        for i in hashTable:
            cur = i
            while cur:
                new_code = cur.val % n
                new_node = ListNode(cur.val)
                cur = cur.next

                newTable[new_code].next = new_node
                newTable[new_code] = newTable[new_code].next
        for i in xrange(len(resultTable)):
            resultTable[i] = resultTable[i].next.next
        return resultTable
