class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l = r = 0
        # cur_set = set()
        # res = 0
        # while r < len(s):
        #     if s[r] not in cur_set:
        #         cur_set.add(s[r])
        #         print("Hi", cur_set)
        #         res = max(res, len(cur_set))
        #     else:
        #         while True:
        #             print(s[l], s[r])
        #             if s[l] == s[r]:
        #                 cur_set.remove(s[l])
        #                 l += 1
        #                 break
        #             else:
        #                 cur_set.remove(s[l])
        #                 l += 1

        #         cur_set.add(s[r])
        #         print("hey", cur_set)
        #     r += 1
            

        # return res

        res = 0
        l = 0
        char_map = {}
        for r, ch in enumerate(s):
            if ch in char_map:
                l = max(char_map[ch]+1, l)
            char_map[ch] = r
            res = max(r-l+1, res)

        return res