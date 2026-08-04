class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i, prev):
            if i == len(nums):
                return 0
            # if i in dp:
            #     return dp[i]
            
            
            dp[i] = dfs(i+1, prev)
            if nums[i] > prev:
                dp[i] = max(dp[i], 1 + dfs(i+1, nums[i]))

            return dp[i]

        return dfs(0, float('-inf'))
