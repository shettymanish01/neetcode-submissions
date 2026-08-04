class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        tickets.sort()

        for s, d in tickets:
            adj[s].append(d)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                res.append(v)
                adj[src].pop(i)

                if dfs(v):
                    return True
                res.pop()
                adj[src].insert(i, v)

            return False

        if dfs("JFK"):
            return res