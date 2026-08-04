class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        r = 0
        maxf = 0
        while r < len(s):
            count[s[r]] = count.get(s[r],0) + 1
            maxf = max(count[s[r]], maxf)

            if ((r - l + 1) - maxf ) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1 , res)
            r += 1

        return res

                