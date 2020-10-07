import unittest
from double_linked_list import DoubleLinkedList

class DoubleLinkedListTest_reverse_list(unittest.TestCase):
    def setUp(self):
        my_list = [1, 2, 3]     
        self.dll = DoubleLinkedList()
        self.dll.add_list(my_list)


    def test_reverse_list(self):
        self.dll.reverse_list()
        self.assertEqual(self.dll.print(), 'HEAD >> 3 -> 2 -> 1 ->  TAIL')
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 1 -> 2 -> 3 ->  HEAD')


if __name__ == '__main__':
    # unittest.main()  

    # verbose output
    unittest.main(argv=['ignored', '-v'], exit=False)         