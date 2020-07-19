class MovingAverage:
    # 窗口移动可以分为两个阶段
    # 第一个是开始阶段，没有形成size大小的窗口，窗口中元素的数目小于size
    # 第二个阶段中每一步都会形成窗口
    # 通过一个累计量count计算目前遇到过的元素数目，进而判断是否形成了size大小的窗口
    # 时间复杂度O(1)，空间复杂度O(n)
    def __init__(self, size: int):
        from collections import deque
        self.size = size
        self.count = 0 # number of elements seen so far
        self.queue = deque()
        self.window_sum = 0
        
    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        if self.count > self.size:
            del_num = self.queue.popleft()
            self.window_sum = self.window_sum - del_num + val
        else:
            self.window_sum = self.window_sum + val
        return self.window_sum / min(self.size, self.count)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)