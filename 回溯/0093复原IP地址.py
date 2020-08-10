class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 递归 + 回溯，难，多看回溯
        # 时间复杂度O(|s| * 3^4)，空间复杂度O(4)
        def backtrack(i, str_num, tmp):
            if i == n and str_num == 4:
                res.append(tmp[: -1])
                return 
            if str_num > 4:
                return 
            for j in range(i, i + 3):
                if j < n:
                    if j == i and s[j] == "0":
                        backtrack(j + 1, str_num + 1, tmp + s[j] + ".")
                        break
                    if 0 < int(s[i: j + 1]) <= 255:
                        backtrack(j + 1, str_num + 1, tmp + s[i: j + 1] + ".")

        res = []
        n = len(s)
        backtrack(0, 0, "")
        return res