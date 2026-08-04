class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 1
        res = 1
        if s == "":
            return 0
        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
                res = max(res, r-l)
            else:
                while s[r] != s[l]:
                    l += 1
                l += 1
                r += 1

        return res

