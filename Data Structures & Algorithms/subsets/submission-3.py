class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # res = []
        # for i in range(1 << n):
        #     subset = [nums[j] for j in range(n) if (i & (1 << j))]
        #     res.append(subset)

        # return res

        # res = [[]]
        # for num in nums:
        #     res += [sub + [num] for sub in res]

        # return res

        res= []
        def dfs(i, sub):
            if i >= len(nums):
                res.append(sub)
                return

            dfs(i+1, sub + [nums[i]])
            dfs(i+1, sub)

        dfs(0,[])
        return res