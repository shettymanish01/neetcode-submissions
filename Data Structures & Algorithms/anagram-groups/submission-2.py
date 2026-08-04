class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_list = defaultdict(list)
        for s in strs:
            count_s = Counter(s)
            res_list[frozenset(count_s.items())].append(s)
        print(res_list)
        return list(res_list.values())