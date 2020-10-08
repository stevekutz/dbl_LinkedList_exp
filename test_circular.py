import unittest
from double_linked_list import DoubleLinkedList


class DoubleLinkedListTest_circular(unittest.TestCase):
    
    #########################################################
    ##################  verify prev & next pointers in Circular Double Linked List
    def setUp(self):

        my_list = [1, 2, 3]
        self.dll = DoubleLinkedList()
        # self.dll_2 = DoubleLinkedList()
        # self.dll_3 = DoubleLinkedList()

        self.dll.add_list(my_list)
        # self.dll_2.add_list(my_list)
        # self.dll_3.add_list(my_list)

    def test_create_circular(self):
        self.dll.convert_to_circular()
        self.assertEqual(self.dll.detect_circular(), True)
        self.assertEqual(self.dll.print_circular(), '==> HEAD >> 1 -> 2 -> 3 ->  TAIL ===> 1')
        self.assertEqual(self.dll.print_circular_reverse(), 'LAST >> 3 => 2 => 1 =>  HEAD ===> 3')    

    def tearDown(self):
        self.dll = None


    #########################################################
    ##################  add value to front
    def setUp(self):
        my_list = [1, 2, 3]
        
        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)

    def test_add_to_front_circular(self):
        self.dll.convert_to_circular()        
        self.dll.add_value_to_front_circular(100)
        self.assertEqual(self.dll.print_circular(), '==> HEAD >> 100 -> 1 -> 2 -> 3 ->  TAIL ===> 100')
        self.assertEqual(self.dll.print_circular_reverse(), 'LAST >> 3 => 2 => 1 => 100 =>  HEAD ===> 3')

    def tearDown(self):
        self.dll = None



    #########################################################
    ##################  add value to tail        
    def setUp(self):
        my_list = [1, 2, 3]
        
        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)

    def test_add_value_to_end_circular(self):
        self.dll.convert_to_circular()
        self.dll.add_value_to_last_circular(999)
        self.assertEqual(self.dll.print_circular(), '==> HEAD >> 1 -> 2 -> 3 -> 999 ->  TAIL ===> 1')
        self.assertEqual(self.dll.print_circular_reverse(), 'LAST >> 999 => 3 => 2 => 1 =>  HEAD ===> 999')


    def tearDown(self):
        self.dll = None     




if __name__ == '__main__':
    # unittest.main()  

    # verbose output
    unittest.main(argv=['ignored', '-v'], exit=False) 