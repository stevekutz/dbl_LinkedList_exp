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
        if self.head is None:
            new_node = Node(value)
            # new_node.next = self.head
            self.head = new_node   
        # nodes already exist, must manage prev and next
        else:
            new_node = Node(value)
            orig_head = self.head  # save pointer to head
            new_node.next = orig_head # point to orig head
            orig_head.prev = new_node  # point to new node
            self.head = new_node   # assign new node as head

            # # another way without defining a variable to clarify orig_head
            # new_node = Node(value)
            # new_node.next = self.head
            # self.head.prev = new_node
            # self.head = new_node

    def add_to_head_2(self, value):

        current = self.head

        new_node = Node(value)
        new_node.next = current
        self.head = new_node


    def add_to_tail(self, value):

        current = self.head
        last_node = current

        # if list empty
        if current is None: 
            new_node = Node(value)
            # new_node.next = current
            self.head = new_node
            return

        # if list has at least one item, find last node
        else:
            while current is not None:
                last_node = current
                current = current.next

        # if hasattr(last_node, 'next'):
        #     print(f' found last_node: {last_node.value}    last_node.next is  {last_node.next}  ')
        #     prev_node = last_node.prev
        #     print(f' \t prev is   {prev_node}')
        # if getattr(last_node, 'next') is None:
        #     print(f' found last_node: {last_node.value}    last_node.next is  {last_node.next}')


        new_node = Node(value)
        last_node.next = new_node
        new_node.prev = last_node

    def add_to_tail_2(self, value):
        current = self.head
        new_node = Node(value)
        prev_node = None

        if current is None:
            self.head = new_node

        else:
            while current:
                prev_node = current
                current = current.next
            prev_node.next = new_node
            new_node.prev = prev_node



    def add_after_value(self, value, new_value):

        current = self.head

        while current is not None:
            if current.value == value: 
                new_node = Node(new_value)

                new_node.prev = current
                new_node.next = current.next
                
                current.next = new_node
                return
            current = current.next

        print(f' value {value} does not exist in the list')


    def add_before_value(self, value, new_value):
        
        current = self.head
        count = 0

        # if target is first in list
        if current.value == value:
            new_node = Node(new_value)
            prev_node = current.prev
            new_node.next = current
            new_node.prev = prev_node
            self.head = new_node
            return

        # current is target insert value
        # current.next is value after 

        while current.next is not None:
            if current.next.value == value:
                new_node = Node(new_value)
                orig_current_next = current.next  # pointer to rest of list
                prev_node = current.prev
                current.next = new_node

                new_node.next = orig_current_next
                new_node.prev = prev_node
                return
            current = current.next

        print(f' value {value} does not exist in the list')    


    def add_before_value_2(self, value, new_value):

        current = self.head

        # find value
        while current is not None:
            if current.value == value:
                break
            current = current.next

        if current is None:
            print(f'value {value} is not in the list')
        else:
            new_node = Node(new_value)
            new_node.next = current
            new_node.prev = current.prev

            # if target value is NOT first item in list 
            if current.prev is not None:
                current.prev.next = new_node
            else:
                # target value is first item in list
                self.head = new_node
                # return    


    def print(self):
        current = self.head
        list_str = 'HEAD >> '

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





# dbl_ll_1 = DoubleLinkedList()

# dbl_ll_1.add_to_tail_2(1)
# dbl_ll_1.print()
# dbl_ll_1.add_to_tail_2(2)
# dbl_ll_1.add_to_tail_2(3)
# dbl_ll_1.print()

# dbl_ll_1.add_to_head_2(3)
# dbl_ll_1.print()  # HEAD >> 3 ->  TAIL
# dbl_ll_1.add_to_head_2(2)
# dbl_ll_1.add_to_head_2(1)
# dbl_ll_1.print() # HEAD >> 1 -> 2 -> 3 ->  TAIL


# # dbl_ll_1.add_after_value(1000, 999)   # value 1000 does not exist in list


# # dbl_ll_1.add_to_head(3)
# # dbl_ll_1.print()   # HEAD >> 3 ->  TAIL

# # dbl_ll_1.add_to_head(2)
# # dbl_ll_1.add_to_head(1)
# # dbl_ll_1.print()   # HEAD >> 1 -> 2 -> 3 ->  TAIL


# dbl_ll_1.add_to_tail(10)
# dbl_ll_1.print()   # HEAD >> 10 ->  TAIL

# dbl_ll_1.add_to_tail(11)
# dbl_ll_1.print()   # HEAD >> 10 -> 11 ->  TAIL 

# dbl_ll_1.add_to_tail(12)
# dbl_ll_1.add_to_tail(13)
# dbl_ll_1.print()   # HEAD >> 10 -> 11 -> 12 -> 13 ->  TAIL 


# # dbl_ll_1.add_after_value(10, 999)
# # dbl_ll_1.print()   # HEAD >> 10 -> 11 -> 12 -> 13 -> 999 ->  TAIL
# # dbl_ll_1.add_after_value(1000, 999)   # value 1000 does not exist in list

# dbl_ll_1.add_before_value_2(11, 999)
# dbl_ll_1.print()
