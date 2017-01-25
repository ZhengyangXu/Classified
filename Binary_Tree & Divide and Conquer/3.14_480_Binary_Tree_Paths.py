"""
Description
___________
Given a binary tree, return all root-to-leaf paths.

Example
____________
Given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

[
  "1->2->5",
  "1->3"
]


Approach/Complexity
___________________
Exactly same as last one

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
        self.dfs(root, path, result, 0, target)
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
