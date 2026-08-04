class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        dp = {}
        def dfs(i, cur_sum):
            if i >= n:
                return 0
            if cur_sum > amount:
                return 0
            if cur_sum == amount:
                return 1
            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]
            
            dp[(i, cur_sum)] = dfs(i, cur_sum+coins[i])  + dfs(i+1, cur_sum)

            return dp[(i, cur_sum)]

        return dfs(0, 0)