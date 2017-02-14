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
        path, result, cur = [], [], 0
        self.traverse(root,path,cur,target,result)
        return result


    def traverse(self, node, path, cur, target, result):
        if node is None:
            return
        cur += node.val
        path += [node.val]

        if cur == target and node.left is None and node.right is None:
            result.append(path[:])

        self.traverse(node.left, path, cur, target, result)
        self.traverse(node.right, path, cur, target, result)

        path.pop()
        cur -= node.val
    
