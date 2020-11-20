"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

 

限制：

0 <= n <= 1000

0 <= m <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 早起一题 ( •̀ ω •́ )✧

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 方法1
        # 利用矩阵的顺序性质，从右上角开始排除行和列
        # 比较当前矩阵右上角的元素和目标元素的大小，分三种情况：
        #   如果右上角元素 等于 目标元素，返回True
        #   如果右上角元素 小于 目标元素，说明目标元素不在当前行，row+1
        #   如果右上角元素 大于 目标元素，说明目标元素不在当前列，col-1
        # 时间复杂度O(rows+cols)，空间复杂度O(1)
        flag = False
        if not matrix or not matrix[0]:
            return flag
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                flag = True
                break
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return flag