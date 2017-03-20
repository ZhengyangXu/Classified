"""
Description
_____________
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

Example
_____________
Example
Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None

Approach
------------
Divide conquer 遍历
class variable to keep track of maxnode and maxavg

Global maintain - maxNode, maxAvg
Maintain - size, sum
base - root is None, return 0 , 0

Recursion and update

    left_size, left_max = self.traverse_dc(root.left)
    right_size, right_max = self.traverse_dc(root.right)

    result_size = left_size + right_size + 1
    result_max = left_max + right_max + root.val
    result_avg = result_max * 1.0 / result_size
    if self.maxAvg is None or self.maxAvg < result_avg:
        self.maxNode = root
        self.maxAvg = result_avg

Complexity
___________
N - number of nodes
H - height of Tree
Time - O(N)
Space - o(H)
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of twe
    # the maximum average of subtree
    maxNode = None
    maxAvg = None

    def findSubtree2(self, root):
        # Write your code here
        self.traverse_dc(root)
        return self.maxNode

    def traverse_dc(self, root):
        if root is None:
            return 0, 0
        left_size, left_max = self.traverse_dc(root.left)
        right_size, right_max = self.traverse_dc(root.right)

        result_size = left_size + right_size + 1
        result_max = left_max + right_max + root.val
        result_avg = result_max * 1.0 / result_size
        if self.maxAvg is None or self.maxAvg < result_avg:
            self.maxNode = root
            self.maxAvg = result_avg
        return result_size, result_max
