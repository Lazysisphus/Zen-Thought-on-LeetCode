class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 感觉没有当初学的时候那么难了
        # 明白了，好像计算逆波兰式的值不复杂，构造逆波兰式比较复杂
        # 创建空斩，遍历逆波兰式中的每个元素
        #   如果当前元素是符号，那么将栈中倒数两个元素出栈，并将计算结果再压入栈中
        #   如果当前元素是数字，那么将该元素直接压入栈中
        stack = []
        if not tokens:
            return 0
        
        n = len(tokens)
        for i in range(n):
            if tokens[i] in "+-*/":
                num1 = stack.pop()
                num2 = stack.pop()
                res = str(int(eval(num2 + tokens[i] + num1)))
                stack.append(res)
            else:
                stack.append(tokens[i])
        return int(stack[0])