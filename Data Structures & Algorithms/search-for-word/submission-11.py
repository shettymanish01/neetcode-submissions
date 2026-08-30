class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        visited = set()

        def found_word(i, j, cur_letter_index):
            if cur_letter_index == len(word):
                return True
            if i<0 or j<0 or i >= ROWS or j >= COLS or word[cur_letter_index] != board[i][j] or ((i, j) in visited):
                return False

            visited.add((i,j))
            nearby_cols = [[-1,0], [1,0], [0,-1], [0,1]]
            for x,y in nearby_cols:
                if found_word(i+x, j+y, cur_letter_index+1):
                    return True
            visited.remove((i,j))
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if found_word(i,j,0):
                    return True

        return False
                