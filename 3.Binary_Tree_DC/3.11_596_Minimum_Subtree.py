"""

Description
_________________
Given a binary tree, find the subtree with minimum sum.
Return the root of the subtree.

Example
_________________
Given a binary tree:

     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5
return the node 1.

Appraoch
___________
Same as 3.11

Complexity
___________
Same as 3.11
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the minimum subtree
    minimum = None
    minimum_node = None

    def findSubtree(self, root):
        # Write your code here
        self.traverse_dc(root)
        return self.minimum_node

    def traverse_dc(self, root):
        if root == None:
            return 0

        left_sum = self.traverse_dc(root.left)
        right_sum = self.traverse_dc(root.right)

        result_sum = left_sum + right_sum + root.val

        if self.minimum is None or result_sum < self.minimum:
            self.minimum_node = root
            self.minimum = result_sum
        return result_sum
