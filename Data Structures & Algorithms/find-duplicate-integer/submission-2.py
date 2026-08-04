class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        print(slow, fast)

        slow2 = 0

        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow