import unittest
from double_linked_list import DoubleLinkedList


class DoubleLinkedListTest_add_before_value(unittest.TestCase):
    
    
    
    ####################################################
    def setUp(self):
        my_list = [1 ,2 ,3]
        
        self.dll_1 = DoubleLinkedList()
        self.dll_1.add_list(my_list)

        self.dll_2 = DoubleLinkedList()
        self.dll_2.add_list(my_list)

        self.dll_3 = DoubleLinkedList()
        self.dll_3.add_list(my_list)

    def test_insert_before_value_1(self):
        self.dll_1.add_before_value(1, 999)
        self.assertEqual(self.dll_1.print(), 'HEAD >> 999 -> 1 -> 2 -> 3 ->  TAIL')
        self.assertEqual(self.dll_1.print_reverse(), 'TAIL >> 3 -> 2 -> 1 -> 999 ->  HEAD')   

    def test_insert_before_value_2(self):
        self.dll_2.add_before_value(2, 999)
        self.assertEqual(self.dll_2.print(), 'HEAD >> 1 -> 999 -> 2 -> 3 ->  TAIL')
        self.assertEqual(self.dll_2.print_reverse(), 'TAIL >> 3 -> 2 -> 999 -> 1 ->  HEAD') 

    def test_insert_before_value_3(self):
        self.dll_3.add_before_value(3, 999)
        self.assertEqual(self.dll_3.print(), 'HEAD >> 1 -> 2 -> 999 -> 3 ->  TAIL')
        self.assertEqual(self.dll_3.print_reverse(), 'TAIL >> 3 -> 999 -> 2 -> 1 ->  HEAD')        

    def tearDown(self):
        self.dll_1 = None
        self.dll_2 = None
        self.dll_3 = None

    ####################################################
    def setUp(self):
        my_list = [1 ,2 ,3]
        
        self.dll_1 = DoubleLinkedList()
        self.dll_1.add_list(my_list)

        self.dll_2 = DoubleLinkedList()
        self.dll_2.add_list(my_list)

        self.dll_3 = DoubleLinkedList()
        self.dll_3.add_list(my_list)

    def test_insert_before_value__1(self):
        self.dll_1.add_before_value_2(1, 999)
        self.assertEqual(self.dll_1.print(), 'HEAD >> 999 -> 1 -> 2 -> 3 ->  TAIL')
        self.assertEqual(self.dll_1.print_reverse(), 'TAIL >> 3 -> 2 -> 1 -> 999 ->  HEAD')   

    def test_insert_before_value__2(self):
        self.dll_2.add_before_value_2(2, 999)
        self.assertEqual(self.dll_2.print(), 'HEAD >> 1 -> 999 -> 2 -> 3 ->  TAIL')
        self.assertEqual(self.dll_2.print_reverse(), 'TAIL >> 3 -> 2 -> 999 -> 1 ->  HEAD') 

    def test_insert_before_value__3(self):
        self.dll_3.add_before_value_2(3, 999)
        self.assertEqual(self.dll_3.print(), 'HEAD >> 1 -> 2 -> 999 -> 3 ->  TAIL')
        self.assertEqual(self.dll_3.print_reverse(), 'TAIL >> 3 -> 999 -> 2 -> 1 ->  HEAD')        

    def tearDown(self):
        self.dll_1 = None
        self.dll_2 = None
        self.dll_3 = None