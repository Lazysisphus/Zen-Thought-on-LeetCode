class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # bfs
        if not matrix or not matrix[0]:
            return 
        
        from collections import deque
        queue = deque()
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col): # 将问题转化为：0到各个非0元素的距离
                if matrix[i][j] == 0:
                    queue.append([i, j])
                else:
                    matrix[i][j] = None
        while queue: # 本质上是一层一层遍历图或者树
            x, y = queue.popleft() # 注意要popleft!
            for nx, ny in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] == None:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append([nx, ny])
        return matrix