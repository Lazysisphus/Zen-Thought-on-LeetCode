class Solution:
    # 和0043字符串相乘类似
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        if l1 < l2:
            num1, num2 = num2, num1
            l1, l2 = l2, l1
        num1 = [int(x) for x in num1]
        num2 = [int(x) for x in num2]
        num1, num2 = num1[::-1], num2[::-1]
        for i, digit in enumerate(num2):
            num1[i] += num2[i]
        num1 = self.CarrySolver(num1)
        num1 = num1[::-1]
        return "".join(str(x) for x in num1)
    
    def CarrySolver(self, nums):  
        i = 0
        while i < len(nums):
            if nums[i] >= 10:
                carrier = nums[i] // 10
                if i == len(nums) - 1:
                    nums.append(carrier)
                else:
                    nums[i + 1] += carrier
                nums[i] %= 10
            i += 1
        return nums