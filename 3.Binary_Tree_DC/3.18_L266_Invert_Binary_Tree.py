"""
Description
_____________
invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Approach
________________
easy DQ

complexity
_______________
Time - O(H)
SPace - O(H)
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root
