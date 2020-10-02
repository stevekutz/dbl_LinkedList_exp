import unittest
from test_add_to_head_tests import DoubleLinkedListTests_add_to_head
from test_add_to_tail_tests import DoubleLinkedListTests_add_to_tail
from test_add_list import DoubleLinkedListTests_add_list

def suite():
    suite = unittest.TestSuite()
    suite.addTest(DoubleLinkedListTests_add_to_head('test_add_to_head'))
    suite.addTest(DoubleLinkedListTests_add_to_head('test_add_to_head_2'))
    suite.addTest(DoubleLinkedListTests_add_to_tail('test_add_to_tail'))
    suite.addTest(DoubleLinkedListTests_add_to_tail('test_add_to_tail_2'))
    suite.addTest(DoubleLinkedListTests_add_list('test_add_list'))
    return suite



if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
    runner = unittest.TextTestRunner()
    runner.run(suite())    

    # verbose output
#   unittest.main(argv=['ignored', '-v'], exit=False)