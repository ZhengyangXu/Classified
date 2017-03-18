"""
Description
==========
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

Example
==========
Given the below binary tree:

  1
 / \
2   3
return 6

Approach
===========
at a root 3 situations
1. maxpath lies at left tree
2. maxpath lies at right
3. maxpath must combine left and right passing through root

SO we keep track of two variables and use DQ
# This is important
# means we do extra max with 0 at new_max 
1. maxRoot starts from root (contains at least one node)
2. max starts from any node (contains at least one node)
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import sys

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxPathSum(self, root):
        # write your code here
        # Define both maxRoot, max must have at least one point in it
        def helper(root):
            # return max_from_root, max
            if root == None:
                return -sys.maxint, -sys.maxint
            left_maxRoot, left_max = helper(root.left)
            right_maxRoot, right_max = helper(root.right)

            new_maxRoot = root.val + max(left_maxRoot, right_maxRoot, 0)
            new_max = max(max(left_maxRoot, 0) + max(right_maxRoot, 0) + root.val, max(left_max, right_max))

            return new_maxRoot, new_max

        _, maximum = helper(root)
        return maximum
