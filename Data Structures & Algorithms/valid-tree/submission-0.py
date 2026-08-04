class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        visiting = set()
        hashmap = {i : [ ] for i in range(n)}
        for s, d in edges:
            hashmap[s].append(d)
            hashmap[d].append(s)

        def dfs(node, par):
            if node in visiting:
                return False
            # if node in visited:
            #     return True
            visiting.add(node)
            for nei in hashmap[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False

            # visiting.remove(node)
            # visited.add(node)

            return True

        return dfs(0, -1) and len(visiting) == n