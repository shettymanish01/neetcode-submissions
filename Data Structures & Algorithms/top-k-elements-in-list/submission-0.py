class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            counter[num]+= 1
        for num, f in counter.items():
            freq[f].append(num)
        

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
