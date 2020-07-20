class MyCircularQueue(object):
    # 队列使用固定大小的列表实现
    # 队列的头指针指向队列中的第一个元素
    # 队列没有设置尾指针，通过(head_idx + count - 1) % capacity可以获得队列的最后一个元素的索引
    # 设计了单独的计数变量count来判断队列的空和满
    # 时间复杂度O(1)，空间复杂度O(1)
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [0] * k
        self.head_idx = 0
        self.count = 0
        self.capacity = k
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.count == self.capacity:
            return False
        self.queue[(self.head_idx + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.count == 0:
            return False
        self.head_idx = (self.head_idx + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.count == 0:
            return -1
        return self.queue[self.head_idx]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.count == 0:
            return -1
        return self.queue[(self.head_idx + self.count - 1) % self.capacity]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.count == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.count == self.capacity
    

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()