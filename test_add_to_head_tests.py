import unittest
from double_linked_list import DoubleLinkedList #, Node

class DoubleLinkedListTests_add_to_head(unittest.TestCase):
    # create instance
    def setUp(self):
        self.dll = DoubleLinkedList()

    def test_add_to_head(self):
        self.dll.add_to_head(3)
        self.assertEqual(self.dll.head.value, 3)     
        self.dll.add_to_head(2)
        self.assertEqual(self.dll.head.value, 2)
        self.dll.add_to_head(1)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.print(), 'HEAD >> 1 -> 2 -> 3 ->  TAIL')  
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 3 -> 2 -> 1 ->  HEAD' )


    # remove instance
    def tearDown(self):
          self.dll = None

    def setUp(self):
      self.dll = DoubleLinkedList()

    def test_add_to_head_2(self):
        self.dll.add_to_head_2(3)
        self.assertEqual(self.dll.head.value, 3)     
        self.dll.add_to_head_2(2)
        self.assertEqual(self.dll.head.value, 2)
        self.dll.add_to_head_2(1)
        self.assertEqual(self.dll.head.value, 1)            
        self.assertEqual(self.dll.print(), 'HEAD >> 1 -> 2 -> 3 ->  TAIL')  
        self.assertEqual(self.dll.print_reverse(), 'TAIL >> 3 -> 2 -> 1 ->  HEAD' )

if __name__ == '__main__':
## direct output
#   unittest.main()

# verbose output
  unittest.main(argv=['ignored', '-v'], exit=False)

# from command line
# python3 -m unittest -v test_double_linked_list.py
