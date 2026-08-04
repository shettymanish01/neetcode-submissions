class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, s, i, j):
        node = self.root
        for idx in range(i, j+1):
            if s[idx] not in node.children:
                return False
            node = node.children[s[idx]]
        return node.is_word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp = {}
        # words = set(wordDict)
        # def dfs(i):
        #     if i == len(s):
        #         return True
        #     if i in dp:
        #         return dp[i]
        #     for word in words:
        #         n = len(word)
        #         if s[i:i+n] == word:
        #             if dfs(i+n):
        #                 dp[i] = True
        #                 return True
        #     dp[i] = False
        #     return False

        # return dfs(0)

        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        t= max([len(word) for word in wordDict])
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, min(len(s), i+t)):
                if trie.search(s, i, j):
                    dp[i] = dp[j+1]
                    if dp[i]:
                        break
        return dp[0]


        

            