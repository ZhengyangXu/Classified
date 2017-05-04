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

Approach
________

See code

Complexity
__________
N - number of nodes
H - height of Tree
Time - O(N)
Space - o(H)
"""


"""
Use Iterative
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        from collections import deque
        stack = deque()
        stack.append(root)
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

"""
Use Divide and Conquer
"""
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
