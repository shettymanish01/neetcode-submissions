class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t < "":
            return ""

        couS, couT = {},{}
        for i in range(len(t)):
            couT[t[i]] = couT.get(t[i], 0) + 1
            # couS[s[i]] = couS.get(s[i], 0) + 1

        matches = 0
        # for c in t:
        #     if c in couS and couT[c] == couS[c]:
        #         matches += 1
        need = len(couT)
        res_len = float('infinity')
        res = [-1, -1]
        l = 0
        print(matches, need)
        for r in range(len(s)):
            
            couS[s[r]] = couS.get(s[r], 0) + 1
            if s[r] in couT and couT[s[r]] == couS[s[r]]:
                matches += 1

            while matches == need:
                if (r - l+1) < res_len:
                    
                    res_len = r - l + 1
                    res = [l, r]
                    print(res_len, res)

                couS[s[l]] -= 1
                if s[l] in couT and couT[s[l]] > couS[s[l]]:
                    matches -= 1
                l += 1

        l, r = res
        return s[l : r+1] if res_len != float('infinity') else ""
