import unittest

from double_linked_list import DoubleLinkedList

class DoubleLinkedListTests_add_list(unittest.TestCase):
    def setUp(self):
        self.dll = DoubleLinkedList()

    def test_add_list(self):
        # test_list
        list_vals = [1, 2, 3]

        self.dll.add_list(list_vals)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.head.next.value, 2)
        self.assertEqual(self.dll.head.next.next.value, 3)

if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit = False)        