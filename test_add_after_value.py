import unittest
from double_linked_list import DoubleLinkedList

import logging

class DoubleLinkedListTests_add_after_value(unittest.TestCase):
    
    def setUp(self):
        my_list = [1, 2, 3, 4]

        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)

    def test_add_after_value(self):
        self.dll.add_after_value(0, 999)
        self.assertEqual(self.dll.print(), 'HEAD >> 1 -> 2 -> 3 -> 4 ->  TAIL')
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 4 -> 3 -> 2 -> 1 ->  HEAD')

        self.dll.add_after_value(1, 999)
        self.assertEqual(self.dll.print(), 'HEAD >> 1 -> 999 -> 2 -> 3 -> 4 ->  TAIL')
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 4 -> 3 -> 2 -> 999 -> 1 ->  HEAD')

        self.dll.add_after_value(2, 999)
        self.assertEqual(self.dll.print(), 'HEAD >> 1 -> 999 -> 2 -> 999 -> 3 -> 4 ->  TAIL')
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 4 -> 3 -> 999 -> 2 -> 999 -> 1 ->  HEAD')

        self.dll.add_after_value(3, 999)
        self.assertEqual(self.dll.print(), 'HEAD >> 1 -> 999 -> 2 -> 999 -> 3 -> 999 -> 4 ->  TAIL')
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 4 -> 999 -> 3 -> 999 -> 2 -> 999 -> 1 ->  HEAD')

        self.dll.add_after_value(4, 999)
        self.assertEqual(self.dll.print(), 'HEAD >> 1 -> 999 -> 2 -> 999 -> 3 -> 999 -> 4 -> 999 ->  TAIL')
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 999 -> 4 -> 999 -> 3 -> 999 -> 2 -> 999 -> 1 ->  HEAD')

        self.dll.add_after_value(1, 888)
        self.assertEqual(self.dll.print(), 'HEAD >> 1 -> 888 -> 999 -> 2 -> 999 -> 3 -> 999 -> 4 -> 999 ->  TAIL')
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 999 -> 4 -> 999 -> 3 -> 999 -> 2 -> 999 -> 888 -> 1 ->  HEAD')


if __name__ == '__main__':
    unittest.main(argv = ['ignored', '-v'], exit = False)        