# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Brian F Thomas


class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.data = []
        for i in range(0, size):
            self.data.append([])

    def __setitem__(self, key, val):
        index = self.hash(key)
        if self.__getitem__(key):
            for i in self.data[index]:
                if i[0] == key:
                    self.data[index][0][1] = val
                    return
            self.data[index].append([key, val])

        else:
            self.data[index].append([key, val])

    def __getitem__(self, key):
        index = self.hash(key)
        if not self.data[index]:
            return None
        return self.data[index][0][1]

    def hash(self, key):
        """Returns a hash value that is smaller than the table size"""
        return hash(key) % self.size