class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        window = {}
        count_t = {}

        for c in t:
            count_t[c] = 1 + count_t.get(c,0)

        res = [-1, -1]
        res_len = float('inf')
        have, need = 0, len(count_t)
        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)

            if ch in count_t and window[ch] == count_t[ch]:
                have += 1
            
            while have == need:
                if (r-l+1) < res_len:
                    res = [l, r]
                    res_len = r-l+1

                window[s[l]] -= 1
                if s[l] in count_t and count_t[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""

