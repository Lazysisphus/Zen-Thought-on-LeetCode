class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        # 方法1：从完整的后序遍历序列开始递归
        # 每层递归中，序列的最后一个数字是根节点
        # 然后通过比较大小，将根节点以外的其他结点划分为左右子树
        # 时间复杂度O(n^2)，空间复杂度O(n)
        def helper(left, right):
            if right <= left:
                return True
            cur = left
            while postorder[cur] < postorder[right]:
                cur += 1
            mid = cur
            while postorder[cur] > postorder[right]:
                cur += 1
            return cur == right and helper(left, mid-1) and helper(mid, right-1)
        return helper(0, len(postorder)-1)

        # 方法2：单调栈+后序遍历倒序
        # 每次都找到剩下的序列中，不能超过的最大值，如果序列中的元素超过该最大值，则不是平衡搜索树
        # 这个方法太难想到了，而且也不好理解，以后再看看
        # 时间复杂度O(n)，空间复杂度O(n)
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: 
                return False
            while stack and postorder[i] < stack[-1]:
                root = stack.pop()
            stack.append(postorder[i])
        return True