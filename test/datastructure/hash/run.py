from test.datastructure.hash.TestHashQ1 import TestHashQ1
from test.datastructure.hash.TestExtensibleHashQ1 import TestExtensibleHashQ1
import unittest


if __name__ == '__main__':
    unittest.TestLoader().loadTestsFromTestCase(TestHashQ1)
    unittest.TestLoader().loadTestsFromTestCase(TestExtensibleHashQ1)
    unittest.main()

