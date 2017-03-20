"""
Description
________________
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Example
__________________
Example
Given a binary tree as follow:
  1
 / \
2   3
   / \
  4   5
The maximum depth is 3.

Approach
___________
DQ

Compleixty
____________

T(N) = 2T(N/2) + C
Log(b,a) = 1
c = 0
so
N - number of nodes
H - height of Tree
Time - O(N)
Space - o(H)

SOdepends on the Tree, if it's balanced Lg(N), otherwise O(N)
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
    @return: An integer
    """

    def maxDepth(self, root):
        # write your code here
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
