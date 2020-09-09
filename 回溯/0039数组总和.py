class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 回溯
        def backtrack(i, tmp_sum, tmp):
            if tmp_sum > target or i == n:
                return 
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                backtrack(j, tmp_sum + candidates[j], tmp + [candidates[j]])
            
        res = []
        n = len(candidates)
        candidates.sort()
        backtrack(0, 0, [])
        return res