"""
Description
_____________
Start any anywhere


Approach
_____________
Recursive DQ+DFS+BACKTRACKING
++++++++++++++++++

parameter Maintain - node, path, result, target

Base - if None, return

adding condition -
when temp = target
reduced to zero in the for loop

When DFS to a specific node
    path += [node.val]
    tmp = target
    size = len(path) - 1
    # start from back to get
    # sum of path[i:]
    # This is how we get all possible inner paths
    for i in xrange(size, -1, -1):
        tmp -= path[i]
        if tmp == 0:
            result.append(path[i:])

Complexity
_________
N - number of nodes
H - height of Tree
Time - O(N^2)
Space - O(H)
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
        self.traverse(root, path, result, target)
        return result

    def traverse(self, node, path, result, target):
        if node is None:
            return
        path += [node.val]
        tmp = target
        size = len(path) - 1
        for i in xrange(size, -1, -1):
            tmp -= path[i]
            if tmp == 0:
                result.append(path[i:])
                """
                CANNOT HAVE THIS BECAUSE SAME PATh'S SUBPATHS might
                all be one solution
                """
                # path.pop()
                # return
        self.traverse(node.left, path, result, target)
        self.traverse(node.right, path, result, target)

        path.pop()
