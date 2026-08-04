class DSU:
    def __init__(self, n):
        self.components = n
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
        if self.size[pu] > self.size[pv]:
            pu, pv = pv, pu
        self.parent[pu] = pv
        self.size[pv] += self.size[pu]
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))

        for u, v in edges:
            if not dsu.union(u,v):
                return [u, v]
