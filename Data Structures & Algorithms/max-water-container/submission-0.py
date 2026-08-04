class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights) - 1
        max_water = 0
        while l < r:
            cur_max = min(heights[l], heights[r]) * (r - l)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

            max_water = max(cur_max, max_water)

        return max_water