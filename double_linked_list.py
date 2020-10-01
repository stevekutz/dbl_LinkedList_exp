class Node:
    def __init__(self, value, prev = None, next = None ):
        self.value = value
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):

        # List is empty
        if self.head == None:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node   
        # nodes already exist, must manage prev and next
        else:
            new_node = Node(value)
            orig_head = self.head  # save pointer to head
            new_node.next = orig_head # point to orig head
            orig_head.prev = new_node  # point to new node
            self.head = new_node   # assign new node as head

    def add_to_tail(self, value):

        current = self.head
        last_node = current

        # if list empty
        if current == None: 
            new_node = Node(value)
            new_node.next = current
            self.head = new_node
            return

        # if list has at least one item, find last node
        else:
            while current:
                last_node = current
                current = current.next

        new_node = Node(value)
        last_node.next = new_node
        new_node.prev = last_node
                
    def print(self):
        current = self.head
        list_str = 'HEAD >> '

        if current == None:
            print(f' Double Linked List is empty ')

        while current:
            list_str += str(current.value) + ' -> '
            current = current.next

        list_str += ' TAIL'    
        print(f'{list_str}')






dbl_ll_1 = DoubleLinkedList()

# dbl_ll_1.add_to_head(3)
# dbl_ll_1.print()

# dbl_ll_1.add_to_head(2)
# dbl_ll_1.add_to_head(1)
# dbl_ll_1.print()

dbl_ll_1.add_to_tail(10)
dbl_ll_1.print()

dbl_ll_1.add_to_tail(11)
dbl_ll_1.print()

dbl_ll_1.add_to_tail(12)
dbl_ll_1.add_to_tail(13)
dbl_ll_1.print()