class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # space = O(1)(limited chars i.e 26), Time= O(m+n)
        # count_s = {}
        # count_t = {}
        # len_s = len(s)
        # len_t = len(t)
        # if len_s != len_t:
        #     return False
        # for i in range(len_s):
        #     count_s[s[i]] = count_s.get(s[i],0) + 1
        #     count_t[t[i]] = count_t.get(t[i],0) + 1

        # return count_s == count_t

        count_arr = [0] * 26
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        for i in range(len_s):
            count_arr[ord(s[i]) - ord("a")] += 1
            count_arr[ord(t[i]) - ord("a")] -= 1

        for val in count_arr:
            if val != 0:
                return False
        return True
