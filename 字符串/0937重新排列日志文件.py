class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 学习如何使用sort函数根据两个条件来排序
        l1, l2 = [], []
        for l in logs:
            if l[-1].isdigit():
                l2.append(l)
            else:
                l1.append(l)
        l1.sort(key=lambda x: (x[x.index(" ") + 1: ], x[: x.index(" ")]))
        return l1 + l2