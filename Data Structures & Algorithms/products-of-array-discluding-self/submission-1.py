class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = 1
        # res = [1] * len(nums)
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
        # postfix = 1
        # for i in range(len(nums)-1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]

        # return res
        
        prod = 1
        zero_count = 0
        res = [0] * len(nums)
        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
        if zero_count > 1: return res

        for i, num in enumerate(nums):
            if zero_count: res[i] = 0 if num else prod
            else:
                res[i] = prod // num

        return res
 
        

             