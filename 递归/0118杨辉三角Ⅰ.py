class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 练习递归
        def helper(numRows):
            if numRows == 0:
                return []
            if numRows == 1:
                return [1]
            pre_layer = helper(numRows - 1)
            cur_layer = [1] + [pre_layer[i - 1] + pre_layer[i] for i in range(1, numRows - 1)] + [1]
            if numRows == 2:
                res.append(pre_layer)
            res.append(cur_layer)
            return cur_layer

        res = []
        helper(numRows)
        return res