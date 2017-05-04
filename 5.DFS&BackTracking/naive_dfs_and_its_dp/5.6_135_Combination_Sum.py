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
        result = []
        candidates.sort()
        self.dfs(0, result, [], 0, target, candidates)
        return result

    def dfs(self, start, result, path, cur, target, A):
        if cur == target:
            result.append(path[:])
            return
        for i in xrange(start, len(A)):
            if i != 0 and A[i] == A[i - 1]:
                continue
            if A[i] + cur <= target:
                cur += A[i]
                path.append(A[i])

                self.dfs(i, result, path, cur, target, A)

                path.pop()
                cur -= A[i]
