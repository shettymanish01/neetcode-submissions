class DSU:
    def __init__(self, n):
        self.components = n
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False
        
        self.components -= 1
        if self.size[pu] > self.size[pv]:
            pu, pv = pv, pu
        self.parent[pu] = pv
        self.size[pv] += pu
        return True
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u,v)

        return dsu.components