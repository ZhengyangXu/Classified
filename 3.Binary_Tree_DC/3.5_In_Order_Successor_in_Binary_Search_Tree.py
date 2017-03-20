"""
Description
_____________
Given a binary search tree (See Definition) and a node in it, find the in-order successor of that node in the BST.
If the given node has no in-order successor in the tree, return null.

Notice
____________
It's guaranteed p is one node in the given tree. (You can directly compare the memory address to find p)

Example
____________
Given tree = [2,1] and node = 1:

  2
 /
1
return node 2.

Given tree = [2,1,3] and node = 2:

  2
 / \
1   3
return node 3.



Approach
______________

two situations
a. have right tree, leftmost of right tree
b. not, either parent or null

for b Utilize BST to search for it

Only update parent_successor when branching to left
because only left of root has inorderSuccessor
    parent_successor = None
    while root.val != p.val and root != None:
        if p.val > root.val:
            root = root.right
        else:
            parent_successor = root
            root = root.left
    return parent_successor

Complexity
__________
N - number of nodes
H - height of Tree
Time - O(N)
Space - o(H)
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        # write your code here
        if root is None or p is None:
            return None

        if p.right != None:
            p = p.right
            while (p.left != None):
                p = p.left

            return p

        else:
            parent_successor = None
            while root.val != p.val and root != None:
                if p.val > root.val:
                    root = root.right
                else:
                    parent_successor = root
                    root = root.left
            return parent_successor
