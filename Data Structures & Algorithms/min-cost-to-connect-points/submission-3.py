class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # n = len(points)
        # dist = [float('inf')] * n
        # edges = 0
        # node = 0
        # res = 0
        # visit = set()

        # while edges < n -1:
        #     visit.add(node)
        #     next_node = -1
        #     for i in range(n):
        #         if i in visit:
        #             continue
        #         cur_dist = (abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1]))
        #         dist[i] = min(cur_dist, dist[i])

        #         if next_node == -1 or dist[i] < dist[next_node]:
        #             next_node = i

        #     node = next_node
        #     res += dist[node]
        #     edges += 1

        # return res

        adj_map = defaultdict(list)
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = (abs(x1-x2) + abs(y1 - y2))
                adj_map[i].append([dist, j])
                adj_map[j].append([dist, i])

        minH = [[0, 0]]
        visit = set()
        res = 0
        while minH and len(visit) < n :
            cost, node = heapq.heappop(minH)
            if node in visit:
                continue
            res += cost
            visit.add(node)
            for nei_cost, nei in adj_map[node]:
                if nei not in visit:
                    heapq.heappush(minH, [nei_cost, nei])

        return res
