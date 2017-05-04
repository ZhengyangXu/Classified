"""
Description
______________
Tree contians both node
have parent link
"""

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
 

class Solution:
    """
    @param root: The root of the tree
    @param A and B: Two node in the tree
    @return: The lowest common ancestor of A and B
    """

    def lowestCommonAncestorII(self, root, A, B):
        # Write your code here
        # Write your code here
        A_visited = []
        B_visited = []

        while A is not None or B is not None:
            A_visited.append(A)
            B_visited.append(B)
            if A in B_visited:
                return A
            if B in A_visited:
                return B
            if A:
                A = A.parent
            if B:
                B = B.parent
        return None
