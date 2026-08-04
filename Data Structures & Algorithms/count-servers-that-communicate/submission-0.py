class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = [0 for i in range(len(grid))]
        col = [0 for i in range(len(grid[0]))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row[i] +=  1
                    col[j] += 1

        print(row)
        print(col)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (row[i] >= 2 or col[j] >= 2):
                    res += 1

        return res