class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #TC O(n) SC O(1)
        # maxP = 0
        # l, r = 0, 1
        # while r <len(prices):
        #     if prices[l] > prices[r]:
        #         l = r
        #     else:
        #         maxP = max(maxP, prices[r] - prices[l])

        #     r += 1

        # return maxP

        maxP = 0
        minBuy = prices[0]
        for price in prices:
            maxP = max(maxP, price - minBuy)
            minBuy = min(minBuy, price)

        return maxP