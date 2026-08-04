class DSU:
    def __init__(self, n):
        self.cmps = n
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False
        self.cmps -= 1
        if self.size[pu] > self.size[pv]:
            pu, pv = pv, pu
        self.parent[pu] = pv
        self.size[pv] += self.size[pu]
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # visited = set()
        # visiting = set()
        # hashmap = {i : [ ] for i in range(n)}
        # for s, d in edges:
        #     hashmap[s].append(d)
        #     hashmap[d].append(s)

        # def dfs(node, par):
        #     if node in visiting:
        #         return False
        #     # if node in visited:
        #     #     return True
        #     visiting.add(node)
        #     for nei in hashmap[node]:
        #         if nei == par:
        #             continue
        #         if not dfs(nei, node):
        #             return False

        #     # visiting.remove(node)
        #     # visited.add(node)

        #     return True

        # return dfs(0, -1) and len(visiting) == n
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False

        return dsu.cmps == 1 