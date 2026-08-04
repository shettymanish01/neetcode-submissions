class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[0] * (len(word2)+1) for i in range( len(word1)+1)]
        cache[-1][-1] = 0
        w1_len, w2_len = len(word1), len(word2)
        for i in range(w1_len):
            cache[i][-1] = w1_len - i
        for i in range(w2_len):
            cache[-1][i] = w2_len - i

        for i in range(w1_len - 1, -1, -1):
            for j in range(w2_len-1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j+1], cache[i+1][j], cache[i][j+1])

        return cache[0][0]