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
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths

    def binaryTreePaths(self, root):
        # Write your code here
        result = []
        path = []
        self.dfs(root, path, result) 
        return ['->'.join([str(i)for i in path]) for path in result]

    def dfs(self, node, path, result):
        if node == None:
            return

        path = path + [node.val]

        if node.left is None and node.right is None:
            result.append(path[:])

        self.dfs(node.left, path, result)
        self.dfs(node.right, path, result)

        path.pop()
