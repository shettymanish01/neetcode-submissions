class Solution:
    def climbStairs(self, n: int) -> int:
        store = {}
        def dfs(pos):
            if pos == n:
                return 1
            if pos > n:
                return 0
            if pos in store:
                return store[pos]
            
            store[pos] = dfs(pos+2) + dfs(pos+1)
            return store[pos]

        dfs(0)
        return store[0]