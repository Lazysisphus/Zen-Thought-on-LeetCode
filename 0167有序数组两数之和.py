class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 方法1：哈希表，一次遍历
        n = len(numbers)
        if n == 0 or n < 2:
            return []
        
        hash_map = {}
        for idx, num1 in enumerate(numbers):
            num2 = target - num1
            if num2 in hash_map:
                return [hash_map[num2]+1, idx+1]
            hash_map[num1] = idx
        return []

        # 方法2：双指针
        # 如果数组原本无序，且题目要求返回元素的下标，那么不能将数组排序后使用双指针
        # 因为会破坏数组中各个元素的原本下标
        n = len(numbers)
        if n == 0 or n < 2:
            return []
        
        left = 0
        right = n-1
        while left < right:
            tmp = numbers[left] + numbers[right]
            if tmp < target:
                left += 1
            elif tmp > target:
                right -= 1
            else:
                return [left+1, right+1]
        return []
        