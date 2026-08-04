class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m+n != len(s3):
            return False

        dp = [False for i in range(n+1)]
        dp[n] = True

        for i in range(m, -1, -1):
            nextDP = True if i==m else False
            for j in range(n, -1, -1):
                res = False if j < n else nextDP
                if i < m and s1[i] == s3[i+j] and dp[j]:
                    res = True
                if j < n and s2[j] == s3[i+j] and nextDP:
                    res = True
                dp[j] = res
                nextDP = dp[j]
        
        return dp[0]