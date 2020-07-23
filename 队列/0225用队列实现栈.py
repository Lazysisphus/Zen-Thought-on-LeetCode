class MyStack:

    '''
    思路：
        两个队列来回倒腾
            在整个元素入栈和出栈的过程中，最多只有一个队列有元素
            在入栈的时候，将元素加入到非空的队列的末尾
            在出栈的时候，将非空队列中的元素依次出队并放入另一个队列中，直到队尾元素到达队首
                此时将该元素直接出队
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.q1 = deque()
        self.q2 = deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            return self.q1.popleft()
        else:
            while len(self.q2) > 1:
                self.q1.append(self.q2.popleft())
            return self.q2.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[-1] if self.q1 else self.q2[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1 and not self.q2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()