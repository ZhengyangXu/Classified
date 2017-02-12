"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

 Notice

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

public class Solution {

    private ArrayList<ArrayList<Integer>> results;

    public ArrayList<ArrayList<Integer>> combinationSum2(int[] candidates,
            int target) {
        if (candidates.length < 1) {
            return results;
        }

        ArrayList<Integer> path = new ArrayList<Integer>();
        java.util.Arrays.sort(candidates);
        results = new ArrayList<ArrayList<Integer>> ();
        combinationSumHelper(path, candidates, target, 0);

        return results;
    }

    private void combinationSumHelper(ArrayList<Integer> path, int[] candidates, int sum, int pos) {
        if (sum == 0) {
            results.add(new ArrayList<Integer>(path));
        }

        if (pos >= candidates.length || sum < 0) {
            return;
        }

        int prev = -1;
        for (int i = pos; i < candidates.length; i++) {
            if (candidates[i] != prev) {
                path.add(candidates[i]);
                combinationSumHelper(path, candidates, sum - candidates[i], i + 1);
                prev = candidates[i];
                path.remove(path.size()-1);
            }
        }
    }



xishuahusa
______

I
和3 sum那题很像，如果选定一个candidates[i]，则需要继续寻找和为target-candidate[i]的combination。由于candidates和target都为正数，当和超过或等于target时，查找中止。与3sum的思路一样，对candidate排序，并且每层递归扫描的时候需要做到去重复解：
1. 不回头扫，在扫描candidates[i]时，对candidate[i: n-1]递归查找target-candidates[i]。
2. 每层扫描的时候跳过重复的candidates。


class Solution {
public:
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        vector<vector<int> > allSol;
        vector<int> sol;
        if(candidates.empty()) return allSol;
        sort(candidates.begin(),candidates.end());
        findCombSum(candidates, 0, target, sol, allSol);
        return allSol;
    }

    void findCombSum(vector<int> &candidates, int start, int target, vector<int> &sol, vector<vector<int>> &allSol) {
        if(target==0) {
            allSol.push_back(sol);
            return;
        }

        for(int i=start; i<candidates.size(); i++) {
            if(i>start && candidates[i]==candidates[i-1]) continue;
            if(candidates[i]<=target) {
                sol.push_back(candidates[i]);
                findCombSum(candidates, i, target-candidates[i], sol, allSol);
                sol.pop_back();
            }
        }
    }
};


II
和I的唯一区别是每个candidate只能用一次。只需要在调用下一层递归时，查找范围的起始数字不是当前数字而是下一个数字即可。


class Solution {
public:
    vector<vector<int> > combinationSum2(vector<int> &num, int target) {
        vector<vector<int> > allSol;
        if(num.empty()) return allSol;
        sort(num.begin(),num.end());
        vector<int> sol;
        findCombSum2(num, 0, target, sol, allSol);
        return allSol;
    }

    void findCombSum2(vector<int> &num, int start, int target, vector<int> &sol, vector<vector<int> > &allSol) {
        if(target==0) {
            allSol.push_back(sol);
            return;
        }

        for(int i=start; i<num.size(); i++) {
            if(i>start && num[i]==num[i-1]) continue;
            if(num[i]<=target) {
                sol.push_back(num[i]);
                findCombSum2(num, i+1, target-num[i], sol, allSol);
                sol.pop_back();
            }
        }
    }
"""


class Solution:
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, candidates, target):
        # write your code here
        candidates.sort()
        self.ans, tmp, use = [], [], [0] * len(candidates)
        self.dfs(candidates, target, 0, 0, tmp, use)
        return self.ans

    def dfs(self, can, target, p, now, tmp, use):
        if now == target:
            self.ans.append(tmp[:])
            return
        for i in range(p, len(can)):
            if now + can[i] <= target and (i == 0 or can[i] != can[i - 1] or use[i - 1] == 1):
                tmp.append(can[i])
                use[i] = 1
                self.dfs(can, target, i + 1, now + can[i], tmp, use)
                tmp.pop()
                use[i] = 0
