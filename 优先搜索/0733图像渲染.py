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
            if image[x][y] == rawColor:
                image[x][y] = newColor
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    if 0 <= x + dx < row and 0 <= y + dy < col:
                        helper(x + dx, y + dy)

        rawColor = image[sr][sc]
        if newColor == rawColor:
            return image
        row, col = len(image), len(image[0])
        helper(sr, sc)
        return image