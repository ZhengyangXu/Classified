"""
Description
____________
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
Return null if LCA does not exist

Example
______________
For the following binary tree:

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7


Approach
_____________

SImilar idea compared to LCA I. However sicne A, B can not eixist in the tree. we have to account for that situation
so Divide and conquer, return
root, a_exist, b_exist

Note that the push-up of root when encountered comes after the divide and counter now because we have to decide a_exist b_exist

"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
 

class Solution:
    """
    @param {TreeNode} root The root of the binary tree.
    @param {TreeNode} A and {TreeNode} B two nodes
    @return Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        result, a_exist, b_exist = self.helper(root, A, B)
        if a_exist and b_exist:
            return result
        else:
            return None

    def helper(self, root, A, B):
        # return LCA, a_exist,b_exist
        if root is None:
            return None, False, False
        left, left_a_exist, left_b_exist = self.helper(root.left, A, B)
        right, right_a_exist, right_b_exist = self.helper(root.right, A, B)

        a_exist = left_a_exist or right_a_exist or root is A
        b_exist = left_b_exist or right_b_exist or root is B

        if root is A or root is B:
            return root, a_exist, b_exist

        if left is not None and right is not None:
            return root, a_exist, b_exist
        if left is not None:
            return left, a_exist, b_exist
        if right is not None:
            return right, a_exist, b_exist

        return None, a_exist, b_exist
