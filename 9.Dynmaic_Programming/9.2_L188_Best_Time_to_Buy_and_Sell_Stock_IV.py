"""
Description
____________
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell
the stock before you buy again).


Approach
________________
DP + greedy
+++++++++++
DP[i][j] - max profit for using [:j+1] with i transactions permitted
- i as how many transactions allowed
- j as can use prices[: j+1], 0 means can use 0 index element

When k >= n/2, apply BTBS II

DP[i][j] = MAX(DP[i][j-1], prices[j] - prices[jj] + DP[i-1][jj-1]){jj <- 0 to j-1}
Now, to save iterations and sicne DP[i-1] does not change, we can maintain a local
         = Max(DP[i][j-1], prices[j] + max(DP[i-1][jj-1] - prices[jj]))
"""


class Solution(object):

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # DP[i][j] = MAX(DP[i][j-1], Prices[j] - Prices[jj] + DP[i-1][jj]) {jj <- 0 to j-1}
        #          = MAX(.........., Prices[j] + max(DP[i-1][jj] - prices[jj]))

        n = len(prices)
        if prices is None or n == 0:
            return 0
        if k is None or k == 0:
            return 0

        if k >= n / 2:
            max_profit = 0
            for i in xrange(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    max_profit += (prices[i] - prices[i - 1])
            return max_profit

        DP = [[0 for _ in xrange(n)] for i in xrange(k + 1)]
        for i in xrange(1, k + 1):
            tmp = DP[i - 1][0] - prices[0]
            for j in xrange(1, len(prices)):
                DP[i][j] = max(DP[i][j - 1], tmp + prices[j])
                tmp = max(DP[i - 1][j] - prices[j], tmp)
        return DP[k][n - 1]
