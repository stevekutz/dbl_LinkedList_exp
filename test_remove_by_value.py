import unittest
from double_linked_list import DoubleLinkedList


class DoubleLinkedListTest_remove_by_value(unittest.TestCase):
    ###############################################################
    #################   all values removed, empty list returned
    def setUp(self):
        not_found = [2,3,4]
        self.dll_1 = DoubleLinkedList()
        self.dll_1.add_list(not_found)

        repeat_list = [1, 1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 4, 1, 1, 1]
        self.dll_2 = DoubleLinkedList()
        self.dll_2.add_list(repeat_list)

        all_removed = [1, 1, 1, 1]
        self.dll_3 = DoubleLinkedList()
        self.dll_3.add_list(all_removed)

    def test_remove_by_value_not_found(self):
        self.dll_1.remove_by_value(1)
        self.assertEqual(self.dll_1.get_length(), 3) 
        
        
    ###############################################################
    #################   all values removed, empty list returned

    def test_remove_by_value_repeat(self):
        self.dll_2.remove_by_value(1)
        # self.assertEqual(self.dll.get_length(), 3) 
        self.assertEqual(self.dll_2.print(), 'HEAD >> 2 -> 3 -> 4 ->  TAIL')
        self.assertEqual(self.dll_2.print_reverse(), 'TAIL >> 4 -> 3 -> 2 ->  HEAD')


    ###############################################################
    #################   all values removed, empty list returned

    def test_remove_by_value_all(self):
        self.dll_3.remove_by_value(1)
        self.assertEqual(self.dll_3.get_length(), 0) 



if __name__ == '__main__':
    # unittest.main()  

    # verbose output
    unittest.main(argv=['ignored', '-v'], exit=False)          