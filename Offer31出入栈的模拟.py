class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # 思路清晰才不会慌，这道题的解法也很朴素，即
        # 用一个栈来模拟两个序列的产生过程
        # 根据入栈序列将元素入栈，每次入栈后判断栈顶元素是否需要出栈
        # 如果出入栈顺序无法模拟得到，那么返回False
        stack = [] # 辅助栈
        i = 0 # 当前出栈元素在序列中的索引
        for num in pushed:
            stack.append(num)
            while stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return not stack