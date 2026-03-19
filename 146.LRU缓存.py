class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add(self, node):
        nxt = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = nxt
        nxt.prev = node

    def _remove(self, node):
        p = node.prev
        n = node.next

        p.next = n
        n.prev = p
    
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self._remove(node)
        self._add(node)

        return node.val
    
    def put(self, key: int, value: int) -> None:
        # key 已存在
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._add(node)

        else:
        # key 不存在 且已满
            if len(self.map) == self.cap:
                lru = self.tail.prev
                self._remove(lru)
                del self.map[lru.key]
            
            # key 不存在 且未满
            node = Node(key, value)
            self.map[key] = node
            self._add(node)
