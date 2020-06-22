class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        # 方法1：从头到尾遍历数组，时间复杂度O(n)
        # 震惊，击败了双百用户，难道没人提交吗
        if not numbers:
            return

        min_num = numbers[0]
        for num in numbers:
            if num < min_num:
                min_num = num
        return min_num

        # 方法2：结合数组特点，二分查找，时间复杂度O(n)
        # 需要打两个布丁
        # 1.把原始数组前面的0个数字旋转到后面，即原始数组和新数组一样，如何处理
        # 2.出现左右指针指向的数字和中间的数字都相等，怎么处理
        if not numbers:
            return 

        n = len(numbers)
        left, right = 0, n-1
        mid = 0 # 处理情况1，初始让mid指向left
        while numbers[left] >= numbers[right]:
            if right - left == 1:
                mid = right
                break
            
            mid = left + (right - left)//2
            # 处理情况2，只能使用顺序查找
            if numbers[left] == numbers[right] and numbers[right] == numbers[mid]:
                min_num = numbers[0]
                for num in numbers:
                    if num < min_num:
                        min_num = num
                return min_num

            if numbers[mid] >= numbers[left]:
                left = mid
            if numbers[mid] <= numbers[right]:
                right = mid
        
        return numbers[mid]