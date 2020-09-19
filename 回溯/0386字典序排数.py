'''
给定一个整数 n, 返回从 1 到 n 的字典顺序。

例如，

给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。

请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。
'''

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # 遍历过程，先遍历1，然后深度遍历10 * 1 + 1，然后10 * 10 + 1
        # 直到目前的值大于n，返回
        res = []

        def dfs(cur): 
            if cur > n: 
                return 
            res.append(cur)
            for i in range(10):
                dfs(10 * cur + i)

        for i in range(1,10):
            dfs(i)
        return res