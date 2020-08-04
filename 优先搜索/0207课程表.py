class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 使用拓扑图的思想，只有当前结点的所有前置结点被访问，才可访问当前结点
        # 1。初始化图结构，统计所有结点的 入度 和 相邻结点
        # 2。初始化队列，将当前入度为0的结点入队，
        # 3。进入循环，当队列非空，执行
        #       出队 -> 课程数-1 -> 遍历出队结点邻结点，入度-1，如果入度为0，入队
        # 时间复杂度O(m+n)，空间复杂度O(m+n)，m是邻边数量，n是结点数量
        from collections import deque
        indegrees = [0 for _ in range(numCourses)]
        neighbors = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            neighbors[pre].append(cur)
        queue = deque()
        for v, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(v)
        while queue:
            node = queue.popleft()
            numCourses -= 1
            for nei in neighbors[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        return numCourses == 0