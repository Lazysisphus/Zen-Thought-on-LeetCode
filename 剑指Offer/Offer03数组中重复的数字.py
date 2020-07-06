# 好困啊，但是只能晚上做题 (；′⌒`)
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法1：哈希表，一次遍历，边存边找，时间和空间复杂度O(n)
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 0
            else:
                return num

        # 方法2：先排序，再查找，时间复杂度O(nlogn)，空间复杂度O(1)
        nums.sort()
        pre = nums[0]
        for i in range(1, len(nums)):
            if pre == nums[i]:
                return pre
            else:
                pre = nums[i]

        # 方法3：利用下标，一次遍历，时间复杂度O(n)，空间复杂度O(1)
        # 一个小细节：不要使用range(len(nums))，似乎在每次循环中都会计算长度
        n = len(nums)
        for i in range(n):
            cur_num = nums[i]
            while cur_num != i:
                if cur_num == nums[cur_num]:
                    return cur_num
                else:
                    # 这里不要写反了，cur_num的值需要第二个再改变
                    nums[cur_num], cur_num = cur_num, nums[cur_num]