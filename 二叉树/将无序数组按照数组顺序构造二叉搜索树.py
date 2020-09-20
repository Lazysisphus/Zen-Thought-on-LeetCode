class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

nums = [-3, 0, 4, 8, 2, -5]

def BuildTree(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    for num in nums[1: ]:
        InsertNode(num, root)
    return root

def InsertNode(num, root):
    if not root:
        return TreeNode(num)
    elif num < root.val:
        root.left = InsertNode(num, root.left)
    else:
        root.right = InsertNode(num, root.right)
    return root

def levelOrderBottom(root):
    if not root:
        return []
    from collections import deque
    queue = deque([root])
    res = []
    while queue:
        n = len(queue)
        tmp = []
        for i in range(n):
            cur = queue.popleft()
            tmp.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        res.append(tmp)
    return res

root = BuildTree(nums)
print(levelOrderBottom(root))