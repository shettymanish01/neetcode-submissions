class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = {}
        for i,num in enumerate(nums):
            required = target-num
            if required in target_map:
                return [target_map[required], i]
            else:
                target_map[num] = i
