class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if isPali(s, i, j+1):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()

        def isPali(s, i, j):
            rev = s[i:j][::-1]

            print(s[i:j], s[i:j][::-1], rev)
            if s[i:j] == rev:
                return True
            return False

        # def isPali(s, l, r):
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l, r = l + 1, r - 1
        #     return True

        dfs(0)
        return res