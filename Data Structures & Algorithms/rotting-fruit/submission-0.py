class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        res = float('inf')
        def addcell(r,c):
            if min(r, c) < 0 or r >= ROWS or c>= COLS or (r,c) in visited or grid[r][c]==0:
                return
            visited.add((r,c))
            q.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = -dist
                addcell(r+1, c)
                addcell(r-1, c)
                addcell(r, c+1)
                addcell(r, c-1)

            dist += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
                res = min(res, grid[r][c])

        return -1 * res
        