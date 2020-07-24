class Solution:
    def decodeString(self, s: str) -> str:
        # 栈
        # 启发：栈中元素不仅可以是数据单体，也可以是数据的组合
        # 本题难点：括号嵌套的情况
        # 算法描述，遍历字符串中的每个元素：
        #   使用 times 和 res 分别保存当前两个『[』之间的数字和字符串，
        #       因此，当遇到『[』的时候，要将当前 times 和 res 入栈，并将他们初始化已保存下一组嵌套的内容；
        #   遇到『]』则将当前 res 重复 times 次，然后再加上出栈得到的前一步的 res（注意加在前面）
        #   最后，只剩下遇到字符的情况，直接累加到 res 上
        # 时间复杂度O(n)，空间复杂度O(n)
        res, times = "", 0
        stack = []
        for ch in s:
            if ch in "0123456789":
                times = 10 * times + int(ch)
            elif ch == "[":
                stack.append([res, times])
                res = ""
                times = 0
            elif ch == "]":
                last_res, cur_times = stack.pop()
                res = last_res + res * cur_times
            else:
                res += ch
        return res