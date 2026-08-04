class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)
        def dfs(i, cur):
            print(i,cur)
            if cur == target and i == n:
                print("1")
                return 1
            if i>=n:
                return 0

            if (i,cur) in dp:
                return dp[(i,cur)]

            dp[(i,cur)] = dfs(i+1, cur-nums[i]) + dfs(i+1, cur+nums[i])
            return dp[(i,cur)]


        return dfs(0,0)