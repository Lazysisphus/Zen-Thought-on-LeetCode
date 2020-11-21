"""
题目：不修改数组找出重复的数字

在一个长度为 n+1 的数组里的所有数字都在 1~n 的范围内，所以数组中至少有一个数字是重复的。
请找出数组中任意一个重复的数字，但不能修改输入的数组。
例如，如果输入长度为 8 的数组 {2,3,5,4,3,2,6,7}，那么对应的输出是重复的数字 2 或者 3 。
"""

nums = [2, 5, 4, 3, 2, 6, 7, 1]

# 方法1
# 遍历数组，同时使用一个哈希表保存遍历到的数字
#   如果当前数字不存在于哈希表中，那么将其保存在哈希表中，并遍历下一个数字
#   如果当前数字已经存在于哈希表中，那么它就是重复的数字
# 时间复杂度 O(n)，空间复杂度 O(n)

def method1(nums):
    hash_map = {}
    for num in nums:
        if num in hash_map:
            return num
        else:
            hash_map[num] = 0

# print(method1(nums))

# 方法2
# 二分法，对区间进行二分，每次二分后，统计区间内数字在 nums 中出现次数
# 如果出现次数大于区间内不同数字的个数，那么该区间有数字在 nums 中是重复出现的
# 时间复杂度 O(nlogn)，空间复杂度 O(1)

def count_helper(nums, beg, end):
    cnt = 0
    for num in nums:
        if num >= beg and num <= end:
            cnt += 1
    return cnt


def method2(nums):
    beg, end = 1, len(nums) - 1 # beg、end是区间的起点和终点，不是数组的第一个元素和最后一个元素
    while beg <= end:
        mid = beg + (end - beg) // 2
        cnt = count_helper(nums, beg, mid)
        if beg == end:
            if cnt > 1:
                return beg
            else:
                break # 没有重复的数字，退出循环
        if cnt > mid - beg + 1:
            end = mid
        else:
            beg = mid + 1
    return -1

# print(method2(nums))