from operator import mod
from datastructure.list.LinkedList import *


class HashTuple(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other

    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.value) + ")"


class Hash(object):
    def __init__(self, n):
        self.vec = []
        for x in range(0, (n/2)):
            self.vec.append(LinkedList())
        self.func = lambda key: mod((key * 101), (n/2))

    def __len__(self):
        total_length = 0
        for data_structure in self.vec:
            total_length += len(data_structure)
        return total_length

    def add(self, key, value):
        bucket = self.func(key)
        self.vec[bucket].add(HashTuple(key, value))

    def __str__(self):
        result = ""
        for data_structure in self.vec:
            if len(data_structure) > 0:
                result += str(data_structure) + " "
        return result.strip()

    def is_empty(self):
        if len(self) > 0:
            return False
        return True

    def find(self, key):
        bucket = self.func(key)
        hash_tuple = self.vec[bucket].find(key)
        if hash_tuple is not None:
            return hash_tuple.value
        return None

    def remove(self, key):
        bucket = self.func(key)
        return self.vec[bucket].remove(key)

    def clean(self):
        for data_structure in self.vec:
            data_structure.clean()
