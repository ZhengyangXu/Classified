"""
Given a binary tree, return the preorder traversal of its nodes' values.

   1
   / \
  2   3
 / \
4   5
return [1,2,4,5,3].
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


"""
Use Recursion
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in list which contains node values.
    """

    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder
"""
Use Traverse
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        def traverse(root, result):
            if root is None:
                return
            result.append(root.val)
            traverse(root.left, result)
            traverse(root.right, result)
        result = []
        traverse(root, result)
        return result

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
