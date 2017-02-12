"""

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]
0 <- 1

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example
Given n = 2, prerequisites = [[1,0]]
Return true

Given n = 2, prerequisites = [[1,0],[0,1]]
Return false

这道课程清单的问题对于我们学生来说应该不陌生，因为我们在选课的时候经常会遇到想选某一门课程，发现选它之前必须先上了哪些课程，这道题给了很多提示，第一条就告诉我们了这道题的本质就是在有向图中检测环。
LeetCode中关于图的题很少，有向图的仅此一道，还有一道关于无向图的题是 Clone Graph 无向图的复制。
个人认为图这种数据结构相比于树啊，链表啊什么的要更为复杂一些，尤其是有向图，很麻烦。第二条提示是在讲如何来表示一个有向图，可以用边来表示，边是由两个端点组成的，
用两个点来表示边。第三第四条提示揭示了此题有两种解法，DFS和BFS都可以解此题。我们先来看BFS的解法，我们定义二维数组graph来表示这个有向图，
一位数组in来表示每个顶点的入度。我们开始先根据输入来建立这个有向图，并将入度数组也初始化好。然后我们定义一个queue变量，将所有入度为0的点放入队列中，
然后开始遍历队列，从graph里遍历其连接的点，每到达一个新节点，将其入度减一，如果此时该点入度为0，则放入队列末尾。直到遍历完队列中所有的值，若此时还有节点的入度不为0，则
说明环存在，返回false，反之则返回true。代码如下：

or
in this case
we check the number of nodes we get to visit should be exactly equal to numof courses

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
