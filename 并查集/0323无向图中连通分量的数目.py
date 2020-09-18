'''
给定编号从 0 到 n-1 的 n 个节点和一个无向边列表（每条边都是一对节点），请编写一个函数来计算无向图中连通分量的数目。

示例 1:

输入: n = 5 和 edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

输出: 2
示例 2:

输入: n = 5 和 edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

输出:  1
注意:
你可以假设在 edges 中不会出现重复的边。而且由于所以的边都是无向边，[0, 1] 与 [1, 0]  相同，所以它们不会同时在 edges 中出现。
'''


from collections import Counter
class UF:
    def __init__(self, n):
        self.uf = [-1] * n

    def find(self, idx):
        if self.uf[idx] == -1:
            return idx
        return self.find(self.uf[idx])
    
    def union(self, idx1, idx2):
        f1 = self.find(idx1)
        f2 = self.find(idx2)
        if f1 != f2: 
            self.uf[f2] = f1

    def result(self):
        return Counter(self.uf)[-1] # 每个连通分量最终指向-1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        return uf.result()