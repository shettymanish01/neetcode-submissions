class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cur_chars = set()
        res = []
        prev = 0
        counts = {}
        for ch in s:
            counts[ch] = 1 + counts.get(ch,0)
        
        for i,ch in enumerate(s):
            cur_chars.add(ch)
            counts[ch] -= 1
            if counts[ch] == 0:
                cur_chars.remove(ch)
                if len(cur_chars) == 0:
                    res.append(i - prev + 1)
                    prev = i+1

        return res
