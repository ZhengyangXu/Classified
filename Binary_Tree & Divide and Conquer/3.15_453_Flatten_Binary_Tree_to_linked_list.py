"""

Description
___________
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

 Notice

Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.

Have you met this question in a real interview? Yes
Example
              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6


Approach
_______________
The following approach is relied on
            right_start = root.right
            root.right = root.left
            left_tail.right = right_start
            root.left = None
to connect the three pieces

another approach with extra O(N) space is to visit it pre_order and
build linked_list
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing

    def flatten(self, root):
        # write your code here
        self.helper(root)

    def helper(self, root):
        # return the tail of the flattned list
        if root == None:
            return
        left_tail = self.helper(root.left)
        right_tail = self.helper(root.right)
        if left_tail:
            right_start = root.right
            root.right = root.left
            left_tail.right = right_start
            root.left = None

        if right_tail:
            return right_tail
        if left_tail:
            return left_tail
        return root
