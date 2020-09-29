class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/solution/yi-tu-sheng-qian-yan-by-pianpianboy/
        # 搭建一个10叉树模型，在树上遍历
        # 或横向遍历，或纵向遍历
        def calNum(beg, end, n):
            num = 0
            while beg <= n:
                num += min(n + 1, end) - beg
                beg *= 10
                end *= 10
            return num

        cur = 1
        k -= 1
        while k:
            num = calNum(cur, cur + 1, n)
            if num <= k:
                k -= num
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur