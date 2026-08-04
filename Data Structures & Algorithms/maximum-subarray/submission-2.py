class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        resSum = 0
        res = float('-inf')
        for i, num in enumerate(nums):
            resSum = max(resSum + num, num)
            res = max(res, resSum)
        return res
            
