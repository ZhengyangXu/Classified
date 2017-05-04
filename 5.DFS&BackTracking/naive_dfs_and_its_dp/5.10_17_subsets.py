"""
Description
___________
Given a set of distinct integers, return all possible subsets.

 Notice

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Have you met this question in a real interview? Yes
Example
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Approach
___________
DFS
details see notes for dfs

Complexity
___________
Exponential
"""


class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
 
    def subsets(self, S):
        # write your code here
        result, branch = [], []
        S = sorted(S)
        self.dfs(S, 0, result, branch)
        return result

    def dfs(self, S, start, result, branch):
        result.append(branch[:])
        for i in xrange(start, len(S)):
            branch.append(S[i])
            self.dfs(S, i + 1, result, branch)
            branch.pop()
