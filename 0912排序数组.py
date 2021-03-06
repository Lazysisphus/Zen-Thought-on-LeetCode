class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.SelectSort(nums) # 选择排序，不能过
        return self.BubbleSort(nums) # 冒泡排序，不能过
        return self.InsertSort(nums) # 插入排序，不能过
        return self.ShellSort(nums)  # 希尔排序
        return self.MergeSort(nums)  # 归并排序
        return self.QuickSort(0, len(nums) - 1, nums) # 快速排序
        return self.HeapSort(nums)   # 堆排序

    def SelectSort(self, nums):
        """
        选择排序：
            从数组的无序部分（如后半部分）选择最小的数字，拼在有序数组（如数组的前半部分）后面
        时间复杂度O(n^2)
        不稳定(5, 8, 5, 2, 9)，内排序
        """
        n = len(nums)
        for i in range(n - 1):
            cur_idx = i
            for j in range(i + 1, n):
                if nums[cur_idx] > nums[j]:
                    cur_idx = j
            nums[i], nums[cur_idx] = nums[cur_idx], nums[i]
        return nums

    def BubbleSort(self, nums):
        """
        冒泡排序：
            进行 n - 1 次沉淀，每次沉淀从前到后进行
        时间复杂度O(n^2)
        稳定，内排序
        """
        n = len(nums)
        for i in range(n - 1): # 选择第 i 个元素进行沉淀
            flag = 0
            for j in range(1, n - i): # 每次沉淀扫描范围
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                    flag = 1
            if flag == 0: # 没有发生交换，提前结束排序
                return nums
        return nums

    def InsertSort(self, nums):
        """
        插入排序：
            从第二个元素开始和前面的元素进行比较
            如果前面的元素比当前元素大，则将前面元素后移，当前元素依次往前
            直到找到比它小或等于它的元素插入在其后面
        时间复杂度O(n^2)
        稳定，内排序
        """
        n = len(nums)
        for i in range(1, n):
            while i > 0 and nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                i -= 1
        return nums

    def ShellSort(self, nums):
        """
        希尔排序：
            最外层while循环，控制step
            中间for循环，类似插入排序，内层使用while实现元素交换
        时间复杂度，与增量序列有关，序列{1,2,4,...}的最坏时间复杂度为O(n^2)
        非稳定，内排序
        """
        n = len(nums)
        step = n // 2
        while step:
            for i in range(step, n):
                while i - step >= 0 and nums[i - step] > nums[i]:
                    nums[i - step], nums[i] = nums[i], nums[i - step]
                    i -= step
            step //= 2
        return nums
    
    def MergeSort(self, nums):
        """
        归并排序
        时间复杂度，O(nlogn)
        稳定，外排序，占用额外空间
        """
        def merge(nums1, nums2):
            i, j = 0, 0
            res = []
            while i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
            res += nums1[i: ]
            res += nums2[j: ]
            return res
        
        n = len(nums)
        if n <= 1:
            return nums
        mid = n // 2
        left = self.MergeSort(nums[: mid])
        right = self.MergeSort(nums[mid: ])
        return merge(left, right)

    def QuickSort(self, low, high, nums):
        """
        快速排序
        时间复杂度O(nlogn)
        不稳定，内排序
        """
        if low < high:
            mid = self.partition2(low, high, nums)
            self.QuickSort(low, mid - 1, nums)
            self.QuickSort(mid + 1, high, nums)
        return nums
        
    def partition1(self, low, high, nums):
        pivot = nums[high]
        i = low
        for j in range(low, high):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[high], nums[i] = nums[i], nums[high]
        return i

    def partition2(self, low, high, nums):
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high] # low的值已经保存在pivot中
            while low < high and nums[low] <= pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        return low

    def HeapSort(self, nums):
        """
        step1: 
            建堆：从最后一个非叶子结点开始，自下而上，从右向左调整，使数组满足堆的性质
        step2: 
            堆排序：进行n-1次操作，每次操作分两步进行
                    首先将堆顶和最末元素交换
                    然后调整除当前最末元素的数组，使其满足堆的性质
                    直至数组整体有序
        时间复杂度O(nlogn)
        不稳定，内排序
        """
        n = len(nums)
        for i in reversed(range(n // 2)):
            self.adjust_heap(nums, i, n)
        
        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.adjust_heap(nums, 0, i)
        return nums

    def adjust_heap(self, nums, startpos, endpos):
        """
        [startpos, endpos]为调整的范围
        对该范围内的元素调整，使它们满足堆的性质
        """
        pos = startpos
        childpos = pos * 2 + 1
        if childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and nums[rightpos] > nums[childpos]:
                childpos = rightpos
            if nums[childpos] > nums[pos]:
                nums[pos], nums[childpos] = nums[childpos], nums[pos]
                adjust_heap(nums, childpos, endpos)