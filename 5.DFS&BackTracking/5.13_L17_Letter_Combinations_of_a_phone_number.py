"""
Description
____________
Given a digit string, return all possible
letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.

Example
____________
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""


class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None or len(digits) == 0:
            return []
        dic = {'0': [" "], '1': ["*"], '2': ["a", "b", "c"],
               '3': ["d", "e", "f"], '4': ["g", "h", "i"],
               '5': ["j", "k", "l"], '6': ["m", "n", "o"],
               '7': ["p", "q", "r", "s"], '8': ["t", "u", "v"], '9': ["w", "x", "y", "z"]}

        A = [dic[i] for i in digits]
        result = []

        self.dfs(A, result, [])
        return result

    def dfs(self, A, result, path):
        # print A
        if len(path) == len(A):
            # print path
            result.append("".join(path[:]))
            return
        for i in (A[len(path)]):
            path.append(i)
            self.dfs(A, result, path)
            path.pop()
