class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def a_circle(start):
            x_end = col - start - 1
            y_end = row - start - 1
            for j in range(start, x_end + 1):
                res.append(matrix[start][j])
            
            if y_end > start:
                for i in range(start + 1, y_end + 1):
                    res.append(matrix[i][x_end])
            
            if y_end > start and x_end > start:
                for j in range(x_end - 1, start - 1, -1):
                    res.append(matrix[y_end][j])
            
            if y_end - 1 > start and x_end > start:
                for i in range(y_end - 1, start, -1):
                    res.append(matrix[i][start]) 
        
        if not matrix or not matrix[0]:
            return []
        row = len(matrix)
        col = len(matrix[0])
        start = 0
        res = []
        while start * 2 < row and start * 2 < col:
            a_circle(start)
            start += 1
        return res