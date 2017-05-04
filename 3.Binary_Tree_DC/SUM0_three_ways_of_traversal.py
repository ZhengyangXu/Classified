"""
Three traversals

Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1

Breadth First or Level Order Traversal : 1 2 3 4 5
Please see this post for Breadth First Traversal.

Inorder Traversal:

Algorithm Inorder(tree)
   1. Traverse the left subtree, i.e., call Inorder(left-subtree)
   2. Visit the root.
   3. Traverse the right subtree, i.e., call Inorder(right-subtree)
Uses of Inorder
In case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder itraversal s reversed, can be used.
Example: Inorder traversal for the above given figure is 4 2 5 1 3.
 

Preorder Traversal:

Algorithm Preorder(tree)
   1. Visit the root.
   2. Traverse the left subtree, i.e., call Preorder(left-subtree)
   3. Traverse the right subtree, i.e., call Preorder(right-subtree)
Uses of Preorder
Preorder traversal is used to create a copy of the tree. Preorder traversal is also used to get prefix expression on of an expression tree. Please see http://en.wikipedia.org/wiki/Polish_notation to know why prefix expressions are useful.
Example: Preorder traversal for the above given figure is 1 2 4 5 3.

Practice Preorder Traversal


Postorder Traversal:

Algorithm Postorder(tree)
   1. Traverse the left subtree, i.e., call Postorder(left-subtree)
   2. Traverse the right subtree, i.e., call Postorder(right-subtree)
   3. Visit the root.
"""



"""
Traverse
"""

# preorder

class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, cur, result):
        if cur is None:
            return
        result.append(cur.val)
        self.traverse(cur.left, result)
        self.traverse(cur.right, result)

# postorder

class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, root, result):
        if root is None:
            return
        self.traverse(root.left, result)
        self.traverse(root.right, result)
        result.append(root.val)

# inorder

class Solution:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, root, result):
        if root is None:
            return
        self.traverse(root.left, result)
        result.append(root.val)
        self.traverse(root.right, result)
        return result


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


class Solution:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        if root == None:
            return []
        stack = []
        res = []
        cur = root
        while cur is not None or len(stack) > 0:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            node = cur
            cur = cur.right
            res.append(node.val)
        return res

# Preorder Iterative


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

        # Post order
    def postorderTraversal(self, root):
        if root is None:
            return []
        stack = []
        res = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        output = []
        while res:
            output.append(res.pop())
        return output
