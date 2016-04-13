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

    def is_full(self):
        return len(self) >= len(self.vec)

    def add(self, key, value):
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
        self.number_of_buckets = 1
        self.bucket_len = bucket_len
        self.vec = [Bucket(bucket_len)] * int(math.pow(2, self.deep))
        self.func = lambda key: mod((key * 101), math.pow(2, self._n_bits))

    def __len__(self):
        total_length = 0
        return total_length

    def get_bucket(self, key):
        pass

    def add(self, key, value):
        hash_value = self.func(key)
        bucket = self.vec[hash_value]
        if len(bucket) < self.bucket_len:
            bucket.add(HashTuple(key, value))
        #split the bucket
        else:
            if self.number_of_buckets < self.deep:
                pass

    def find(self, key, value):
        pass

    def remove(self, key, value):
        
        pass
