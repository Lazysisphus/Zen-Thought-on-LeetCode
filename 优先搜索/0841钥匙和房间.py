class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # bfs
        from collections import deque
        queue = deque([0])
        seen = set([0])
        while queue:
            idx = queue.popleft()
            for nei in rooms[idx]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append(nei)
        return len(seen) == len(rooms)

        # dfs
        # 栈实现
        seen = set([0])
        stack = [0]
        while stack:
            idx = stack.pop()
            for nei in rooms[idx]:
                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)
        return len(seen) == len(rooms)

        # 递归实现
        def dfs(idx):
            seen.add(idx)
            for nei in rooms[idx]:
                if nei not in seen:
                    dfs(nei)

        seen = set()
        dfs(0)
        return len(seen) == len(rooms)