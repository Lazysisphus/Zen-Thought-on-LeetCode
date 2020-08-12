# 使用双向链表 + 哈希表实现
# 双向链表中，每个结点都有指向前驱和后继的指针
# 此题中，每个结点保存一个key，一个value，可以看作一个结构体
# 为方便操作，增加一个伪头结点head和伪尾结点tail
# hash表中保存key-value对
# 两个函数的时间复杂度都是O(1)
# 空间复杂度O(capacity)
class DeLinkNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hash_map = {}
        self.head = DeLinkNode()
        self.tail = DeLinkNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        else:
            node = self.hash_map[key]
            self.moveToHead(node)
            return node.value
            
    def put(self, key: int, value: int) -> None:
        if key not in self.hash_map:
            node = DeLinkNode(key, value)
            self.hash_map[key] = node
            self.size += 1
            self.addToHead(node)
            if self.size > self.capacity:
                removed = self.removeTail()
                self.hash_map.pop(removed.key) # 字典中使用pop删除
                self.size -= 1
        else:
            node = self.hash_map[key]
            node.value = value
            self.moveToHead(node)
    
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
    
    def addToHead(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.pre = node
    
    def moveToHead(self, node):
        self.remove(node)
        self.addToHead(node)
    
    def removeTail(self):
        node = self.tail.pre
        self.remove(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)