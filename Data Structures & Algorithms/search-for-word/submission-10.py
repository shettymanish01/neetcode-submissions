class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        def isMatch(i, j, index):
            if index == len(word):
                return True
            if (i < 0 or j < 0 or i >= row or j >= col or word[index] != board[i][j] or visited[i][j]):
                return False
                
            visited[i][j] = True
            combs = [(i-1,j), (i+1, j), (i, j-1), (i, j+1)]
            for x, y in combs:
                if isMatch(x, y, index+1):
                    return True
            visited[i][j] = False
                

            return False

        for i in range(row):
            for j in range(col):
                if isMatch(i, j, 0):
                    return True

        return False