class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxR = [0] * len(height)
        cur_maxL = 0
        cur_maxR = 0
        total = 0
        for i in range(1, len(height)):
            maxL[i] = cur_maxL = max(cur_maxL, height[i-1])
        print(maxL)


        for i in range(len(height)-2, -1, -1):
            maxR[i] = cur_maxR = max(cur_maxR, height[i+1])
        print(maxR)

        for i in range(len(height)):
            total = total + max(0,(min(maxL[i], maxR[i]) - height[i]))

        return total