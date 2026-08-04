class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        store = {}
        n = len(cost)
        def dfs(floor):
            first = 0
            second = 0
            if floor >= n:
                return 0
            if floor in store:
                return store[floor]

            first = dfs(floor+1)
            second = dfs(floor+2)

            store[floor] = cost[floor] + min(first, second)
            return store[floor]

        return min(dfs(0), dfs(1))