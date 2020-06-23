class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 方法1：右移n，并和1做『与』操作
        # 当最高位表示符号，且n为负，可能会进入死循环
        # 但是这里可以通过
        count = 0
        while n:
            if n & 1:
                count += n & 1
            n >>= 1
        return count

        # 方法2：左移1，并和n做『与』操作
        flag = 1
        count = 0
        while flag <= n:
            if flag & n:
                count += 1
            flag <<= 1
        return count 

        # 方法3：小技巧
        # 把一个整数减去1，再和原来的整数做位与运算，通过这样
        # 的方式，可以依次把数字n最右侧的1置0
        count = 0
        while n:
            count += 1
            n = (n-1) & n
        return count