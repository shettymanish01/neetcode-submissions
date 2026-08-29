class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def generate_subsets(i, sub, total):
            if total == target:
                res.append(sub.copy())
                return
            if i >= len(candidates) or total > target:
                return
            sub.append(candidates[i])
            generate_subsets(i+1, sub, total + candidates[i])
            sub.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1 
            generate_subsets(i+1, sub, total)

        generate_subsets(0, [], 0)
        return res

            