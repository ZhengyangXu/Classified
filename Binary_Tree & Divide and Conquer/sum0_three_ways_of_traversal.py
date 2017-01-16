"""
I Come
I Divide
I Conquer
"""
# inorder Divide and Conquer


class Solution:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        result = []
        if root == None:
            return result
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        result.extend(left)
        result.append(root.val)
        result.extend(right)

        return result

# Preorder Divide and Conquer


class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        result = []
        if root is None:
            return result
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        result.append(root.val)
        result.extend(left)
        result.extend(right)
        return result
# PostOrder Divide and Conquer

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
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
        # write your code here
        result = []
        if root == None:
            return result
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        result.extend(left)
        result.extend(right)
        result.append(root.val)
        return result


"""
=====================================================================================
"""

"""
Iterative Bitches
"""

# Inorder Iterative
