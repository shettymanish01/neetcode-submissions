class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.nex, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node()
        self.right = Node()
        self.left.nex, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nex = node.prev, node.nex
        prev.nex = nex
        nex.prev = prev

    def insert(self, node):
        prev, nex = self.right.prev, self.right
        node.prev, node.nex = prev, nex
        prev.nex = nex.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.nex
            self.remove(lru)
            del self.cache[lru.key]
