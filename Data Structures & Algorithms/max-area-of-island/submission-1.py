class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        res = 0

        def dfs(r, c):
            nonlocal area
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c]==0:
                return 0

            area += 1
            grid[r][c] = 0
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
                    area = 0

        return res
