class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        neg_diagonal = set()
        pos_diagonal =set()
        res = []
        board = [["."]*n for r in range(n)]

        def find_possibilities(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or r+c in pos_diagonal or r-c in neg_diagonal:
                    continue

                cols.add(c)
                pos_diagonal.add(r+c)
                neg_diagonal.add(r-c)
                board[r][c] = "Q"

                find_possibilities(r+1)

                cols.remove(c)
                pos_diagonal.remove(r+c)
                neg_diagonal.remove(r-c)
                board[r][c] = "."


        find_possibilities(0)
        return res

