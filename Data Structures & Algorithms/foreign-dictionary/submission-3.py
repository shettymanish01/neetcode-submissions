class Solution:
    def foreignDictionary(self, words):
        adj = {c:set() for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            w1_len, w2_len = len(w1), len(w2)
            min_len = min(w1_len, w2_len)
            if w1_len > w2_len and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []
        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True
            for nei in adj[char]:
                if dfs(nei):
                    return True

            visited[char] = False
            res.append(char)


        for c in list(adj.keys()):
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)