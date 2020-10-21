import unittest
from double_linked_list import DoubleLinkedList


class DoubleLinkedListTest_remove_by_value_2(unittest.TestCase):

    def setUp(self):
        self.dll = DoubleLinkedList()
        self.all = DoubleLinkedList()
        self.repeat = DoubleLinkedList()

        all_val = [1, 1, 1, 1]
        self.all.add_list(all_val)
        
        
        repeat_val = [1, 1, 2, 5, 6, 1, 1, 1, 3, 1, 4, 9, 1, 1, 1]
        self.repeat.add_list(repeat_val)

    # list is empty
    def test_remove_empty(self):
        self.dll.remove_by_value_2(1)
        self.assertEqual(self.dll.print(), 'HEAD >>  TAIL')


    # list contains all values to be removed
    def test_remove_all(self):
        self.all.remove_by_value_2(1)
        self.assertEqual(self.all.print(), 'HEAD >>  TAIL')
            
    # list has multiple values at start, middle, and end
    def test_remove_all_2_repeat(self):
        self.repeat.remove_by_value_2(1)
        self.assertEqual(self.repeat.print(), 'HEAD >> 2 -> 5 -> 6 -> 3 -> 4 -> 9 ->  TAIL')
        self.assertEqual(self.repeat.print_reverse(), 'TAIL >> 9 -> 4 -> 3 -> 6 -> 5 -> 2 ->  HEAD')

    # list does not contain remove value
    def test_remove_not_found(self):
        self.repeat.remove_by_value_2(1)
        self.assertEqual(self.repeat.print(), 'HEAD >> 2 -> 5 -> 6 -> 3 -> 4 -> 9 ->  TAIL')    
        self.assertEqual(self.repeat.print_reverse(), 'TAIL >> 9 -> 4 -> 3 -> 6 -> 5 -> 2 ->  HEAD')

if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)        