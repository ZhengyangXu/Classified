"""
Description
_______________________
Given two words (start and end), and a dictionary
find all shortest transformation sequence(s) from start to end, such that:
1. Only one letter can be changed at a time
2. Each intermediate word must exist in the dictionary

Example
________________________
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

Approach
_________________________
Use previously discussded BFS approach to build
(adj_list) for each node's neighbors
(distance) to indicate closet path distance from start to node_i

use those two to impelement a DFS search to find all paths
only DFS when distance[node_j] = distance [node_i] + 1 where node_j in adj_list[node_i]

Complexity
Time -- O(N^2)
Space -- O(N^2)
"""
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string

    def findLadders(self, start, end, dict):
        # write your code here
        adj_list, distance = self.bfs(start, end, dict)
        result, branch = [], []
        self.dfs(adj_list, distance, result, branch, start, end)
        # print adj_list,distance
        return result

    def bfs(self, start, end, dict):
        # return map and distance
        from collections import deque, defaultdict
        import sys
        dict.add(end)
        q = deque()
        adj_list = defaultdict(list)
        distance = defaultdict(int)
        visited = []
        # initalize adjacency list for every node except start and end
        [adj_list[i] for i in dict]
        distance[start] = 0
        for i in dict:
            distance[i] = sys.maxint
        distance[end] = sys.maxint
        q.append(start)
        visited.append(start)
        count = 0
        while q:
            size = len(q)
            for i in xrange(size):
                cur = q.popleft()
                # print count ,cur
                # print visited
                distance[cur] = count
                if cur == end:
                    return adj_list, distance
                neighbors = self.findNeighbors(cur, dict)
                adj_list[cur] = neighbors

                for neighbor in neighbors:
                    if neighbor not in visited:

                        # print "not in visited==>" + neighbor
                        q.append(neighbor)
                        visited.append(neighbor)
            count += 1
        return adj_list, distance

    def dfs(self, adj_list, distance, result, branch, cur, end):
        branch.append(str(cur))
        # print branch
        if cur == end:
            result.append(branch[:])

        for neighbor in adj_list[cur]:
            if distance[neighbor] == distance[cur] + 1:
                self.dfs(adj_list, distance, result, branch, neighbor, end)

        branch.pop()

    def findNeighbors(self, s, source_dic):
        ord_a = ord('a')
        neighbors = []

        for s_i in xrange(len(s)):
            list_s = [i for i in s]
            ordinal = ord(s[s_i])
            for i in xrange(26):
                if ordinal == ord_a + i:
                    continue
                else:
                    list_s[s_i] = chr(ord_a + i)
                    temp = "".join(list_s)
                    if temp in source_dic:
                        neighbors.append(temp)
        return neighbors
