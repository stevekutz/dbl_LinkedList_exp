import unittest
from test_double_linked_list import DoubleLinkedListTests_add_to_head

def suite():
    suite = unittest.TestSuite()
    suite.addTest(DoubleLinkedListTests_add_to_head('test_add_to_head'))
    return suite



if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())    