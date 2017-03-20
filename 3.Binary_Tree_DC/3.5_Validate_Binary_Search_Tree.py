"""
Description
============
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
Example
=============
An example:

  2
 / \
1   4
   / \
  3   5
The above binary tree is serialized as {2,1,4,#,#,3,5} (in level order).

"""

"""
Approach
___________
Recursive DQ
++++++++++++
A BT is BST if
a. left tree is BST
b. right tree is BST
c. min of right tree > root value
d. max value of left tree < root value

So
maintain - max, min, isBST
base - -sys.maxint, sys.maxint, True
recursion -

    left_max, left_min, left_isBST = helper(root.left)
    right_max, right_min, right_isBST = helper(root.right)

    new_max = max(right_max, root.val)
    new_min = min(left_min, root.val)

    isBST = left_isBST and right_isBST and (left_max < root.val)
            and (right_min > root.val)

    return new_max, new_min, isBST



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
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        # write your code here
        is_bst, _, _ = self.validate(root)
        return is_bst

    def validate(self, root):
        import sys
        if root is None:
            # return is_bst, max, min
            return True, -sys.maxint, sys.maxint

        left_bst, left_max, left_min = self.validate(root.left)
        right_bst, right_max, right_min = self.validate(root.right)
        is_bst = False
        if left_bst and right_bst and left_max < root.val and right_min > root.val:
            is_bst = True
        result_max = max(root.val, right_max)
        result_min = min(left_min, root.val)

        return is_bst, result_max, result_min
