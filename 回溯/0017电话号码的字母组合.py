class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(i, tmp):
            if len(tmp) == n:
                res.append(tmp)
                return
            for j in range(len(phone[digits[i]])):
                backtrack(i + 1, tmp + phone[digits[i]][j])
        
        phone = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        n = len(digits)
        res = []
        if n == 0:
            return res
        backtrack(0, "")
        return res