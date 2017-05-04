"""
Description
________________
Given n books and the ith book has A[i] pages. You are given k people to copy the n books.
n books list in a row and each person can claim a continous range of the n books.
For example one copier can copy the books from ith to jth continously,
but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).
They start copying books at the same time and they all cost 1 minute to copy 1 page of a book.
 What's the best strategy to assign books so that the slowest copier can finish at earliest time?

Example
_______________
Given array A = [3,2,4], k = 2.
Return 5( First person spends 5 minutes
to copy book 1 and book 2 and second person spends 4 minutes to copy book 3. )

Approach
__________
Let's first abatract this problem to another identicial problem
parition array of integers to minimize the maximum subarray to k partitions

Dynamic Programming
+++++++++++++++++++++
A[0..i] - the first i ints (including i)
prefix_sum - prefix_sum of A
Dp [i][j] - the minimum of the maximum subarray for A[0..i] under j partitions

DP[i][j] = for k<-0 to i min( max(DP[k][j-1],prefix_sum[i]-prefix_sum[k]))

Binary search
+++++++++++++++
Constraint: Number of partitions paritions(mid) <= k
(mid represents the maximum (sum) subarray)
Goal: find the first position (smallest) maximum subarray that satisefy the constraint
range: max(A) to sum(A)

only complication is to calculate k from current maximum subarray


    def getRequiredCopiers(self, pages, max_page_per_person):
        copiers = 1
        sum = 0
        for i in pages:
            sum += i
            if sum > max_page_per_person:
                copiers += 1
                sum = i
        return copiers
"""


class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer

    # Here, we present two possible solutions.
    # Dyamic Programming (Extra Space)
    # BInary Search
    # import sys
    def copyBooks(self, pages, k):
        if len(pages) == 0:
            return 0
    # #     write your code here
        import sys
        prefix_sum = pages[:]
        for i in xrange(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i] + prefix_sum[i - 1]
        m = len(pages)
        DP = [[0 for _ in xrange(m)] for _ in xrange(k)]
        # let 0,0 in DP stand for 1 person, with book 1
        for k_i in xrange(k):
            for p_i in xrange(m):
                if k_i == 0:
                    DP[k_i][p_i] = prefix_sum[p_i]

                elif p_i == 0:
                    DP[k_i][p_i] = prefix_sum[0]
                else:
                    minimum = sys.maxint
                    for p_j in xrange(p_i + 1):
                        minimum = min(minimum, max(DP[k_i - 1][p_j], prefix_sum[p_i] - prefix_sum[p_j]))
                    DP[k_i][p_i] = minimum

        return DP[k - 1][m - 1]
 
#-----------------------------------------------------------------------
        # Binary Search
        # Constraint rquired requireCopiers <= k
        # Find first position of range ( max (pages), sum(pages) )

        start = max(pages)
        end = sum(pages)
        while start + 1 < end:
            mid = start + (end - start) / 2
            copiers = self.getRequiredCopiers(pages, mid)
            if copiers <= k:
                end = mid
            else:
                start = mid
        # print self.getRequiredCopiers(pages,start), start
        if (self.getRequiredCopiers(pages, start) <= k):

            return start
        return end

    def getRequiredCopiers(self, pages, max_page_per_person):
        copiers = 1
        sum = 0
        for i in pages:
            sum += i
            if sum > max_page_per_person:
                copiers += 1
                sum = i
        return copiers
