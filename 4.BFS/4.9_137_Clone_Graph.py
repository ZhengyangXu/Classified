"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

How we serialize an undirected graph:

Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

   1
  / \
 /   \
0 --- 2
     / \
     \_/

Approach
_________________
I think code here is straightforward
0. initialise a hashmap, a queue, create a new copy of node
1. hashmap[node] = new_node
2. bfs
    a. pop the node, grab the node copy by copy = hashmap[node]
    b. append in copy's neighbors
        (1). if neighbor inside hashmap, just append
        (2). not, create a copy, enter hashmap, then appened

note:
0. queue(bfs), stack(dfs) both work here


"""


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def __init__(self):
        self.dict = {}

    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return
        from collections import deque
        copiedMap = {}
        q = deque()
        q.append(node)
        new_node = UndirectedGraphNode(node.label)
        copiedMap[node] = new_node
 
        while q:
            cur = q.popleft()
            # print cur.label, [i.label for i in cur.neighbors], [i.label for i in copiedMap.keys()]
            copiedCur = copiedMap[cur]
            for neighbor in cur.neighbors:
                if neighbor in copiedMap:
                    copiedNeigbor = copiedMap[neighbor]
                    copiedCur.neighbors.append(copiedNeigbor)
                else:
                    new_neighbor = UndirectedGraphNode(neighbor.label)
                    q.append(neighbor)
                    copiedMap[neighbor] = new_neighbor
                    copiedCur.neighbors.append(new_neighbor)
        return new_node
