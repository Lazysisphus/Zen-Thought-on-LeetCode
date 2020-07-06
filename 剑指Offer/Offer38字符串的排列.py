class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 递归实现
        # 时间复杂度O(n!)
        # 空间复杂度O(n^2)
        # 递归中的全局变量和局部变量总搞不清楚
        # 这道题中，结果保存变量res、字符串对应的列表char_list是全局变量
        # 前者需要不断append以保存全部可能的排列，后者则需要回溯来保证还原到上一层递归
        # 局部变量有递归的层数cur，在进入下一层递归前都会+1；有
        # 集合seen，保证在当前层的递归中，不会把相同的元素多次交换到cur的位置，起到剪枝作用
        char_list = list(s)
        res = []
        def dfs(cur):
            if cur == len(char_list)-1:
                res.append("".join(char_list))
                return
            seen = set()
            for i in range(cur, len(char_list)):
                if char_list[i] in seen:
                    continue
                seen.add(char_list[i])
                char_list[cur], char_list[i] = char_list[i], char_list[cur]
                dfs(cur+1)
                char_list[i], char_list[cur] = char_list[cur], char_list[i]

        dfs(0)
        return res