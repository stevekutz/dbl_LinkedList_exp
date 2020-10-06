import unittest
from double_linked_list import DoubleLinkedList


class DoubleLinkedListTest_remove_by_value(unittest.TestCase):
    ###############################################################
    #################   all values removed, empty list returned
    def setUp(self):
        my_list = [2,3,4]
        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)

    def test_remove_by_value_all(self):
        self.dll.remove_by_value(1)
        self.assertEqual(self.dll.get_length(), 0) 
        
    def tear_down(self):
        self.dll = None
    
    
    ###############################################################
    #################   all values removed, empty list returned
    def setUp(self):
        my_list = [1, 1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 4, 1, 1, 1]
        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)

    def test_remove_by_value_all(self):
        self.dll.remove_by_value(1)
        self.assertEqual(self.dll.get_length(), 3) 
        self.assertEqual(self.dll.print(), 'HEAD >> 2 -> 3 -> 4 ->  TAIL')
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 4 -> 3 -> 2 ->  HEAD')

        
    def tear_down(self):
        self.dll = None



    ###############################################################
    #################   all values removed, empty list returned
    def setUp(self):
        my_list = [1, 1, 1, 1]
        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)

    def test_remove_by_value_all(self):
        self.dll.remove_by_value(1)
        self.assertEqual(self.dll.get_length(), 0) 
        
    def tear_down(self):
        self.dll = None


if __name__ == '__main__':
    # unittest.main()  

    # verbose output
    unittest.main(argv=['ignored', '-v'], exit=False)          