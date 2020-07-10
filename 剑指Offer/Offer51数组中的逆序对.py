class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 总体使用归并排序
        # 时间复杂度O(nlogn)，空间复杂度O(n)
        def mergeSort(nums, tmp, left, right):
            if left >= right: # 如果left等于或者越过了right，有0对逆序对
                return 0
            mid = left + (right - left) // 2 # 等分数组，分治排序
            # 将数组的左半部分和右半部分分别统计逆序对数目并排序
            rev_num = mergeSort(nums, tmp, left, mid) + mergeSort(nums, tmp, mid+1, right)
            i, j, pos = left, mid+1, left # 整合分治处理完成的左半部分和右半部分
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    tmp[pos] = nums[i]
                    i += 1
                    rev_num += (j - (mid+1))
                else:
                    tmp[pos] = nums[j]
                    j += 1
                pos += 1
            while i <= mid: # 如果右半部分数组已经全部进入tmp，而左半部分的数组没有遍历完
                tmp[pos] = nums[i] # 将左半部分数组的剩余部分全部放入tmp
                rev_num += (j - (mid+1)) # 并更新逆序对数目
                pos += 1
                i += 1
            while j <= right: # 同理，将右半部分数组放入到tmp中
                tmp[pos] = nums[j]
                pos += 1
                j += 1
            nums[left: right+1] = tmp[left: right+1] # 使用tmp对nums中left到right段做更新
            return rev_num # 返回该段的逆序对总数

        n = len(nums)
        tmp = [0 for _ in range(n)]
        return mergeSort(nums, tmp, 0, n-1)