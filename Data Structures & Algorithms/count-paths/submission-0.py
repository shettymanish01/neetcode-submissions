class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        dp[(m-1, n-1)] = 1
        cycle = set()
        def dfs(r,c):
            print(r,c)
            if r < 0 or c < 0 or r > m - 1 or c > n - 1 or (r,c) in cycle:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            cycle.add((r,c))

            dp[(r,c)] = dfs(r+1, c) + dfs(r, c+1)
            cycle.remove((r,c))
            return dp[(r,c)]

        
        return dfs(0, 0)