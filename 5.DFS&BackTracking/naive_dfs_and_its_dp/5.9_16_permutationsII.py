"""
Description
_____________
Given a list of numbers with duplicate number in it. Find all unique permutations.

Have you met this question in a real interview? Yes
Example
For numbers [1,2,2] the unique permutations are:

[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]

Approach
___________
DFS
details see notes for dfs

Complexity
___________
Exponential
"""
class Solution
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
 
    def permuteUnique(self, nums):
        # write your code here
        result, branch, visited = [], [], [False for _ in xrange(len(nums))]
        self.dfs(nums, result, [], visited)
        return result

    def dfs(self, nums, result, branch, visited):
        if len(branch) == len(nums):
            result.append(branch[:])
            return
        for i in xrange(len(nums)):
            # at current stack, [1,2,2] position 1,2 exchange postition are the same situations
            # so we donot branch when at position 2 and position 1 is not used
            if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                continue
            else:
                branch.append(nums[i])
                visited[i] = True
                print branch, i, nums[i]
                self.dfs(nums, result, branch, visited)
                branch.pop()
                visited[i] = False
