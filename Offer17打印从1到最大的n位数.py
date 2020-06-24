class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 方法1：循环实现
        # 时间复杂度O(10^n)
        # target = 10 ** n
        # res = []
        # for i in range(1, target):
        #     res.append(i)
        # return res

        # 方法2：递归+DFS实现全排列
        # 烦人，这道题每一次看都会花费很多时间
        def dfs(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0': 
                    res.append(int(s))
                if n - self.start == self.nine: 
                    self.start -= 1
                return
            for i in range(10):
                if i == 9: 
                    self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1
        
        num, res = ['0'] * n, []
        self.nine = 0
        self.start = n - 1
        dfs(0)
        return res