import unittest
from test.application.TestQ6 import *
from test.datastructure.list.TestQ1 import *
from test.datastructure.list.TestQ2 import *
from test.datastructure.list.TestQ4 import *
from test.datastructure.list.TestQ5 import *
from test.datastructure.list.TestQ3 import *
from test.datastructure.hash.TestHashQ1 import *
from test.datastructure.hash.TestExtensibleHashQ1 import *

if __name__ == '__main__':
    unittest.TestLoader().loadTestsFromTestCase(TestQ1)
    unittest.TestLoader().loadTestsFromTestCase(TestQ2)
    unittest.TestLoader().loadTestsFromTestCase(TestQ3)
    unittest.TestLoader().loadTestsFromTestCase(TestQ4)
    unittest.TestLoader().loadTestsFromTestCase(TestQ5)
    unittest.TestLoader().loadTestsFromTestCase(TestQ6)
    unittest.TestLoader().loadTestsFromTestCase(TestHashQ1)
    unittest.TestLoader().loadTestsFromTestCase(TestExtensibleHashQ1)
    unittest.main()