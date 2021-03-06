from test_add_before_value import DoubleLinkedListTest_add_before_value
import unittest
from test_add_to_head_tests import DoubleLinkedListTests_add_to_head
from test_add_to_tail_tests import DoubleLinkedListTests_add_to_tail
from test_add_list import DoubleLinkedListTests_add_list
from test_remove_by_index import DoubleLinkedListTest_remove_by_index
from test_add_after_value import DoubleLinkedListTests_add_after_value
from test_add_before_value import DoubleLinkedListTest_add_before_value
from test_remove_by_value import DoubleLinkedListTest_remove_by_value
from test_reverse_list import DoubleLinkedListTest_reverse_list
from test_circular import DoubleLinkedListTest_circular
from test_remove_nth_from_end import DoubleLinkedListTest_remove_nth_from_end
from test_remove_by_value_2 import DoubleLinkedListTest_remove_by_value_2

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
    
    suite.addTest(DoubleLinkedListTest_remove_by_value('test_remove_by_value_not_found'))
    suite.addTest(DoubleLinkedListTest_remove_by_value('test_remove_by_value_repeat'))
    suite.addTest(DoubleLinkedListTest_remove_by_value('test_remove_by_value_all'))

    suite.addTest(DoubleLinkedListTest_reverse_list('test_reverse_list'))

    suite.addTest(DoubleLinkedListTest_circular('test_create_circular'))
    suite.addTest(DoubleLinkedListTest_circular('test_add_to_front_circular'))
    suite.addTest(DoubleLinkedListTest_circular('test_add_value_to_end_circular'))


    suite.addTest(DoubleLinkedListTest_remove_nth_from_end('test_remove_0th_from_end'))
    suite.addTest(DoubleLinkedListTest_remove_nth_from_end('test_remove_100th_from_end'))
    suite.addTest(DoubleLinkedListTest_remove_nth_from_end('test_remove_1st_from_end'))
    suite.addTest(DoubleLinkedListTest_remove_nth_from_end('remove_2nd_from_end'))
    suite.addTest(DoubleLinkedListTest_remove_nth_from_end('test_remove_3rd_from_end'))
    suite.addTest(DoubleLinkedListTest_remove_nth_from_end('test_remove_4th_from_end'))


    suite.addTest(DoubleLinkedListTest_remove_by_value_2('test_remove_empty'))
    suite.addTest(DoubleLinkedListTest_remove_by_value_2('test_remove_all'))
    suite.addTest(DoubleLinkedListTest_remove_by_value_2('test_remove_all_2_repeat'))
    suite.addTest(DoubleLinkedListTest_remove_by_value_2('test_remove_not_found'))


    return suite



if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
    runner = unittest.TextTestRunner()
    runner.run(suite())    

    # verbose output
#   unittest.main(argv=['ignored', '-v'], exit=False)