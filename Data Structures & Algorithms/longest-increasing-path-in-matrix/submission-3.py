class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        ROWS, COLS = len(matrix), len(matrix[0])
        res = 0
        def dfs(i, j, prev):
            if i >= ROWS or j >= COLS or i < 0 or j < 0 or matrix[i][j] <= prev:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            cur = matrix[i][j]
            dp[(i,j)] = 1+ max(dfs(i+1, j, cur), dfs(i-1, j, cur), dfs(i, j+1, cur), dfs(i, j-1, cur))
            # dirs = [(1, 0), (-1,0), (0,1), (0,-1)]
            # res = 0
            # for dr, dc in dirs:
            #     if matrix[i+dr][j+dc] > matrix[i][j]:
            #         cur = dfs(i+dr, j+dc)
            #         res = max(res, cur)
            # dp[(i,j)] = 1 + res
            return dp[(i,j)]

        for i in range(ROWS):
            for j in range(COLS):
                cur = dfs(i, j, -1)
                res = max(res, cur)

        return res


            