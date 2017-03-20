"""
Description
______________
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Have you met this question in a real interview? Yes

Example
_____________
For example,

   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.

   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

Approach
_______
Recursive DQ
++++++++++++++
Similar to Binary_Tree_Path_Sum
D&Q, keep track of
general_max_length and max_from_root

Maintain - maxlength(general_max_length, have at least one node)
           maxRoot(max_from_root, have at least one node)

Base - if None, return -sys.maxint, -sys.maxint or 0, 0
(because nothing is smaller than 0 when counting length)

Recursion -
    left_fromRoot, left_max = self.dchelper(root.left)
    right_fromRoot, right_max = self.dchelper(root.right)

    # at length one
    result_fromRoot, result_max = 1, 1
    if root.left and root.left.val == root.val + 1:
        result_fromRoot = max(result_fromRoot, left_fromRoot + 1)
    if root.right and root.right.val == root.val + 1:
        result_fromRoot = max(result_fromRoot, right_fromRoot + 1)
    result_max = max(result_fromRoot, left_max, right_max)

Complexity
_________
N - number of nodes
H - height of Tree
Time - O(N)
Space - O(H)
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path

    def longestConsecutive(self, root):
        # Write your code here
        _, result_max = self.dchelper(root)
        return result_max

    def dchelper(self, root):
        if root is None:
            return 0, 0

        left_fromRoot, left_max = self.dchelper(root.left)
        right_fromRoot, right_max = self.dchelper(root.right)

        result_fromRoot, result_max = 1, 1
        if root.left and root.left.val == root.val + 1:
            result_fromRoot = max(result_fromRoot, left_fromRoot + 1)
        if root.right and root.right.val == root.val + 1:
            result_fromRoot = max(result_fromRoot, right_fromRoot + 1)
        result_max = max(result_fromRoot, left_max, right_max)

        return result_fromRoot, result_max
