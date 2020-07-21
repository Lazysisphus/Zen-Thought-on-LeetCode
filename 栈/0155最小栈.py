class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.sort_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.sort_stack or x < self.sort_stack[-1]:
            self.sort_stack.append(x)
        else:
            self.sort_stack.append(self.sort_stack[-1])

    def pop(self) -> None:
        if not self.stack:
            return None
        else:
            self.stack.pop()
            self.sort_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None
        else:
            return self.sort_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()