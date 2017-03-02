"""
Description
______________________
Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.

For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Example
given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]

Approach
__________
DFS
Details see notes_for dfs
Complexity
___________
2^N
"""
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers

    def combinationSum(self, candidates, target):
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
                self.dfs(i, candidates, remain, res, branch)
                branch.pop()
                remain += candidates[i]
