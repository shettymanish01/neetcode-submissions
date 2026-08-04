class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')] * n
        edges = 0
        node = 0
        res = 0
        visit = set()

        while edges < n -1:
            visit.add(node)
            next_node = -1
            for i in range(n):
                if i in visit:
                    continue
                cur_dist = (abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1]))
                dist[i] = min(cur_dist, dist[i])

                if next_node == -1 or dist[i] < dist[next_node]:
                    next_node = i

            node = next_node
            res += dist[node]
            edges += 1

        return res