class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 双指针
        # 时间复杂度O(n)，空间复杂度O(1)
        i = 1 # 滑动窗口的左边界
        j = 1 # 滑动窗口的右边界
        cur_sum = 0 # 滑动窗口中数字的和
        res = []

        while i <= target // 2:
            if cur_sum < target:
                # 右边界向右移动
                cur_sum += j
                j += 1
            elif cur_sum > target:
                # 左边界向右移动
                cur_sum -= i
                i += 1
            else:
                # 记录结果
                arr = list(range(i, j))
                res.append(arr)
                # 左边界向右移动
                cur_sum -= i
                i += 1
        return res