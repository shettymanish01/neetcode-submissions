class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i, prev):
            if i == len(nums):
                return 0
            if (i,prev) in dp:
                return dp[(i,prev)]
            
            
            dp[(i, prev)] = dfs(i+1, prev)
            if nums[i] > prev:
                dp[(i, prev)] = max(dp[(i, prev)], 1 + dfs(i+1, nums[i]))

            return dp[(i,prev)]

        return dfs(0, float('-inf'))
