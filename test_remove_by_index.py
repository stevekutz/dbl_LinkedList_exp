import unittest
from double_linked_list import DoubleLinkedList


class DoubleLinkedListTest_remove_by_index(unittest.TestCase):
    
    ######################################
    # Remove index 0      first
    def setUp(self):
        my_list = [1, 2, 3]

        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)

    def test_remove_by_index_0(self):
        self.dll.remove_by_index(0)
        self.assertEqual(self.dll.print(), 'HEAD >> 2 -> 3 ->  TAIL')    
        self.assertCountEqual(self.dll.print_reverse(), 'TAIL >> 3 -> 2 ->  HEAD')

    def tearDown(self):
        self.dll = None

    ######################################
    # remove index 1      node inside list
    def setUp(self):
        my_list = [1, 2, 3,]

        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)

    def test_remove_by_index_inside(self):
        self.dll.remove_by_index(1)
        self.assertEqual(self.dll.print(), 'HEAD >> 1 -> 3 ->  TAIL') 
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 3 -> 1 ->  HEAD')  

    def tearDown(self):
        self.dll = None

    ######################################
    # remove index 2      last node        
    def setUp(self):
        my_list = [1, 2, 3]

        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)

    def test_remove_by_index_last(self):
        self.dll.remove_by_index(2)
        self.assertEqual(self.dll.print(), 'HEAD >> 1 -> 2 ->  TAIL')
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 2 -> 1 ->  HEAD')

if __name__ == '__main__':
    unittest.main(argv = ['ignored', '-v'], exit = False)