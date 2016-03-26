import unittest
import datastructure.list.LinkedList
import TestQ1


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQ1.TestQ1)
    alltests = unittest.TestSuite([suite])
    alltests.run()

