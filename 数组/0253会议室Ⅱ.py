给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)
为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1:

输入: [[0, 30],[5, 10],[15, 20]]
输出: 2
示例 2:

输入: [[7,10],[2,4]]
输出: 1

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 将所有会议的开始和结束时间按照从早到晚排序
        # 设置一个变量cur，遍历所有时间
        # 如果遇到开始时间，那么cur+1，如果遇到结束时间，那么cur-1
        # 使用ans记录cur出现过的最大值
        # 时间复杂度O(nlogn)，为排序所用的时间
        ans = 0
        cur = 0
        events = [(iv[0], 1) for iv in intervals] + [(iv[1], -1) for iv in intervals]
        events.sort()
        for e, v in events:
            cur += v
            ans = max(ans, cur)
        return ans