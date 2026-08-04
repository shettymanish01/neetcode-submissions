# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         resSum = 0
#         res = float('-inf')
#         for i, num in enumerate(nums):
#             resSum = max(resSum + num, num)
#             res = max(res, resSum)
#         return res
            
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        resSum = 0
        res = float('-inf')
        startInd, endInd = 0, 0
        resInd = [0,0]
        for i, num in enumerate(nums):
            resSum = resSum + num
            if resSum < num:
                resSum = num
                startInd = i
            endInd = i
            if resSum > res:
                res = resSum
                resInd = [startInd, endInd]
        print(resInd)
        return res