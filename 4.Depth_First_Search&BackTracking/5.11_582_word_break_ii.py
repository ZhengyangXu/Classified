"""
Description
_____________
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

Example
______________
Gieve s = lintcode,
dict = ["de", "ding", "co", "code", "lint"].

A solution is ["lint code", "lint co de"].

Approach
______________
This is very similar to the dfs palindrome problem in a way
So the standard version is easy to understand
recursive recurrence
DFS(S) = S[start:i+1] + DFS(S[i+1:])

for python to pass
we have to use the canbreak as a interesting pruning technique

when DFS return up to previous stack, if result does not have an elment added
this branch canbreak[i+1]= False

"""


class Solution:
    # @param {string} s a string
    # @param {set[str]} wordDict a set of words

    def wordBreak(self, s, wordDict):
        # Write your code here
        if s is None or len(s) == 0 or wordDict is None:
            return None
        result, branch = [], []
        canbreak = [True for _ in xrange(len(s) + 1)]
        self.dfs(s, wordDict, 0, branch, result, canbreak)
        return result

    def iswordBreak(self, s, dict):
        if len(dict) == 0:
            return len(s) == 0

        n = len(s)
        f = [False] * (n + 1)
        f[0] = True

        maxLength = max([len(w) for w in dict])
        for i in xrange(1, n + 1):
            for j in range(1, min(i, maxLength) + 1):
                if not f[i - j]:
                    continue
                if s[i - j:i] in dict:
                    f[i] = True
                    break

        return f[n]

    def dfs(self, s, dic, start, branch, result, canbreak):
        if start == len(s):
            temp = branch[:]
            result.append(' '.join(temp))
            return
        for i in xrange(start, len(s)):
            left = s[start:i + 1]
            if left not in dic:
                continue
            # standard version is to use wordbreak(left,dict)
            if not canbreak[i + 1]:
                continue
            branch.append(left)
            before_size = len(result)
            self.dfs(s, dic, i + 1, branch, result, canbreak)
            if len(result) == before_size:
                canbreak[i + 1] = False
            branch.pop()
