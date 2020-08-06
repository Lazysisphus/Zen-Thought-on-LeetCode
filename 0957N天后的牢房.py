class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # 这是什么类型的题目...
        # 时间复杂度O(2^N)，周期包含的最大状态数是2^N个
        def nextday(cells):
            new_cells = [int(i > 0 and i < 7 and cells[i -1] == cells[i + 1]) for i in range(8)]
            return new_cells
        
        cycle = 0 # 使用cycle记录重复周期的状态数
        day_base = tuple(nextday(cells))
        cells = nextday(cells)
        N -= 1
        while N:
            day = tuple(nextday(cells))
            cells = nextday(cells)
            N -= 1
            cycle += 1
            if day == day_base:
                N = N % cycle
        return cells