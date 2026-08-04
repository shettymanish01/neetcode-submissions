class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l, r = 0, len(nums) - 1
        # res = nums[0]

        # while l <= r:
        #     if nums[l] <= nums[r]:
        #         res = min(res,nums[l])
        #         break

        #     mid = l + (r - l) // 2
        #     res = min(res, nums[mid])
        #     if nums[mid] >= nums[l]:
        #         l = mid + 1
        #     else:
        #         r = mid - 1

        # return res

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]