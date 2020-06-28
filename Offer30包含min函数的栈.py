class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = [] # 通用栈
        self.stack2 = [] # 最小栈


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        if not self.stack2:
            self.stack2.append(x)
        else:
            if x < self.stack2[-1]:
                self.stack2.append(x)
            else:
                self.stack2.append(self.stack2[-1])


    def pop(self):
        """
        :rtype: None
        """
        if not self.stack1:
            return None
        val = self.stack1.pop()
        min_val = self.stack2.pop()
        return val


    def top(self):
        """
        :rtype: int
        """
        if not self.stack1:
            return None
        return self.stack1[-1]


    def min(self):
        """
        :rtype: int
        """
        if not self.stack2:
            return None
        return self.stack2[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()