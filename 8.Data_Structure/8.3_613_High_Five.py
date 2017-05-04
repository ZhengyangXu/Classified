"""
Description
____________
There are two properties in the node student id and scores, to ensure that
each student will have at least 5 points
find the average of 5 highest scores for each person.

Appproach
_____________
0. Initailize dic, result = defaultdict(list), {}
1. for rec in results:
    (a)Maintain a size 5 minheap, so (n-5) number of smallest number will be poped
       leave top 5 number on the heap(then we can take the average)
       heapq.heappush(dic[rec.id],rec.score)
       if len(dic[rec.id]) > 5:
                heapq.heappop(dic[rec.id])
2. for loop in dic
   for id, score_list in dic.items():
        result[id] = sum(score_list)*1.0/len(score_list)

Complexity
___________
maintain a size 5 minheap
Time - O(NLog(5)) = O(N)
Space - O(Lg(5))+O(N) = O(N)
"""

 
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)

    def highFive(self, results):
        # Write your code here
        import heapq
        from collections import defaultdict
        dic = defaultdict(list)
        for rec in results:
            heapq.heappush(dic[rec.id], rec.score)
            if len(dic[rec.id]) > 5:
                heapq.heappop(dic[rec.id])

        result = {}

        for id, score_list in dic.items():

            result[id] = sum(score_list) * 1.0 / len(score_list)
        return result
