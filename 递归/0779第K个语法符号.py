class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        # 找规律
        # 第 N 行的第 K 个数字可以由第 N-1 行的生成它的数字决定
        # 如果 K 是奇数，那么其在 N-1 行的对应数字为 (K + 1) // 2，且它与该数字相同
        # 如果 K 是偶数，那么其在 N-1 行的对应数字为 K // 2，且它与该数字相反（取反）
        if N == 1:
            return 0
        if K % 2 == 1:
            return self.kthGrammar(N - 1, (K + 1) // 2)
        else:
            return 1 - self.kthGrammar(N - 1, K // 2)