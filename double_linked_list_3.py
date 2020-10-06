class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            print("node inserted")
            return
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete_element_by_value(self, x):
        if self.head is None:
            print("The list has no element to delete")
            return 
        if self.head.next is None:
            if self.head.value == x:
                self.head = None
            else:
                print("Item not found")
            return 

        if self.head.value == x:
            self.head = self.head.next
            self.head.prev = None
            return

        n = self.head
        while n.next is not None:
            if n.value == x:
                break;
            n = n.next
        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            if n.value == x:
                n.prev.next = None
            else:
                print("Element not found")


    def print(self):
        current = self.head
        list_str = 'head >> '

        if current is None:
            print(f' Double Linked List is empty ')

        while current is not None:
            list_str += str(current.value) + ' -> '
            current = current.next

        list_str += ' TAIL'    
        print(f'{list_str}')
        return list_str    

        # if hasattr(self.head, 'next'):
        #     print(f' self.head.value  {self.head.value}')
        #     print(f' next is  {self.head.next}')

        # if getattr(current, 'next') is None:
        #     print(f' current.next is None')

    def print_reverse(self):

        current = self.head
        list_str = 'TAIL >> '

        while current.next is not None:
            current = current.next

        # print(f' current.value   {current.value}')    
    
        while current is not None:
            list_str += str(current.value) + ' -> '
            current = current.prev

        list_str += ' HEAD'
        print(f'{list_str}')
        return list_str

dll = DoublyLinkedList()

dll.insert_at_start(1)
dll.insert_at_start(1)
dll.insert_at_start(2)
dll.insert_at_start(1)
dll.insert_at_start(3)
dll.insert_at_start(1)
dll.insert_at_start(1)
dll.insert_at_start(4)
dll.insert_at_start(1)
dll.insert_at_start(1)

dll.print()
dll.print_reverse()
dll.delete_element_by_value(1)
dll.print()
dll.print_reverse()