class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 练习递归
        if rowIndex == 0:
            return [1]
        pre = self.getRow(rowIndex - 1)
        cur = [1] + [pre[i - 1] + pre[i] for i in range(1, rowIndex)] + [1]
        return cur