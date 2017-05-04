"""
Description
_____________________
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1] 0 <- 1
Given the total number of courses and a list of prerequisite pairs,
is it possible for you to finish all courses?

Example
__________________
Given n = 2, prerequisites = [[1,0]]
Return true
Given n = 2, prerequisites = [[1,0],[0,1]]
Return false

Approach
__________________________
Topological sorting
++++++++++++++++++++++
0. initialize edges, indegrees
*1. every course has a key in indegrees even if it's not present in prerequisite
2. instantiate edge, indegrees by looping through prerequisite.
3. start topological sorting
4. Check the number of nodes we get to visit should be exactly equal to numof courses
or
4. check whehter should still left non-zero indegrees value (if exists, False)
"""


class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {boolean} true if can finish all courses or false

    def canFinish(self, numCourses, prerequisites):
        # Write your code here
        from collections import defaultdict, deque
        edges = defaultdict(list)
        indegrees = defaultdict(int)

        q = deque()
        count = 0 
        [indegrees[i] for i in xrange(numCourses)]
        for i, o in prerequisites:
            edges[o].append(i)
            indegrees[i] += 1

        for k, v in indegrees.items():
            if v == 0:
                q.append(k)

        while q:
            cur = q.popleft()
            count += 1

            for next_node in edges[cur]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0:
                    q.append(next_node)
        return count == numCourses
