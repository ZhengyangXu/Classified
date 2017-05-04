"""
Description
________________
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Have you met this question in a real interview? Yes
Example
Given candidate set [10,1,6,7,2,1,5] and target 8,

A solution set is:

[
  [1,7],
  [1,2,5],
  [2,6],
  [1,1,6]
]

"""
 
class Solution:
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
        # write your code here
        result, branch = [], []
        candidates = sorted(candidates)
        self.dfs(0, candidates, target, result, branch)
        return result

    def dfs(self, start, candidates, remain, res, branch):
        # print branch,start,remain
        if remain == 0:
            res.append(branch[:])
            return
        for i in xrange(start, len(candidates)):
            # This get rid of repeatitive results
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if remain - candidates[i] >= 0:

                remain = remain - candidates[i]
                branch.append(candidates[i])
                # print branch,i
                self.dfs(i + 1, candidates, remain, res, branch)
                branch.pop()
                remain += candidates[i]
