class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 单调栈
        # 遍历温度列表
        #   如果目前栈空，当前元素的索引入栈
        #   否则，如果当前元素大于栈顶元素，获取当前元素与栈顶元素的索引差值，写入到创建记录表的对应位置，并将栈顶元素的索引出栈
        #        如果当前元素小于等于栈顶元素，当前元素的索引直接入栈
        # 时间复杂度O(n)，空间复杂度O(n)
        if not T:
            return []

        stack = []
        res = [0 for _ in range(len(T))]
        for idx, t in enumerate(T):
            if stack:
                while stack and t > T[stack[-1]]:
                    res[stack[-1]] = idx - stack[-1]
                    stack.pop()
            stack.append(idx)
        return res