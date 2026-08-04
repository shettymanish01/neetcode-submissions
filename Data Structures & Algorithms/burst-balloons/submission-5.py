# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         nums = [1] + nums + [1]
#         dp = {}

#         def dfs(l, r):
#             if l > r:
#                 return 0
#             if (l,r) in dp:
#                 return dp[(l,r)]

#             dp[(l,r)] = 0
#             for i in range(l, r+1):
#                 coins = nums[l-1] * nums[i] * nums[r+1]
#                 coins += dfs(l,i-1) + dfs(i+1, r)
#                 dp[(l,r)] = max(dp[(l,r)], coins)
#             return dp[(l,r)]

        
#         return dfs(1, len(nums)-2)

class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        new_nums = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n]
