import unittest
from datastructure.hash.ExtensibleHash import *


class TestExtensibleHashQ1(unittest.TestCase):
    def test_creation(self):
        n = 10
        h = ExtensibleHash(n, 15)
        self.assertIsNotNone(h)
        self.assertEqual(0, len(h))

        n = 15
        h = ExtensibleHash(n, 20)
        self.assertIsNotNone(h)
        self.assertEqual(0, len(h))

    def test_insertion(self):
        n = 3
        h = ExtensibleHash(n, 5)
        self.assertEqual(len(h), 0)
        #self.assertEqual("", str(h))

        h.add(5,5)
        self.assertEqual(1, len(h))
        #self.assertEqual("(5, 5)", str(h))

        h.add(34,34)
        h.add(51,51)
        h.add(22,22)
        h.add(8,8)
        self.assertEqual(5, len(h))

    def test_print(self):
       pass

    def test_is_empty(self):
        pass

    def test_find(self):
        pass

    def test_remove(self):
        pass

    def test_list_clean(self):
        pass


if __name__ == '__main__':
    unittest.main()
