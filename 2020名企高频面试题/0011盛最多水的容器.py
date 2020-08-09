class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 双指针 - 左右指针，两个指针向中间移动
        # 每次取较短的那个木板作为高度，取两个木板的距离作为宽度，计算当前面积
        # 保存出现过的最大面积，即为ans
        # 时间复杂度O(n)，空间复杂度O(1)
        ans = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                ans  = max(ans, (right - left) * height[left])
                left += 1
            else:
                ans = max(ans, (right - left) * height[right])
                right -= 1
        return ans