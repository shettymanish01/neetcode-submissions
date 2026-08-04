class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        cache[len(s)][len(p)] = True

        for r in range(len(s), -1, -1):
            for c in range(len(p)-1, -1, -1):
                match = r < len(s) and (s[r] == p[c] or p[c] == '.')
                if (c+1) < len(p) and p[c+1] == "*":
                    cache[r][c] = cache[r][c] or cache[r][c+2]
                    if match:
                        cache[r][c] = cache[r][c] or cache[r+1][c]
                elif match:
                    cache[r][c] = cache[r+1][c+1]

        return cache[0][0]
