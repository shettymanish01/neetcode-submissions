class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0 for i in range(len(text1)+1)]

        for i in range(len(text2)-1, -1, -1):
            # temp = dp
            prev = 0
            for j in range(len(text1)-1, -1, -1):
                temp = dp[j]
                if text1[j] == text2[i]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j+1], dp[j])
                prev = temp
            
        print(dp)

        return dp[0]