"""
Description
===========
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example
==========
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        if root ==None:
            return []
        q = []
        q.insert(0, root)
        result = []
        while len(q) > 0:
            size = len(q)
            level = []
            while size > 0:
                node = q.pop()
                level.append(node.val)
                if node.left:
                    q.insert(0,node.left)
                if node.right:
                    q.insert(0,node.right)
                size -= 1

            result.append(level)

        return result
