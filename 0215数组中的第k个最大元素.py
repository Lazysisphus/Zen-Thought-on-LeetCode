class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)

        target = size - k
        low = 0
        high = size - 1
        while True:
            mid = self.partition(nums, low, high)
            if mid == target:
                return nums[mid]
            elif mid < target:
                left = mid + 1
            else:
                right = mid - 1

    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low
        # 想法其实很简单
        # 就是扫描一遍下标从low到high-1的全部数字
        # 把小于pivot的都换到i目前所指的位置，然后i递增
        # 最后i的位置就是pivot应该在的位置，进行交换
        for j in range(low, high):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[high], nums[i] = nums[i], nums[high]
        return i