class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-1 * s for s in stones]
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            s1 = -1 * heapq.heappop(minHeap)
            s2 = -1 * heapq.heappop(minHeap)

            if s1 == s2:
                continue
            elif s1 < s2:
                heapq.heappush(minHeap,-1 * (s2 - s1))
            else:
                heapq.heappush(minHeap, -1 * (s1 - s2))

        return -1 * minHeap[0] if minHeap else 0