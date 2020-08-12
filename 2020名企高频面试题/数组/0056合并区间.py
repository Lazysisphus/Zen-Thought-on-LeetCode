class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先将区间按照起始点进行排序
        # 然后将第一个区间作为当前需要合并的区间，并和后面的第一个区间进行比较
        # 如果上述两个区间有重合，即后面第一个区间的起始点<=第一个区间的结束点，那么合并
        #   合并之后的区间作为当前需要合并的区间，继续和后面的区间作比较
        # 如果上述两个区间没有重合，那么将后面的第一个区间作为当前需要合并的区间，继续合并
        # 时间复杂度O(n)，空间复杂度O(n)
        res = []
        if not intervals:
            return res

        intervals.sort()
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        return res