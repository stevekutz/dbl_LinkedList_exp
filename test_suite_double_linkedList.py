import unittest
from add_to_head_tests import DoubleLinkedListTests_add_to_head

def suite():
    suite = unittest.TestSuite()
    suite.addTest(DoubleLinkedListTests_add_to_head('test_add_to_head'))
    return suite



if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())    

    # verbose output
#   unittest.main(argv=['ignored', '-v'], exit=False)