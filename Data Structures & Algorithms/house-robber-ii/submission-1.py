class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        store = {}


        def dfs(h, flag):
            if h >= n or (flag and h==n-1):
                return 0
            if (h, flag) in store:
                return store[(h, flag)]

            store[(h, flag)] = max(dfs(h+1, flag), dfs(h+2, flag)+nums[h])
            return store[(h, flag)]

        return max(dfs(0, True), dfs(1, False))