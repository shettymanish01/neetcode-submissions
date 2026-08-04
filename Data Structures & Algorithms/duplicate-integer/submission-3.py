class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums_counter = {}
        # for num in nums:
        #    nums_counter[num] = nums_counter.get(num,0) + 1

        # return len(nums_counter) != len(nums)


        return len(set(nums)) < len(nums)


        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False  #This is best because it does not have to loop through all elements. If it finds duplicate number early it will stop immediately. If not i.e worst case it has to loop through all.