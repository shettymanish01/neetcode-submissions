class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append([p, d])
        print(adj)
        q = deque([[0,src]])
        cnt = 0
        res = float("inf")
        while q and cnt <= k+1:
            for i in range(len(q)):

                c, node = q.popleft()
                print(c , node, res)

                if node == dst:
                    print(n)
                    res = min(res, c)
                    continue

                for neic, nein in adj[node]:
                    q.append([c+neic, nein])

            cnt += 1

        return res if res != float("inf") else -1
                
        

       