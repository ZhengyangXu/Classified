"""
Description
___________
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example
___________
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

Approach
___________
BFS
+++++
Bread-frist-search through the tree
force the level-wise pop each iteration

Complexity
___________
L -- number of leaf nodes
Time - O(N)
Space - O(L)
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
        if root is None:
            return []
        from collections import deque
        q, result = deque(), []
        q.append(root)
        while q:
            level = []
            size = len(q)
            for i in xrange(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result
