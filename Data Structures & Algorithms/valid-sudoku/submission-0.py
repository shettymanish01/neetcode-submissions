class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for c in range(9):
            for r in range(9):
                char = board[r][c]
                if char == ".":
                    continue
                if char in row[r] or char in col[c] or char in box[(r//3,c//3)]:
                    return False

                row[r].add(char)
                col[c].add(char)
                box[(r//3,c//3)].add(char)

        return True