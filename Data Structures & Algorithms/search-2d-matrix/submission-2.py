class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = len(matrix), len(matrix[0])

        l, r = 0, row - 1
        def binary_search(nums, target):
            l,r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r-l) // 2
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    return True

            return False
                

        while l <= r:
            mid_row = l + (r-l) // 2
            print(mid_row)
            if target < matrix[mid_row][0]:
                r = mid_row - 1
            elif target > matrix[mid_row][-1]:
                l = mid_row + 1
            else:
                if binary_search(matrix[mid_row], target):
                    return True
                else:
                    return False

        return False
