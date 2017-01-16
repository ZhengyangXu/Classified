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
==========
Divide and Conquer
A BT is BST if
a. left tree is BST
b. right tree is BST
c. min of right tree > root value
d. max value of left tree < root value
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        # write your code here
        def helper(root):
            # assume this retunrs max, min, isBST
            if root == None:
                return -sys.maxint - 1, sys.maxint, True
            isBST = True
            left_max, left_min, left_isBST = helper(root.left)
            right_max, right_min, right_isBST = helper(root.right)

            new_max = max(right_max, root.val)
            new_min = min(left_min, root.val)

            isBST = left_isBST and right_isBST and (left_max < root.val) and (right_min > root.val)

            return new_max, new_min, isBST

        _, _, isBST = helper(root)
        return isBST
