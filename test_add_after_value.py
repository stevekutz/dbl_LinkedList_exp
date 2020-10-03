import unittest
from double_linked_list import DoubleLinkedList
import logging

class DoubleLinkedListTests_add_list(unittest.TestCase):
    
    def setUp(self):
        my_list = [1, 2, 3]

        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)

    def test_add_list(self):
        self.dll.add_after_value(1, 999)
        self.assertEqual(self.dll.head.next.value, 999)
        self.dll.add_after_value(2, 999)

        self.dll.add_after_value(3, 999)

if __name__ == '__main__':
    unittest.main(argv = ['ignored', '-v'], exit = False)        