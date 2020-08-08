class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 时间复杂度O(n)，空间复杂度O(1)
        def check1(num):
            num = str(num)
            if len(num) == 1:
                return True
            if num == num[::-1]:
                return True
            return False

        def check2(num):
            flag = 0
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    flag = 1
                    break
            return flag == 0

        if N == 1:
            return 2
        while True:
            if check1(N) and check2(N):
                return N
            N += 1
            # 数学经验，在这个范围中没有质数
            # 所以统一按照10**8处理，而10**8不是回文数
            # 所以会加快速度
            if 10**7 < N < 10**8: 
                N = 10**8