'''
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

 

示例 1：

输入：
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出：2 
解释：已知学生 0 和学生 1 互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回 2 。
示例 2：

输入：
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出：1
解释：已知学生 0 和学生 1 互为朋友，学生 1 和学生 2 互为朋友，所以学生 0 和学生 2 也是朋友，所以他们三个在一个朋友圈，返回 1 。
'''

'''
方法1：
    利用类似岛屿数量的解法
    每次dfs，假设入口坐标为 (i, j)，那么需要遍历第 i 行的每一列
    遍历中，如果有坐标 (i, ny) 的值为 1，那么将其置零，并深度遍历 ny 列对应的行
'''
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1 or M[i][j] == 0:
                return
            for ny in range(cols):
                if M[i][ny] == 1:
                    M[i][ny] = 0
                    dfs(ny, i)

        if not M or not M[0]:
            return 0
        
        ans, rows, cols = 0, len(M), len(M[0])
        for i in range(rows):
            for j in range(cols):
                if M[i][j] == 1:
                    ans += 1
                    dfs(i, j)
        return ans

'''
方法2：
    并查集
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
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        
        edges = []
        n = len(M)
        for j in range(1, n):
            for i in range(j):
                if M[i][j] == 1:
                    edges.append([i, j])
        print(edges)

        uf = UF(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        return uf.result()