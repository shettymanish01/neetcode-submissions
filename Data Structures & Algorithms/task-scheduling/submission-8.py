class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count = Counter(tasks)
        # time = 0
        # q = deque()
        # maxHeap= [-1 *val for val in count.values()]
        # heapq.heapify(maxHeap)

        # while maxHeap or q:
        #     time += 1
        #     if not maxHeap:
        #         time = q[0][1]
        #     else:
        #         task = heapq.heappop(maxHeap) + 1
        #         if task:
        #             q.append([task, time+n])
        #     if q and q[0][1] == time:
        #         heapq.heappush(maxHeap,q.popleft()[0])

        # return time
        
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord("A")] += 1

        count.sort()
        maxf = count[25]
        idle = (maxf - 1) * n

        for i in range(24, -1, -1):
            if count[i] == maxf:
                idle -= count[i]-1 #if both frequencies are equal it can't sit in between the idle time of the other task hence it requires one extra space at the end.
            else:
                idle -= count[i]
            # idle -= min(maxf-1, count[i])

        return max(0, idle) + len(tasks)



                