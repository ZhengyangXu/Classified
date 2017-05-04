"""
Given a list of numbers, return all possible permutations.

 Notice

You can assume that there is no duplicate numbers in the list.

Have you met this question in a real interview? Yes
Example
For nums = [1,2,3], the permutations are:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
Approach
__________
DFS
++++
Connecting point at
availale indexes of the whole array
details see notes_for_dfs

Complexity
_________
Exponential
"""
 

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        result, branch, visited = [], [], [False for _ in xrange(len(nums))]
        self.dfs(nums, result, branch, visited)
        return result

    def dfs(self, nums, result, branch, visited):
        if len(branch) == len(nums):
            result.append(branch[:])
        for i in xrange(len(nums)):
            if not visited[i]:
                branch.append(nums[i])
                visited[i] = True
                self.dfs(nums, result, branch, visited)
                branch.pop()
                visited[i] = False
