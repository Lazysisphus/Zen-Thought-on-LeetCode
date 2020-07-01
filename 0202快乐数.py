class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 找规律，非快乐数最后都会塌陷进入一个死循环
        seen = set()
        while n != 1:
            n = sum([int(x)**2 for x in str(n)])
            if n not in seen:
                seen.add(n)
            else:
                return False
        return True