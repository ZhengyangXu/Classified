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
________________________
at a root 3 situations
1. maxpath lies at left tree
2. maxpath lies at right
3. maxpath must combine left and right passing through root

SO we keep track of two variables and use DQ
++++++++++++++++++++++++
Maintain -
1. maxRoot starts from root (contains at least one node)
2. max starts from any node (contains at least one node)
Base - if None return, -maxint, -maxint

Recursion -

new_maxRoot = root.val + max(0, left_maxRoot, right_maxRoot)
new_max = max(max(left_maxRoot, 0) + max(right_maxRoot, 0) + root.val, max(left_max, right_max))

Notice how we decide new_max here
we utilize left_maxRoot, right_maxRoot to connect with current node
THAT'S IMPORTANT how it is different from II

Complexity
__________
N - number of nodes
H - height of Tree
Time - O(N)
Space - o(H)
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
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
    @return: An integer
    """
    import sys

    def maxPathSum(self, root):
        # write your code here
        _, maximum = self.helper(root)
        return maximum

    def helper(self, root):
        if root is None:
            return -sys.maxint, -sys.maxint
        left_maxRoot, left_max = self.helper(root.left)
        right_maxRoot, right_max = self.helper(root.right)

        new_maxRoot = root.val + max(0, left_maxRoot, right_maxRoot)
        new_max = max(max(left_maxRoot, 0) + max(right_maxRoot, 0) + root.val, max(left_max, right_max))

        return new_maxRoot, new_max
