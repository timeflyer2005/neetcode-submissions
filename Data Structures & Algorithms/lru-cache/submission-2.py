class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        value = self.store.pop(key)
        self.store[key] = value

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store.pop(key)

        self.store[key] = value

        if len(self.store) > self.capacity:
            least_recent = next(iter(self.store))
            del self.store[least_recent]