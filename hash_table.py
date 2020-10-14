# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Brian F Thomas


class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.data = []

    def __setitem__(self, key, val):
        key = val

    def __getitem__(self, item):
        return item

    def hash(self, val):
        """Returns a hash value that is smaller than the table size"""
        return hash(val) % self.size