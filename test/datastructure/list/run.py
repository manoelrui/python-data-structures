from test.datastructure.list.TestQ1 import *
from test.datastructure.list.TestQ2 import *
from test.datastructure.list.TestQ4 import *
from test.datastructure.list.TestQ5 import *
from test.datastructure.list.TestQ3 import *

if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestQ1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestQ2)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestQ3)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(TestQ4)
    suite5 = unittest.TestLoader().loadTestsFromTestCase(TestQ5)
    alltests = unittest.TestSuite([suite1, suite2, suite3, suite4, suite5])
    runner=unittest.TextTestRunner()
    runner.run(alltests)
