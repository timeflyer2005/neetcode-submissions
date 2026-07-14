class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)
        
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
    
    def insert(self, node):
        most_recent = self.right.prev
        most_recent.next = node
        node.prev = most_recent

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_Node = Node(key, value)
        self.cache[key] = new_Node
        self.insert(new_Node)
        
        if len(self.cache) > self.capacity:
            least_recent = self.left.next
            self.remove(least_recent)
            del self.cache[least_recent.key]