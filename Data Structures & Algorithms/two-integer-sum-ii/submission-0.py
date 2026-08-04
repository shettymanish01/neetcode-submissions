class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum_map = {}

        for i, num in enumerate(numbers):
            rem = target - num
            if rem in sum_map:
                return [sum_map[rem], i + 1]
            else:
                sum_map[num] = i + 1
