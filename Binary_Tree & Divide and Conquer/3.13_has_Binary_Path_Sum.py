"""
Description
____________
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Empty Leaf with one root does not count
"""
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        sum -= root.val
        if root.left is None and root.right is None:
            if sum == 0:
                return True
            else:
                return False
        left, right = False, False
        if root.left:
            left = self.hasPathSum(root.left, sum)
        if root.right:
            right = self.hasPathSum(root.right, sum)
        return left or right
