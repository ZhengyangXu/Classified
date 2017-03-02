"""
Start end  anywhere
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

    def binaryTreePathSum2(self, root, target):
        # Write your code here
        result, path = [], []
        self.traverse(root, path, result, 0, target)
        return result

    def traverse(self, node, path, result, level, target):
        if node is None:
            return
        path += [node.val]
        tmp = target
        for i in xrange(level, -1, -1):
            tmp -= path[i]
            if tmp == 0:
                result.append(path[i:])
        self.traverse(node.left, path, result, level + 1, target)
        self.traverse(node.right, path, result, level + 1, target)

        path.pop()
