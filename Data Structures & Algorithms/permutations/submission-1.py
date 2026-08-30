class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # if len(nums) == 0:
        #     return [[]]
        
        # perms = self.permute(nums[1:])

        # res= []
        # for p in perms:
        #     for i in range(len(p)+1):
        #         perm_copy = p.copy()
        #         perm_copy.insert(i, nums[0])
        #         res.append(perm_copy)

        # return res

        self.res = []
        self.backtrack(0, nums)
        return self.res


    def backtrack(self, idx, nums):
        if idx == len(nums):
            self.res.append(nums[:])
            return

        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(idx+1, nums)
            nums[idx], nums[i] = nums[i], nums[idx]
                

        