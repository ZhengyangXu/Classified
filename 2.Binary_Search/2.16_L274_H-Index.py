"""
Description
______________
Given an array of citations (each citation is a non-negative integer) of a researcher
write a function to compute the researcher's h-index.
According to the definition of h-index on Wikipedia:
"A scientist has index h if h of his/her N papers have at least h citations each
and the other N − h papers have no more than h citations each."
For example, given citations = [3, 0, 6, 1, 5], which means the researcher
has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively
Since the researcher has 3 papers with at
least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Approach
________________
Smart-ass Bucket Sort
++++++++++++++++++++++
1. establish n buckets
   - bucket i represents i references, value represents the count
   - value in bucket n represnets the count of references >= n
2. Walk backwards for the buckets and maintain a count += value
   - when count is larger or equal to i
     we return i

"""


class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        buckets = [0 for _ in xrange(n + 1)]
        for c in citations:
            if c >= len(citations):
                buckets[n] += 1
            else:
                buckets[c] += 1

        count = 0
        print buckets
        for i in range(n, -1, -1):
            print i, count
            count += buckets[i]
            print 'after', i, count
            if count >= i:
                return i
        return 0
