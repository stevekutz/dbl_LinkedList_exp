import unittest
from double_linked_list import DoubleLinkedList

class DoubleLinkedListTest_remove_nth_from_end(unittest.TestCase):
########################################################################
#############      remove 0th from end, remove value outside of index range, 1st from end 
    
    def setUp(self):
        my_list = [4, 3, 2, 1]
        
        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)


    def test_remove_0th_from_end(self):
        self.dll.remove_nth_from_end(0)
        self.assertEqual(self.dll.print(), 'HEAD >> 4 -> 3 -> 2 -> 1 ->  TAIL')    

    def test_remove_100th_from_end(self):
        self.dll.remove_nth_from_end(100)
        self.assertEqual(self.dll.print(), 'HEAD >> 4 -> 3 -> 2 -> 1 ->  TAIL')

    def test_remove_1st_from_end(self):
        self.dll.remove_nth_from_end(1)
        self.assertEqual(self.dll.print(), 'HEAD >> 4 -> 3 -> 2 ->  TAIL')
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 2 -> 3 -> 4 ->  HEAD')


    def tearDown(self):
        self.dll = None

########################################################################
#############      remove from inside  2nd from end
    def setUp(self):
        my_list = [4, 3, 2, 1]
        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)

    def remove_2nd_from_end(self):
        self.dll.remove_nth_from_end(2)
        self.assertEqual(self.dll.print(), 'HEAD >> 4 -> 3 -> 1 ->  TAIL')
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 1 -> 3 -> 4 ->  HEAD')


    def tearDown(self):
        self.dll = None

########################################################################
#############      remove from inside 3rd from end
    def setUp(self):
        my_list = [4, 3, 2, 1]
        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)


    def test_remove_3rd_from_end(self):
        self.dll.remove_nth_from_end(3)
        self.assertEqual(self.dll.print(), 'HEAD >> 4 -> 2 -> 1 ->  TAIL')
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 1 -> 2 -> 4 ->  HEAD')


    def tearDown(self):
        self.dll = None

########################################################################
#############      remove from inside 4th from end

    def setUp(self):
        my_list = [4, 3, 2, 1]
        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)



    def test_remove_4th_from_end(self):
        self.dll.remove_nth_from_end(4)
        self.assertEqual(self.dll.print(), 'HEAD >> 3 -> 2 -> 1 ->  TAIL')
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 1 -> 2 -> 3 ->  HEAD')


    def tearDown(self):
        self.dll = None



if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False) 