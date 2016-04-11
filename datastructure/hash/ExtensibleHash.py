import math
from datastructure.hash.Hash import *


class Bucket(object):
    def __init__(self, bucket_len):
        self.deep = 1
        self.vec = [None] * bucket_len
        self.length = 0

    def __len__(self):
        total_length = 0
        for element in self.vec:
            if element is not None:
                total_length += 1
        return total_length

    def add(self):
        pass

    def find(self):
        pass

    def remove(self):
        pass


class ExtensibleHash(Bucket):
    def __init__(self, n, bucket_len):
        super(ExtensibleHash, self).__init__(bucket_len)
        self._n_bits = 32
        self.deep = math.ceil(math.log(n, 2))
        self.vec = [Bucket(bucket_len)] * int(math.pow(2, self.deep))
        self.func = lambda key: mod((key * 101), math.pow(2, self._n_bits))

    def __len__(self):
        total_length = 0
        return total_length

    def add(self):
        pass

    def find(self):
        pass

    def remove(self):
        pass
