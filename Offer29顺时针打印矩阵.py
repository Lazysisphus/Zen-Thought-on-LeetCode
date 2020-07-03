class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 字节跳动2021秋招提前批有问到，不过写出来了
        if not matrix or not matrix[0]:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        res = []
        while start*2 < rows and start*2 < cols:
            endx = cols - 1 - start
            endy = rows - 1 - start
            # →
            for i in range(start, endx+1):
                res.append(matrix[start][i])
            
            # ↓
            if endy > start:
                for i in range(start+1, endy+1):
                    res.append(matrix[i][endx])
            
            # ←
            if endx > start and endy > start:
                for i in range(endx-1, start-1, -1):
                    res.append(matrix[endy][i])
            
            # ↑
            if endx > start and endy-1 > start:
                for j in range(endy-1, start, -1):
                    res.append(matrix[j][start])

            start += 1
        return res