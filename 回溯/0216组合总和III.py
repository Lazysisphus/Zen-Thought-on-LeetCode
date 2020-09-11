class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(i, tmp_sum, tmp):
            if tmp_sum == target:
                res.append(tmp)
                return 
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                backtrack(j + 1, tmp_sum + candidates[j], tmp + [candidates[j]])
        backtrack(0, 0, [])
        
        return res