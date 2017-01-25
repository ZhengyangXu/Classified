"""
Description
_____________
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes.

Have you met this question in a real interview? Yes

Example
_____________
Given a binary tree, and target = 5:

     1
    / \
   2   4
  / \
 2   3
return

[
  [1, 2, 2],
  [1, 4]
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
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths

    def binaryTreePathSum(self, root, target):
        # Write your code here
        result = []
        path = []
        self.dfs(root, path, result, 0,  target)
        return result

    def dfs(self, root, path, result, cur, target):
        if root is None:
            return
        cur += root.val
        path += [root.val]
        if cur == target and root.left is None and root.right is None:
            result.append(path[:])

        self.dfs(root.left, path, result, cur, target)
        self.dfs(root.right, path, result, cur, target)
        path.pop()
        cur -= root.val
