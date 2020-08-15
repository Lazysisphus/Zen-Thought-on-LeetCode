class Solution:
    # 很需要耐心的一道题目
    # 把数字三个为一组划分
    def numberToWords(self, num):
        def part(num):
            ans = ""
            if num >= 100:
                ans += d1[num // 100] + " Hundred"
                num %= 100
            if num >= 20:
                if ans:
                    ans += " "
                ans += d2[num // 10]
                num %= 10
            if num != 0:
                if ans:
                    ans += " "
                ans += d1[num]
            return ans

        d1 = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
              "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        d2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if num < 20:
            return d1[num]
        array=[0, 0, 0, 0]
        i = 3
        while i >= 0:
            array[i] = num % 1000
            num = num // 1000
            i -= 1
        
        res = ""
        i = 0
        while i <= 3:
            tmp = ""
            if array[i] != 0:
                tmp = part(array[i])
            else:
                i += 1
                continue
            if i == 0:
                res += tmp + " Billion"
            elif i == 1:
                if res:
                    res += " "
                res += tmp + " Million"
            elif i == 2:
                if res:
                    res += " "
                res += tmp + " Thousand"
            else:
                if res:
                    res += " "
                res += tmp
            i += 1
        return res