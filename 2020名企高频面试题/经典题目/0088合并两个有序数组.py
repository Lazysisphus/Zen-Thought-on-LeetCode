class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 三指针，从后向前
        # 时间复杂度O(m+n)，空间复杂度O(1)
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0: # 仍有需要比较的元素
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        # 当 p2 此时仍大于0，说明需要将 p2 头部复制到 p1 头部
        nums1[: p2 + 1] = nums2[: p2 + 1]
        return nums1