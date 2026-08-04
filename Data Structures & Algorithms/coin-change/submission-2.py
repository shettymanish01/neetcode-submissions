class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [amount+1] * (amount+1)
        # dp[0] = 0
        # for a in range(1, amount+1):
        #     for c in coins:
        #         if (a - c) < 0:
        #             continue
        #         dp[a] = min(dp[a], 1+dp[a-c])
        # return dp[amount] if dp[amount] != (amount+1) else -1

        if amount == 0:
            return 0   
        q = deque([0])
        res = 0
        seen = set()
        while q:
            res += 1
            for _ in range(len(q)):
                a = q.popleft()
                for c in coins:
                    nxt = a+c
                    if nxt == amount:
                        return res
                    if nxt > amount or nxt in seen:
                        continue
                    seen.add(nxt)
                    q.append(nxt)

        return -1
