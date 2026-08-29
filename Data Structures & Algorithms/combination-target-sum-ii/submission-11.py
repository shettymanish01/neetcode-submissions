class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = []
        # candidates.sort()

        # def generate_subsets(i, sub, total):
        #     if total == target:
        #         res.append(sub.copy())
        #         return
        #     if i >= len(candidates) or total > target:
        #         return
        #     sub.append(candidates[i])
        #     generate_subsets(i+1, sub, total + candidates[i])
        #     sub.pop()
        #     while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
        #         i += 1 
        #     generate_subsets(i+1, sub, total)

        # generate_subsets(0, [], 0)
        # return res

        self.count = Counter(candidates)
        self.nums = list(self.count.keys())
        self.res = []
        self.cur = []
        # self.nums = []
        # self.count = defaultdict(int)
        # for num in candidates:
        #     if self.count[num] == 0:
        #         self.nums.append(num)
        #     self.count[num] += 1
      

        self.generate_subsets(0, target)
        return self.res
        
    def generate_subsets(self, i, target):
        if target == 0:
            self.res.append(self.cur.copy())
            return
        if i >= len(self.nums) or target< 0:
            return

        if self.count[self.nums[i]] > 0:
            self.cur.append(self.nums[i])
            self.count[self.nums[i]] -= 1
            self.generate_subsets(i, target-self.nums[i])
            self.cur.pop()
            self.count[self.nums[i]] += 1
        self.generate_subsets(i+1, target)


            