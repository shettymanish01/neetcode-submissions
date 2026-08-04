class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i, prev):
            if i == len(nums):
                return 0
            if (i,prev) in dp:
                return dp[(i,prev)]
            
            include = 0
            if nums[i] > prev:
                include = 1 + dfs(i+1, nums[i])
            exclude = dfs(i+1, prev)

            dp[(i, prev)] = max(include, exclude)
            return dp[(i,prev)]

        return dfs(0, float('-inf'))
