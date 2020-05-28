class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 方法1：使用哈希表，一次遍历，时间复杂度O(n)
        # 每次遍历将当前元素加入哈希表，并检查是否与哈希表中已有元素匹配
        # 重复元素的情况：[2,4,4,4,7]，target=8，输出[1,2]
        if not nums:
            return []

        hash_map = {}
        for idx, num1 in enumerate(nums):
            num2 = target - num1
            hash_map[num1] = idx
        
        return []

        # 方法2：两遍哈希表
        if not nums:
            return []

        hash_map = {}
        # 第一次遍历，将所有元素加入哈希表，考虑到了重复元素的情况
        for idx, num in enumerate(nums):
            if num not in hash_map:
                hash_map[num] = [idx]
            else:
                hash_map[num].append(idx)

        # 第二次遍历
        for idx, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in hash_map:
                if num1 != num2:
                    return [idx, hash_map[num2][0]]
                else:
                    if len(hash_map[num1]) > 1:
                        return [hash_map[num1][0], hash_map[num1][1]]
                    else:
                        continue
        return []