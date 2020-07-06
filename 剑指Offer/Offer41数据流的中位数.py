class MedianFinder(object):
    # 方法1：数字插入无序数组+快速排序
    # 时间复杂度O(1)+O(n)
    
    # 方法2：插入排序+索引获得中位数
    # 时间复杂度O(n)+O(1)

    # 方法3：使用最大堆和最小堆
    # 思路：使用最小堆A和最大堆B分别存储数据流较大的一半和较小的一半
    # 动态添加元素的过程需要保证len(A)-len(B)<=1
    # 当len(A) == len(B)时，将下个元素添加A中
    # 当len(A) ！= len(B)时，说明A比B多一个元素，将下个元素添加到B中
    # 在向堆A中添加元素时，新元素需要先入堆B，再从B中出堆得到符合要求的元素
    # 在向堆B中添加元素时同理
    # 出入堆时间复杂度O(logn)，查找中位数时间复杂度O(1)
    # 另外要学习python中堆的实现，数据结构使用列表
    # 出入堆的方法有heappop()、heappush()、heappushpop()
    # python只有定义好的最小堆，最大堆通过对出入堆的元素取负来实现
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.B = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.A) == len(self.B):
            heappush(self.A, -heappushpop(self.B, -num))
        else:
            heappush(self.B, -heappushpop(self.A, num))

    def findMedian(self):
        """
        :rtype: float
        """
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0]-self.B[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()