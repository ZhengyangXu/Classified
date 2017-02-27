"""
Description
____________________
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example
___________________
Given n = 2, prerequisites = [[1,0]]
Return [0,1]

Given n = 4, prerequisites = [1,0],[2,0],[3,1],[3,2]]
Return [0,1,2,3] or [0,2,1,3]

Approach & Time Complexity
___________________
Exact Same as previous one excpet we append the path here                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
"""


class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {int[]} the course order

    def findOrder(self, numCourses, prerequisites):
        # Write your code here
        from collections import defaultdict, deque

        edges = defaultdict(list)
        indegrees = defaultdict(int)
        [indegrees[i] for i in xrange(numCourses)]

        for i, o in prerequisites:
            edges[o].append(i)
            indegrees[i] += 1

        q = deque()
        count = 0
        res = []

        for k, v in indegrees.items():
            if v == 0:
                q.append(k)

        while q:
            cur = q.popleft()
            count += 1
            res.append(cur)

            for next_node in edges[cur]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0:
                    q.append(next_node)
        if count == numCourses:
            return res
        else:
            return []
