"""
Description
_______________

You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example
___________________
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

Approach
___________________
Now, since most significant bit comes first, use two stacks to reverse it
THen everything becomes identical except

intialize
cur = None
in each iteration
    new.next = cur
    cur = new
in the end,directly return cur
No need for dummy Node since we donot need to get a hold of it

Complexity
____________
Time - O(N)
Space - O(N)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = collections.deque()
        stack2 = collections.deque()

        while l1:
            stack1.append(l1)
            l1 = l1.next
        while l2:
            stack2.append(l2)
            l2 = l2.next
        cur = None
        carry = 0
        while stack1 or stack2 or carry:
            s = 0
            if stack1:
                s += stack1.pop().val
            if stack2:
                s += stack2.pop().val
            s += carry
            new_node = ListNode(s % 10)
            new_node.next = cur
            cur = new_node
            carry = s / 10

        return cur
