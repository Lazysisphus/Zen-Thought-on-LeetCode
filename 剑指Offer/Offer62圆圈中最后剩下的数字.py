class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # 约瑟夫环问题
        # 其实还需要说明一个条件，就是删除一个元素之后
        # 以删除的该元素后面的第一个元素为新的第0号元素，来得到要删除的第m个元素
        # 开始有n个元素，最后一轮剩下2个，因此从2个元素补回到n个元素，需要逆向进行n-1轮
        # 时间复杂度O(n)，空间复杂度O(1)
        pos = 0 # 最后剩下的元素的索引
        for i in range(2, n+1):
            pos = (pos + m) % i
        return pos