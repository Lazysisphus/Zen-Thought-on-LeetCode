"""
993. 二叉树的堂兄弟节点
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。

 

示例 1：


输入：root = [1,2,3,4], x = 4, y = 3
输出：false
示例 2：


输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true
示例 3：



输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false
 

提示：

二叉树的节点数介于 2 到 100 之间。
每个节点的值都是唯一的、范围为 1 到 100 的整数。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # 深度优先搜索，时间复杂度O(n)，空间复杂度O(n)
        # 注意两种特殊情况：找不到查找值，以及查找值在根节点（它没有父节点）
        def helper(root, fa, depth, val):
            if not root:
                return [-1, -1] # 查不到查找值，节点值和深度都返回-1
            if root.val == val:
                if not fa:
                    return [1, depth] # 1表示查找值在根节点（这道题似乎默认根节点的值为1）
                else:
                    return [fa.val, depth]
            left = helper(root.left, root, depth+1, val)
            if left[0] != -1:
                return left
            right = helper(root.right, root, depth+1, val)
            return right
        
        l1 = helper(root, None, 0, x)
        l2 = helper(root, None, 0, y)
        return l1[0] != l2[0] and l1[1] == l2[1]