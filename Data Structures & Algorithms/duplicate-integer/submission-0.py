class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_counter = {}
        for num in nums:
           nums_counter[num] = nums_counter.get(num,0) + 1

        return len(nums_counter) != len(nums)