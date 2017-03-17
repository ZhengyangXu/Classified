"""
Description
_____________
Implement strStr function in O(n + m) time.
strStr return the first index of the target string in a source string.
The length of the target string is m and the length of the source string is n.
If target does not exist in source, just return -1.

Example
____________
Given source = abcdef, target = bcd, return 1.

Approach
____________
KMP
++++++++

source -- a b c a c f
target -- a b a

i - pointer at source
j - pointer at target
n - len(source)

Like the naive solution increment i and j to matc target to source
a. when  target[i] == target[j]:
    i += 1
    j += 1
    if j== m:
        reutrn i - j
b. when not, unlike naive solution we donot start again from begining of target
  move j to lps[j-1]


Now how to build lps ?

This is essentially matching target[1:] to target[0:] using KMP

    def complieLongestPrefixSum(self,target):
        i = 0
        j = 1
        n = len(target)
        lps = [0] * n
        while i < n:
            if target[i] == target[j]:
                j += 1
                target[i] = j
                i += 1
            else:
                if j == 0:
                    lps[i] = 0
                    i += 1
                else:
                    j = lps[j-1]
        return lps

Correctness
___________

Compleixty
____________

"""
def complieLongestPrefixSum(self,target):
    i = 0
    j = 1
    n = len(target)
    lps = [0] * n
    while i < n:
        if target[i] == target[j]:
            j += 1
            target[i] = j
            i += 1
        else:
            if j == 0:
                lps[i] = 0
                i += 1
            else:
                j = lps[j-1]
    return lps


def Kmpstr(source, target):
    lps = complieLongestPrefixSum(target)
    i, j = 0, 0
    n = len(source)
    m = len(target)

    while i < n:
        if target[i] == source[j]:
            i += 1
            j += 1

            if j == m:
                return i - j
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]
    return -1

class Solution:
    # @param {string} source a source string
    # @param {string} target a target string
    # @return {int} an integer as index

    def strStr2(self, source, target):
        # Write your code here
        if target is None:
            return -1
        if len(target) == 0:
            return 0
        if source is None or len(source) == 0:
            return -1

        i = 0
        j = 0

        n = len(source)
        m = len(target)
        lps = self.compileLPS(target)
        # print lps
        while i < n:

            if source[i] == target[j]:
                # print i,j, "in here"
                i += 1
                j += 1
                if j == m:
                    return i - j
            else:
                # print i,j
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
        return -1

    def compileLPS(self, target):
        n = len(target)
        l = 0
        i = 1
        lps = [0] * n
        while i < n:
            if target[l] == target[i]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l == 0:
                    lps[i] = 0
                    i += 1
                else:
                    l = lps[l - 1]
        return lps
