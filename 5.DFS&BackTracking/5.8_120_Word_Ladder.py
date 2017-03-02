"""
Description
___________________
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary

Example
_____________________
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Approach
________________________
Translate this to a graph search problem.
each word can exchange one character at a time eg. "hot"
there are then 3*26 possible next nodes, n_i. n_i is a neighbor (next_node) when
it's in the dict (find neighbors)

Then start point as start, end as end, do BFS

Complexity
________________
Time - O(N^2)
Space - O(N)
"""


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer

    def ladderLength(self, start, end, dict):
        # write your code here
        visited = []
        from collections import deque
        q = deque()
        count = 1
        dict.add(end)
        q.append(start)
        while q:
            size = len(q)
            for i in xrange(size):
                cur = q.popleft()
                # print cur
                visited.append(cur)
                if cur == end:
                    return count
                # print "neighbors%s" % (self.findNeighbors(cur,dict))
                for i in self.findNeighbors(cur, dict):
                    if i not in visited:
                        # print "=>" + str(i)
                        q.append(i)
            count += 1
        return count

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
                    temp = ''.join(list_s)
                    if temp in source_dic:
                        neighbors.append(temp)
                        source_dic.remove(temp)
        return neighbors
