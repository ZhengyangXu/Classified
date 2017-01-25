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
Similar to Binary_Tree_Path_Sum
D&Q, keep track of
general_max_length and max_from_root
Complexity
_________
O(N)
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
        _, result_max = self.helper(root)
        return result_max

    def helper(self, root):
        if root is None:
            return 0, 0
        left_from_root, left_max = self.helper(root.left)
        right_from_root, right_max = self.helper(root.right)

        result_from_root, result_max = 1, 0
        if root.left and root.left.val == root.val + 1:
            result_from_root = max(result_from_root, left_from_root + 1)
        if root.right and root.right.val == root.val + 1:
            result_from_root = max(result_from_root, right_from_root + 1)
        result_max = max(result_from_root, left_max, right_max)

        return result_from_root, result_max
