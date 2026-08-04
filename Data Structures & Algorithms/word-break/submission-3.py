class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in dp:
                return dp[i]
            for word in wordDict:
                n = len(word)
                if s[i:i+n] == word:
                    if dfs(i+n):
                        dp[i] = True
                        return True
            dp[i] = False
            return False

        return dfs(0)