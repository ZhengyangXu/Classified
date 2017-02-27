"""
Description
______________
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

Notice
____________
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Have you met this question in a real interview? Yes

Example
______________
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Appraoch
_____________
A tree with n nodes must be
1. has n-1 edges
2. A BFS must be able to reach all nodes (number of visits == n)

This translates to following algorithm

Complexity
Time - O(N)
SPace - O(N)
"""


class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false

    def validTree(self, n, edges):
        # Write your code here
        from collections import deque
        if n < 0:
            return False
        if len(edges) != n - 1:
            return False

        graph = self.createGraph(n, edges)
        visited = set([])
        q = deque()
        q.append(0)
        visited.add(0)
        counter = 0
        while q:
            cur = q.popleft()
            counter += 1
            if graph.has_key(cur):
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(cur)
        return counter == n

    def createGraph(self, n, edges):
        # return a dict node->[neighbor,neighbor...]

        from collections import defaultdict
        graph = defaultdict(list)
        for o, i in edges:
            graph[o].append(i)
            graph[i].append(o)
        return graph
