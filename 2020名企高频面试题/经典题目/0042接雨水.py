class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        # 第一次遍历，找到最高的柱子
        # 如果最高的柱子有多个，取索引最小的那个
        max_h, max_idx = 0, 0
        for idx, h in enumerate(height):
            if h > max_h:
                max_h = h
                max_idx = idx
        
        n = len(height)
        left, right = 0, n - 1
        max_left, max_right = 0, 0
        ans = 0
        # 从左向右遍历，记录『当前最高柱高』和『当前柱高』之差，累加起来
        while left <= max_idx:
            if height[left] > max_left:
                max_left = height[left]
            ans += max_left - height[left]
            left += 1
        # 从右向左遍历，同理累加
        while right >= max_idx:
            if height[right] > max_right:
                max_right = height[right]
            ans += max_right - height[right]
            right -= 1
        return ans