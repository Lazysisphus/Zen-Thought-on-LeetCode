class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 数组在旋转后分为左半段和右半段
        # 然后二分查找的mid也将数组分为两段
        # 因此需要分别进行讨论，然后再缩小left和right区间的大小进行查找
        # 时间复杂度O(logn)
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            # 确定mid在数组的左半段还是右半段
            if nums[mid] >= nums[left]:
                # 确定target在mid左面还是右面
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return left if nums[left] == target else -1