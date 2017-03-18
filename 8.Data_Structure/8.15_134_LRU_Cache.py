"""
Description
_____________
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key
if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity
it should invalidate the least recently used item before inserting a new item.

Approach
_____________
we want to have random access any element at O(1)  (GET)
we also want to know the least recent used element

ListNode + HashTable

Node
- key
- value
- child
- parent

Map
- key -> key
- value -> corresponding node

at LRU class Maintain

0. head -- head ot the linkedlist
1. tail -- tail of the the linkedlist (this is the LRU element)
2. map  -- hashtalbe
3. capacity -- capacity of the LRU

Now GET and SET will depent upon the remove, and sethead action

def remove(node) - remove the node specified, take care of situation it's head
    or tail and update head and tail (Note edge cases)
=============================================

    Maintain child link -->
    Maintain parent link <--

    a.  -->
       (1) if node.parent exsits, set node.parent.child = node.child
           to skip node
       (2) else, it means node is the head of LRU
           self.head = node.child to skip the head

    b. <--
      (1) if node.child exists, set node.child.parent = node.parent to skip node
      (2) else it means it's the tail
          self.tail = node.parent

      '''
        def remove(self, node):
            if node.parent:
                node.parent.child = node.child
            else:
                self.head = node.child
            if node.child:
                node.child.parent = node.parent
            else:
                self.tail = node.parent
     '''

def sethead(node) - set the node that DOES NOT EXIST in current linkedlist to head
update head and tail accordingly (Notice edge cases)
=========================================
    a. set node's child to current head
    b. if head exist, set head's parent to node
       then set current head to node

    c. if current tail is None
       set current tail to head

        ''''
        def sethead(self, node):
            node.child = self.head
            node.parent = None
            if self.head is not None:
                self.head.parent = node
            self.head = node
            if self.tail is None:
                self.tail = self.head

       ''''


Now for Get
=============
if the key does not exist, just return -1
if it exsits, we need to
0. returen the value
1. move the corresponding node to the head
   a. remove
   b. sethead

'''
def get(self, key):
    # write your code here
    # print self.map
    if key in self.map:
        node = self.map.get(key)
        self.remove(node)
        self.sethead(node)
        # print "afterget", self.head.key, self.tail.key
        return node.value
    return -1
'''

For SET
==============
1. if it the key exists
   (a). get the node (via map)
   (b). update the node
   (c) remove + sethead to move it to the head of the list

2. if it does not
   new_node = Node(key,value)
   (a) if it exceeds the capacity
       (1) remove the LRU from both map and linkedlist
       (2) sethead(new_node)
       (3) map[key] = new_node
   (b) else
       (1) sethead(new_node)
       (2) map[key] = new_node

    def set(self, key, value):
        # write your code here
        if key in self.map:
            old_node = self.map.get(key)
            old_node.value = value
            self.remove(old_node)
            self.sethead(old_node)
        else:
            new_node = Node(key, value)
            if len(self.map) >= self.capacity:

                self.map.pop(self.tail.key)
                self.remove(self.tail)
                self.sethead(new_node)
            else:
                self.sethead(new_node)
            self.map[key] = new_node

"""


class Node:

    def __init__(self, key, value, parent=None, child=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.child = child


class LRUCache:

    # @param capacity, an integer

    def __init__(self, capacity):
        # write your code here
        self.capacity = capacity
        self.map = {}
        self.head = None
        self.tail = None

    def remove(self, node):
        if node.parent:
            node.parent.child = node.child
        else:
            self.head = node.child
        if node.child:
            node.child.parent = node.parent
        else:
            self.tail = node.parent

    def sethead(self, node):
        # @return an integer
        node.child = self.head
        node.parent = None
        if self.head is not None:
            self.head.parent = node
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def get(self, key):
        # write your code here
        # print self.map
        if key in self.map:
            node = self.map.get(key)
            self.remove(node)
            self.sethead(node)
            # print "afterget", self.head.key, self.tail.key
            return node.value
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        if key in self.map:
            old_node = self.map.get(key)
            old_node.value = value
            self.remove(old_node)
            self.sethead(old_node)
        else:
            new_node = Node(key, value)
            if len(self.map) >= self.capacity:

                self.map.pop(self.tail.key)
                self.remove(self.tail)
                self.sethead(new_node)
            else:
                self.sethead(new_node)
            self.map[key] = new_node
