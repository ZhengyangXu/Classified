"""
Description
___________
Given n books and the ith book has A[i] pages. You are given k people to copy the n books.
n books list in a row and each person can claim a continous range of the n books.
For example one copier can copy the books from ith to jth continously,
but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).
They start copying books at the same time and they all cost 1 minute to copy 1 page of a book.
 What's the best strategy to assign books so that the slowest copier can finish at earliest time?

Example
Given array A = [3,2,4], k = 2.
Return 5( First person spends 5 minutes to copy book 1 and book 2 and second person spends 4 minutes to copy book 3. )
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

    # #     DP approach + Prefix Sum
        # prefix_sum = []
        # prefix_sum.append(pages[0])
        # for i in xrange(1,len(pages)):
        #     prefix_sum.append(prefix_sum[i-1] + pages[i])
    #     m = len(pages)
    #     dic = [[0 for _ in xrange(k)] for _ in xrange(m)]
    #     # print prefix_sum
    #     for i in xrange(m):
    #         for j in xrange(k):
    #             if i == 0:
    #                 dic[i][j] = pages[0]
    #             elif j==0:
    #                 dic[i][j] = prefix_sum[i]
    #             else:
    #                 minimum = sys.maxint
    #                 for p in xrange(i):
    #                     minimum = min(minimum, max(dic[p][j-1],prefix_sum[i]-prefix_sum[p]))
    #                 # print minimum, i,j
    #                 # print dic
    #                 dic[i][j] = minimum

    #     # print dic
    #     return dic[m-1][k-1]

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
