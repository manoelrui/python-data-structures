import math
from datastructure.hash.Hash import *


class Bucket(object):
    def __init__(self, bucket_len):
        self.deep = 0
        self.container = [None] * bucket_len
        self.length = 0

    def __len__(self):
        return self.length

    def is_full(self):
        return len(self) >= len(self.container)

    def add(self, key, value):
        if self.is_full():
            return False
        self.container[self.length] = (HashTuple(key, value))
        self.length += 1
        return True

    def find(self):
        pass

    def remove(self):
        pass


class ExtensibleHash(Bucket):
    def __init__(self, n, bucket_len):
        super(ExtensibleHash, self).__init__(bucket_len)
        self._n_bits = 32
        self.deep = int(math.ceil(math.log(n, 2)))
        self.number_of_buckets = 1
        self.bucket_len = bucket_len
        self.container = [Bucket(bucket_len)] * int(math.pow(2, self.deep))
        self.func = lambda key: int(mod((key * 101), math.pow(2, self._n_bits)))

    def __len__(self):
        total_length = 0
        return len(s)

    def get_bucket(self, key):
        pass

    def add(self, key, value):
        hash_value = self.func(key)
        bucket = self.container[hash_value & ((1 << self.deep) -1)]

        if bucket.is_full() and bucket.deep >= self.deep:
            return False
            # TODO: To expand the key space

        # Split one bucket in another two
        if bucket.is_full() and bucket.deep < self.deep:
            new_bucket_1 = Bucket()
            new_bucket_2 = Bucket()

            # split values in two buckets
            for hash_tuple in Bucket:
                hash_value = self.func(hash_tuple.key)
                hash_value &= ((1 << self.deep) -1)
                if (hash_value >> bucket.deep) & 1 == 1:
                    new_bucket_1.add(key, value)
                else:
                    new_bucket_2.add(key, value)

            # replace pointers to new buckets
            for index, b in enumerate(self.container):
                if b == bucket:
                    if (index >> bucket.deep) & 1 == 1:
                        self.container[index] = new_bucket_1
                    else:
                        self.container[index] = new_bucket_2
            new_bucket_1.deep = new_bucket_2 = bucket.deep + 1
            del bucket
            return self.add(key, value)
        else:
            return bucket.add(key, value)

    def find(self, key, value):
        pass

    def remove(self, key, value):
        
        pass
