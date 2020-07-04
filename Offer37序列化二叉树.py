# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # 解释参考题解区K姓大佬
    # 依照题目样例，应使用层序方法遍历二叉树，进行序列化和反序列化
    # 相比样例答案，该题解会打印多余的“null”，不过重点在序列化，而且样例的答案也比较反常
    # 这里注意返回值是字符串类型，挺别扭的
    # 序列化：时间复杂度O(n)，空间复杂度O(n)
    # 反序列化：时间复杂度O(n)，空间复杂度O(n)
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        
        from collections import deque
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        ans = "[" + ",".join(res) + "]"
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None
        
        vals = data[1:-1].split(",")
        i = 1
        from collections import deque
        queue = deque()
        root = TreeNode(vals[0])
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(vals[i])
                queue.append(node.left)
            i += 1 # 不管当前序列的值是否为“null”，都需要+1
            if vals[i] != "null":
                node.right = TreeNode(vals[i])
                queue.append(node.right)
            i += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))