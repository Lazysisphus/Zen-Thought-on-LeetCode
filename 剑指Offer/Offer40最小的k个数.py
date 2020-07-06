class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 方法1：使用自带排序，时间复杂度O(ologn)，是一种称为timesort的排序方法
        arr.sort()
        return arr[:k]

        # 方法2：使用快速排序中的partition找到数组第k小的数
        # 时间复杂度O(n)
        def partition(arr, low, high):
            pivot = arr[low]
            while low < high:
                while low < high and arr[high] >= pivot:
                    high -= 1
                arr[low] = arr[high]
                while low < high and arr[low] <= pivot:
                    low += 1
                arr[high] = arr[low]
            arr[low] = pivot
            return low

        if not arr or k <= 0:
            return [] 
        low = 0
        high = len(arr) - 1
        index = partition(arr, low, high)
        while index != k-1:
            if index > k-1:
                high = index - 1
                index = partition(arr, low, high)
            if index < k-1:
                low = index + 1
                index = partition(arr, low, high)
        return arr[:k]