import unittest
from datastructure.hash.Hash import *


class TestHashQ1(unittest.TestCase):
    def test_creation(self):
        n = 10
        h = Hash(n)
        self.assertIsNotNone(h)
        self.assertEqual(0, len(h))

        n = 15
        h = Hash(n)
        self.assertIsNotNone(h)
        self.assertEqual(0, len(h))

    def test_insertion(self):
        n = 13
        h = Hash(n)
        self.assertEqual(len(h), 0)
        self.assertEqual("", str(h))

        h.add(5,5)
        self.assertEqual(1, len(h))
        self.assertEqual("(5, 5)", str(h))

        h.add(34,34)
        h.add(51,51)
        h.add(22,22)
        h.add(8,8)
        self.assertEqual(5, len(h))

    def test_is_empty(self):
        n = 7
        h = Hash(n)
        self.assertEqual(len(h), 0)
        self.assertTrue(h.is_empty())

        n = 8
        h = Hash(n)
        h.add(5,5)
        h.add(93,93)
        self.assertEqual(2, len(h))
        self.assertTrue(h.is_empty() == False)

    def test_find(self):
        n = 11
        h = Hash(n)
        self.assertEqual(0, len(h))
        self.assertIsNone(h.find(16), None)

        h.add(2,33)
        h.add(3,67)
        h.add(7,90)
        h.add(44,176)
        self.assertEqual(4, len(h))
        self.assertEqual(h.find(2), 33)
        self.assertEqual(h.find(3), 67)
        self.assertEqual(h.find(7), 90)
        self.assertEqual(h.find(44), 176)
        self.assertIsNone(h.find(556))

    def test_remove(self):
        n = 17
        h = Hash(n)
        self.assertEqual(0, len(h))
        self.assertTrue(h.remove(666) == False)

        h.add(2,33)
        h.remove(2)
        self.assertEqual(0, len(h))

        h.add(3,67)
        h.add(7,90)
        h.add(44,176)
        h.add(883,24)
        self.assertEqual(4, len(h))
        self.assertTrue(h.remove(7) == True)
        self.assertTrue(h.remove(883) == True)
        self.assertEqual(2, len(h))

        self.assertTrue(h.remove(556) == False)
        self.assertEqual(2, len(h))

    def test_list_clean(self):
        n = 9
        h = Hash(n)
        h.clean()
        self.assertEqual(0, len(h))

        h.add(2,33)
        h.clean()
        self.assertEqual(0, len(h))

        h.add(3,67)
        h.add(7,90)
        h.add(44,176)
        h.add(883,24)
        h.clean()
        self.assertEqual(0, len(h))

if __name__ == '__main__':
    unittest.main()
