class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 单调队列，维护队首元素总是当前窗口中最大的元素
        # 思路：
        #   单调队列保证了队首元素总是当前窗口中的最大元素，因此
        #   1.若队首元素 deque[0] == 当前移出窗口元素 nums[i-k]，则队首元素从队首出队；
        #   2.若当前进入窗口元素大于队尾元素，那么将队尾元素
        #       一直从队尾弹出，直到当前加入窗口元素小于队首元素，或直到队空，
        #       然后加入该元素到队列，从而保证队列的单调不严格递减；
        #   3.在考虑完成上面两步之后，如果当前形成了窗口，则将队首元素加入到res中
        # 时间复杂度O(n)，空间复杂度O(k)
        if not nums:
            return []
        
        n = len(nums)
        res = []
        from collections import deque
        queue = deque()
        for i in range(k): # 第一阶段，没有形成窗口，i指向窗口最末的元素
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
        res.append(queue[0]) # 第一阶段的最后一个状态形成了窗口，添加对应的对大元素到结果中
        for i in range(k, n): # 第二阶段，每次循环都会形成一个窗口
            if nums[i-k] == queue[0]: # 如果当前窗口中第一个元素是最大的元素（最大元素位于队首）
                queue.popleft() # 从队首弹出元素
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            res.append(queue[0])
        return res