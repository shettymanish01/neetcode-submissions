class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        def dfs(i, buy):
            if i >= n:
                return 0
            if (i,buy) in dp:
                return dp[(i,buy)]
            c = dfs(i+1, buy)
            if buy:
                b = dfs(i+1, not buy) - prices[i]
                dp[(i,buy)] = max(b,c)
            else:
                s = dfs(i+2, not buy) + prices[i]
                dp[(i,buy)] = max(s,c)

            return dp[(i,buy)]

        return dfs(0, True)
