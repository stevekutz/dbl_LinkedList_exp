import unittest
from double_linked_list import DoubleLinkedList


class DoubleLinkedListTests_add_to_tail(unittest.TestCase):
    def setUp(self):
        self.dll = DoubleLinkedList()
        self.dll2 = DoubleLinkedList()

    def test_add_to_tail(self):
        self.dll.add_to_tail(1)
        self.assertEqual(self.dll.head.value, 1) 
        self.dll.add_to_tail(2)
        self.assertEqual(self.dll.print(), 'HEAD >> 1 -> 2 ->  TAIL') 
        self.dll.add_to_tail(3)
        self.assertEqual(self.dll.print(), 'HEAD >> 1 -> 2 -> 3 ->  TAIL')  
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 3 -> 2 -> 1 ->  HEAD' )


    def test_add_to_tail_2(self):
        self.dll2.add_to_tail_2(1)
        self.assertEqual(self.dll2.head.value, 1)
        self.dll2.add_to_tail_2(2)
        self.assertEqual(self.dll2.head.next.value, 2)
        self.dll2.add_to_tail_2(3)
        self.assertEqual(self.dll2.head.next.next.value, 3)
        self.assertEqual(self.dll2.print(), 'HEAD >> 1 -> 2 -> 3 ->  TAIL')
        self.assertEqual(self.dll2.print_reverse(), 'TAIL >> 3 -> 2 -> 1 ->  HEAD')

if __name__ == '__main__':
    # unittest.main()  

    # verbose output
    unittest.main(argv=['ignored', '-v'], exit=False)      