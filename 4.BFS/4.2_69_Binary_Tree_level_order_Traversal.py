"""
Description
___________________
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Have you met this question in a real interview? Yes
Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7

Approach
____________________
standard BFS approach
+
force to pop all current level node using a for loop
append all this level popped nodes as a list and append to result

Complexity
Time - O(N)
Space- O(N)
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
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        if root is None:
            return []
        from collections import deque
        q = deque()
        result = []
        q.append(root)
        while q:
            level_size = len(q)
            level = []
            for i in xrange(level_size):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            result.append(level)
        return result
