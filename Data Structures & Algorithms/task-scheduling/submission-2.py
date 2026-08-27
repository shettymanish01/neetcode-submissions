class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        time = 0
        q = deque()
        maxHeap= [-1 *val for val in count.values()]
        heapq.heapify(maxHeap)

        while maxHeap or q:
            time += 1
            if maxHeap:
                task = heapq.heappop(maxHeap) + 1
                if task:
                    q.append([task, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])

        return time

                