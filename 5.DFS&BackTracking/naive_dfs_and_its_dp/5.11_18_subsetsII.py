"""
Description
____________
Given a list of numbers that may has duplicate numbers, return all possible subsets

 Notice

Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.
Have you met this question in a real interview? Yes
Example
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
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
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, S):
        # write your code here
        result = []
        S = sorted(S)
        self.dfs(S, 0, result, [])
        return result
 
    def dfs(self, S, start, result, branch):
        result.append(branch[:])
        for i in xrange(start, len(S)):
            if i > start and S[i] == S[i - 1]:
                continue
            else:
                branch.append(S[i])
                self.dfs(S, i + 1, result, branch)
                branch.pop()
