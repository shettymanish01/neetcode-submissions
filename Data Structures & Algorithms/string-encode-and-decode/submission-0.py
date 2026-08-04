class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s))+"#"+s for s in strs])
    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        res = []
        while i < len(s):
            if s[i] == "#":
                word_len = int(s[j:i])
                j = i+1+word_len
                res.append(s[i+1:j])
                i = j
            else:
                i += 1

        return res