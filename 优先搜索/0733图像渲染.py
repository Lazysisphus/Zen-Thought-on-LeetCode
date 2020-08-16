class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # bfs
        if newColor == image[sr][sc]: # 这个有点坑，新颜色和旧颜色可相同 = =
            return image
        row, col = len(image), len(image[0]) 
        from collections import deque
        queue = deque([[sr, sc]])
        rawColor = image[sr][sc]
        image[sr][sc] = newColor
        while queue:
            x, y = queue.pop()
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= x + dx < row and 0 <= y + dy < col and image[x + dx][y + dy] == rawColor:
                    queue.append([x + dx, y + dy])
                    image[x + dx][y + dy] = newColor
        return image

        # dfs
        def helper(x, y):
            if x < 0 or x >= row or y < 0 or y >= col or image[x][y] != oldColor:
                return 
            image[x][y] = newColor
            for nx, ny in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:
                helper(nx, ny)

        oldColor = image[sr][sc]
        if newColor == oldColor:
            return image
        row, col = len(image), len(image[0])
        helper(sr, sc)
        return image