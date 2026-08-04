class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-1 *n for n in nums]
        heapq.heapify(minHeap)

        res = 0
        while k > 0:
            res = heapq.heappop(minHeap)
            k -= 1

        return -1 * res