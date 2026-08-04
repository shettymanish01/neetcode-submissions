class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = curMin = 1

        for n in nums:
            tmpMax = curMax
            curMax = max(n * tmpMax, n * curMin, n)
            curMin = min(n * tmpMax, n * curMin, n)
            res = max(res, curMax)

        return res