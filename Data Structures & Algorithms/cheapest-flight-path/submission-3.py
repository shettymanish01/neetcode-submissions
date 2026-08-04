class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # adj = defaultdict(list)
        # for s, d, p in flights:
        #     adj[s].append([p, d])
        # print(adj)
        # q = deque([[0,src]])
        # cnt = 0
        # res = float("inf")
        # while q and cnt <= k+1:
        #     for i in range(len(q)):

        #         c, node = q.popleft()
        #         print(c , node, res)

        #         if node == dst:
        #             print(n)
        #             res = min(res, c)
        #             continue

        #         for neic, nein in adj[node]:
        #             q.append([c+neic, nein])

        #     cnt += 1

        # return res if res != float("inf") else -1

        INF = float("inf")
        adj = [[] for _ in range(n)]
        dist = [[INF] * (k + 5) for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])

        dist[src][0] = 0
        minHeap = [(0, src, -1)] # cost, node, stops
        while len(minHeap):
            cst, node, stops = heapq.heappop(minHeap)
            if dst == node: return cst
            if stops == k or dist[node][stops + 1] < cst:
                continue
            for nei, w in adj[node]:
                nextCst = cst + w
                nextStops = 1 + stops
                # if dist[nei][nextStops + 1] > nextCst:
                #     dist[nei][nextStops + 1] = nextCst
                heapq.heappush(minHeap, (nextCst, nei, nextStops))

        return -1
                
        

       