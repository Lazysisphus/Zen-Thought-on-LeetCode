# 早起一题 ( •̀ ω •́ )✧
class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        find = False
        if not matrix or not matrix[0]:
            return find
        
        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols - 1
        while row < rows and col >= 0:
            if target == matrix[row][col]:
                find = True
                break
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1

        return find