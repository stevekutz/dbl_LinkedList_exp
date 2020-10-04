from test_add_before_value import DoubleLinkedListTest_add_before_value
import unittest
from test_add_to_head_tests import DoubleLinkedListTests_add_to_head
from test_add_to_tail_tests import DoubleLinkedListTests_add_to_tail
from test_add_list import DoubleLinkedListTests_add_list
from test_remove_by_index import DoubleLinkedListTest_remove_by_index
from test_add_after_value import DoubleLinkedListTests_add_after_value
from test_add_before_value import DoubleLinkedListTest_add_before_value


def suite():
    suite = unittest.TestSuite()
    suite.addTest(DoubleLinkedListTests_add_to_head('test_add_to_head'))
    suite.addTest(DoubleLinkedListTests_add_to_head('test_add_to_head_2'))

    suite.addTest(DoubleLinkedListTests_add_to_tail('test_add_to_tail'))
    suite.addTest(DoubleLinkedListTests_add_to_tail('test_add_to_tail_2'))

    suite.addTest(DoubleLinkedListTests_add_list('test_add_list'))

    suite.addTest(DoubleLinkedListTest_remove_by_index('test_remove_by_index_0'))
    suite.addTest(DoubleLinkedListTest_remove_by_index('test_remove_by_index_inside'))
    suite.addTest(DoubleLinkedListTest_remove_by_index('test_remove_by_index_last'))

    suite.addTest(DoubleLinkedListTests_add_after_value('test_add_after_value'))

    suite.addTest(DoubleLinkedListTest_add_before_value('test_insert_before_value_1'))
    suite.addTest(DoubleLinkedListTest_add_before_value('test_insert_before_value_2'))
    suite.addTest(DoubleLinkedListTest_add_before_value('test_insert_before_value_3'))  
    suite.addTest(DoubleLinkedListTest_add_before_value('test_insert_before_value__1'))
    suite.addTest(DoubleLinkedListTest_add_before_value('test_insert_before_value__2'))
    suite.addTest(DoubleLinkedListTest_add_before_value('test_insert_before_value__3'))    
    



    return suite



if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
    runner = unittest.TextTestRunner()
    runner.run(suite())    

    # verbose output
#   unittest.main(argv=['ignored', '-v'], exit=False)