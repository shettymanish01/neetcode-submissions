class Solution:
    def trap(self, height: List[int]) -> int:
        #TC : O(n) SC : O(n)

        # maxL = [0] * len(height)
        # maxR = [0] * len(height)
        # cur_maxL = 0
        # cur_maxR = 0
        # total = 0
        # for i in range(1, len(height)):
        #     maxL[i] = cur_maxL = max(cur_maxL, height[i-1])

        # for i in range(len(height)-2, -1, -1):
        #     maxR[i] = cur_maxR = max(cur_maxR, height[i+1])

        # for i in range(len(height)):
        #     total = total + max(0,(min(maxL[i], maxR[i]) - height[i]))

        # return total

        l ,r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        res = 0
        while l < r:
            if l_max < r_max:
                l += 1
                res = res + max(0, l_max - height[l])
                l_max = max(l_max, height[l])
            else:
                r -= 1
                res = res + max(0, r_max - height[r])
                r_max = max(r_max, height[r])

        return res


