"""
Description
_________________
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs.
The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 10^4.
Reconstruction means building a shortest common supersequence of the sequences in seqs
(i.e., a shortest sequence so that all sequences in seqs are subsequences of it).
Determine whether there is only one sequence that can be reconstructed from seqs
and it is the org sequence.

Example
________________
Given org = [1,2,3], seqs = [[1,2],[1,3]]
Return false
Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

Given org = [1,2,3], seqs = [[1,2]]
Return false
Explanation:
The reconstructed sequence can only be [1,2].

Given org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Return true
Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Given org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Return true


seqs = [1,2] , [1,3]
1->2 ; 1->3
find topological sorting path

build
indegrees and edges to do topological sorting

(1) only one path <-> Queue is always 1
(2) the path is the same as org
"""


class Solution:
    # @param {int[]} org a permutation of the integers from 1 to n
    # @param {int[][]} seqs a list of sequences
    # @return {boolean} true if it can be reconstructed only one or false

    def sequenceReconstruction(self, org, seqs):
        # Write your code here
        from collections import defaultdict
        edges = defaultdict(list)
        indegrees = defaultdict(int)
        for seq in seqs:
            for i in xrange(len(seq)):
                if i == 0:
                    indegrees[seq[i]] += 0
                if i < len(seq) - 1:
                    edges[seq[i]].append(seq[i + 1])
                    indegrees[seq[i + 1]] += 1

        cur = [k for k in indegrees if indegrees[k] == 0]
        res = []

        while len(cur) == 1:
            cur_node = cur.pop()
            res.append(cur_node)
            for node in edges[cur_node]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    cur.append(node)
        if len(cur) > 1:
            return False
        return res == org
