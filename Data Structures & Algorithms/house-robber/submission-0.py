class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        store = defaultdict(int)
        def rob(h):
            first = 0
            second = 0
            if h >= n:
                return 0
            if h in store:
                return store[h]
            
            store[h] = max(rob(h+1),nums[h]+rob(h+2))
            return store[h]

        return rob(0)