class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        dp = set()
        dp.add(0)

        for num in nums:
            nextDP = set()
            for t in dp:
                if t+num == target:
                    return True
                nextDP.add(t)
                nextDP.add(t+num)
            dp = nextDP
        return False
            


