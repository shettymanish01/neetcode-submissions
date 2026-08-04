class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for i, num in enumerate(nums):
            if num in ref:
                return [ref[num], i]
            s = target - num
            ref[s] = i
