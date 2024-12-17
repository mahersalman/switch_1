class HashTableOpenAddressing:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.size = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        if self.size == self.capacity:
            raise Exception("Hash table is full")

        index = self._hash(key)
        initial_index = index
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.capacity
            if index == initial_index:
                raise Exception("Hash table is full")

        if self.table[index] is not None and self.table[index][0] == key:
            self.table[index] = (key, value)
        else:
            self.table[index] = (key, value)
            self.size += 1

    def get(self, key):
        index = self._hash(key)
        initial_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity
            if index == initial_index:
                return None
        return None

    def remove(self, key):
        index = self._hash(key)
        initial_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.size -= 1
                self._rehash(index)
                return True
            index = (index + 1) % self.capacity
            if index == initial_index:
                return False
        return False

    def _rehash(self, start_index):
        index = (start_index + 1) % self.capacity
        while self.table[index] is not None:
            key, value = self.table[index]
            self.table[index] = None
            self.size -= 1
            self.insert(key, value)
            index = (index + 1) % self.capacity

