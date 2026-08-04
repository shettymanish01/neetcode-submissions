class Solution:
    def numDecodings(self, s: str) -> int:
        # dp = {len(s):1}

        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if s[i] == "0":
        #         return 0

        #     dp[i] = dfs(i+1)
        #     if (i+1) < len(s) and int(s[i:i+2]) <= 26:
        #         dp[i] += dfs(i+2)
            
        #     return dp[i]

        # return dfs(0)

        dp = dp2 = 0
        dp1 = 1

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp = 0
            else:
                dp = dp1
            
            if (i+1) < len(s) and (s[i] != "0" and int(s[i:i+2]) <= 26):
                dp += dp2
            
            dp, dp1, dp2 = 0, dp, dp1

        return dp1
            