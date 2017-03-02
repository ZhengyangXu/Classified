#### Palindrome I

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

```python
def partition(self, s):
    # write your code here
    result = []
    branch = []
    self.dfs(s, 0, branch, result)
    return result

def dfs(self, s, start, branch, result):
    if start == len(s):
        result.append(branch[:])
        return
    for i in xrange(start, len(s)):
        if self.isPalindrome(s[start:i + 1]):
            branch.append(s[start:i + 1])
            self.dfs(s, i + 1, branch, result)
            branch.pop()
```
###### Notes
1. when append, make a copy @ 11
2. standard, append and pop off procedure after each branching @ 15, 17
3. dfs increment at i inside for loop @ 16

#### combination Sum
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

```python
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
```
###### Notes
0. Sort the candidates in this case @ 39
1. when append branch to result make a copy @ 46
2. DFS only when current element >= remain
3. can reuse one element so start at i @ 57

#### combinationSum II
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

```python
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
```
###### Notes
0. Only difference compared to I is to start at i + 1 to prohibit reuse of the element


#### Permutations
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

```python
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        result, branch, visited = [],[],[False for _ in xrange(len(nums))]
        self.dfs(nums, result,branch, visited)
        return result
    def dfs(self, nums, result, branch, visited):
        if len(branch) == len(nums):
            result.append(branch[:])
        for i in xrange(len(nums)):
            if not visited[i]:
                branch.append(nums[i])
                visited[i] = True
                self.dfs(nums, result, branch,visited)
                branch.pop()
                visited[i] = False
```
###### Notes
0. make a copy of branch when append to result @ 142
1. only dfs when not visited @ 144
2. keep track of visited or not and not dfs on position

#### Permutations II
Now there might exist duplicates
Given a list of numbers with duplicate number in it. Find all unique permutations.

Have you met this question in a real interview? Yes
Example
For numbers [1,2,2] the unique permutations are:

[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]

```python
class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        result, branch, visited = [],[], [False for _ in xrange(len(nums))]
        self.dfs(nums,result,[],visited)
        return result
    def dfs(self, nums, result, branch, visited):
        if len(branch) == len(nums):
            result.append(branch[:])
            return
        for i in xrange(len(nums)):
            # at current stack, [1,2,2] position 1,2 exchange postition are the same situations
            # so we donot branch when at position 2 and position 1 is not used
            if visited[i] or  ( i>0 and nums[i] == nums[i-1] and not visited[i-1]):
                continue
            else:
                branch.append(nums[i])
                visited[i] = True
                print branch, i,nums[i]
                self.dfs(nums, result, branch, visited)
                branch.pop()
                visited[i] = False
```
######
0. difference is since there are duplicates we donot dfs unless at current stack, nums[i] == nums[i-1] and nums[i-1] not visited because this solution is previsouly explored when we at nums[i-1]
1. we also now need to sort the array first

#### subsets
Given a set of distinct integers, return all possible subsets.

- Elements in a subset must be in non-descending order.
- The solution set must not contain duplicate subsets.

```python
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
            self.dfs(S, i+1, result, branch)
            branch.pop()
```
######
0. Must sort

#### subsets II
duplicates integers

```python
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
            if i > start and S[i] == S[i-1]:
                continue
            else:
                branch.append(S[i])
                self.dfs(S, i + 1, result, branch)
                branch.pop()
```
