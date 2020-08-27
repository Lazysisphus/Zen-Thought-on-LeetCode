class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 使用单调递增的栈实现
        # 对于当前出栈元素，其左侧第一个比它低的元素是其出站后的的栈顶元素
        # 其右侧第一个比它低的元素是for循环遍历中，当前遍历到的，使其进行出栈的元素（即i）
        ans = 0
        heights = [0] + heights + [0]
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                cur = stack.pop()
                left = stack[-1] + 1 # 闭区间[left, right]
                right = i - 1
                ans = max(ans, (right - left + 1) * heights[cur])
            stack.append(i)
        return ans