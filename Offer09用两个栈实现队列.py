class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value):
        self.stack1.append(value)


    # 对两个栈的状态要做判断
    def deleteHead(self):
        # 两个栈都空，队列空
        if not self.stack1 and not self.stack2:
            return -1
        
        if self.stack2:
            val = self.stack2.pop()
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            val = self.stack2.pop()
        return val



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
