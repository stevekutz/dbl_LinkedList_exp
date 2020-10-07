class Node:
    def __init__(self, value, prev = None, next = None ):
        self.value = value
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):

        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next    

        print(f' length is {count}')
        return count

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
        if current is not None:
            current.prev = new_node
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
        new_node = None

        while current is not None:
            if current.value == value: 
                new_node = Node(new_value)
                
                new_node.next = current.next
                new_node.prev = current
                
                next_node = current.next

                # check if next_node is last node
                if next_node is not None:
                    next_node.prev = new_node

                current.next = new_node
                break
            current = current.next

        if new_node is None:
            print(f' value {value} does not exist in the list')


    def add_before_value(self, value, new_value):
        
        current = self.head
        new_node = Node(new_value)
        prev_node = current.prev
        count = 0

        # if target is first in list
        if current.value == value:
            current.prev = new_node
            new_node.next = current
            new_node.prev = prev_node
            self.head = new_node
            return

        # current is target insert value
        # current.next is value after 

        while current.next is not None:
            if current.next.value == value:
                next_node = current.next  # pointer to rest of list
                if next_node is not None:
                    next_node.prev = new_node
                    
                prev_node = current.prev
                current.next = new_node

                new_node.next = next_node
                new_node.prev = current
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
            print(f' current.value {current.value}')
            new_node = Node(new_value)
            new_node.next = current
            new_node.prev = current.prev

            # if target value is NOT first item in list 
            if current.prev is not None:
                current.prev.next = new_node
                current.prev = new_node
            else:
                # target value is first item in list
                self.head = new_node
                current.prev = new_node  

    def add_list(self,list_vals):

        for item in list_vals:
            self.add_to_tail_2(item)


    def remove_by_index(self, index):

        current = self.head
        ind = 0
        prev_node = None


        while current is not None:
            if ind  == index:
                break
            ind += 1
            prev_node = current
            current = current.next

        if index < 0 or index > ind:
            print(f' !!! index out of bounds')
            raise Exception("Error: index out of bounds of list indices")
                
        if prev_node is None:
            self.head = current.next
            self.head.prev = None
  
        else:
            prev_node.next = current.next
            after_node = current.next
            if after_node is not None:
                after_node.prev = prev_node
            # prev_node.prev = prev_node
            print(f' current.value  {current.value} ')
            print(f'prev_node.value  {prev_node.value}')


    def reverse_list(self):

        current = self.head
        temp = None


        if current is None:
            print(f' list is empty')
            return

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
            if temp is not None:
                self.head = temp.prev


    def convert_to_circular(self):
        current = self.head
        orig_head = self.head

        if current is None:
            print(f' list is empty')

        # loop to end connect first and last nodes
        while current is not None:
            if current.next is None:
                current.next = orig_head
                orig_head.prev = current
                break   
            current = current.next    

    def detect_circular(self):
        current = self.head

        addr_set = set()


        if current.prev is not None:
            addr_set.add(current)
            if current.value == current.prev.next.value:
                print(f' loop detected , last node before loop {current.prev.value}')
                return True

        print(f' Not a Circular Double Linked List')
        return False        

    def remove_circular(self):

        current = self.head

        if current.prev is not None:
            current.prev.next = None
            current.prev = None
            return

        print(f' Not a Circular Double Linked List')
        return False
    

    def add_value_to_front_circular(self, new_value):
        if self.detect_circular():
            current = self.head
            last_p = current.prev

            new_node = Node(new_value)
            new_node.prev = last_p
            new_node.next = current
            current.prev = new_node

            last_p.next = new_node


            self.head = new_node



    def remove_by_value(self, value):
       
        current = self.head
        prev_node = None
        found = False

        while current is not None:
            # print(f' at START current value {current.value}')
            while current.value == value:
                if current.next is not None:
                    current = current.next
                elif current.value == 1 and current.next is None:
                    if prev_node is None:
                        self.head = None
                        return
                    else:    
                        prev_node.next = None
                        print(f' on last value')
                        return

            if prev_node is None:
                self.head = current
                current.prev = None
                prev_node = current
            else:
                prev_node.next = current
                current.prev = prev_node
                
            prev_node = current
            current = current.next

        if found is False:
            print(f' value {value} was not found in the list')
            return f' value {value} was not found in the list' 

    def print_circular(self):

        current = self.head
        addr_set = set()
        str_l = '==> HEAD >> '

        if self.detect_circular():

            while current not in addr_set:
                str_l += str(current.value) + ' -> '
                addr_set.add(current)
                current = current.next

        str_l +=  '===> ' + str(current.value)   
        print(f' {str_l}')
        return str_l

    def print_circular_reverse(self):
        
        current = None
        str_l = 'LAST >> '
        addr_set = set()

        if self.detect_circular():
            current = self.head.prev

            while current not in addr_set:
                addr_set.add(current)
                str_l += str(current.value) + ' => '
                current= current.prev

        str_l += '===>'  + str(current.value)
        print(f' {str_l}')
        return str_l





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

    def print_reverse(self):

        current = self.head
        list_str = 'TAIL >> '

        if current is None:
            print(f' Double Linked List is empty')
            return f' TAIL >>  HEAD'

        while current.next is not None:
            current = current.next

        # print(f' current.value   {current.value}')    
    
        while current is not None:
            list_str += str(current.value) + ' -> '
            current = current.prev

        list_str += ' HEAD'
        print(f'{list_str}')
        return list_str

my_list = [1, 1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 4, 1, 1, 1]# # 
# my_list = [3,2,5]
# my_list = [1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 4, 1, 1, 1]
# my_list = [4, 3, 2, 6]
# my_list = [1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 4, 1, 1, 1]
# # my_list = [2, 1]
# # my_list = [1, 1, 1, 1]

my_list = [1, 2, 3]
dbl_ll_1 = DoubleLinkedList()
dbl_ll_1.add_list(my_list)
# dbl_ll_1.add_to_head_2(3)
# dbl_ll_1.add_to_head_2(2)
# dbl_ll_1.add_to_head_2(1)
# dbl_ll_1.print()
# dbl_ll_1.remove_by_value (1)
dbl_ll_1.print()

# dbl_ll_1.print()
# dbl_ll_1.print_reverse()

# dbl_ll_1.print()   # HEAD >> 1 -> 2 -> 3 ->  TAIL
# dbl_ll_1.print_reverse()

# # dbl_ll_1.remove_by_value(1)
# # dbl_ll_1.print()

# my_list = [1, 2, 3]
# dbl_ll_1.add_list(my_list)
# dbl_ll_1.print()
# # # # dbl_ll_1.print_reverse()

# dbl_ll_1.remove_by_index(2)
# dbl_ll_1.print()   # HEAD >> 2 -> 3 ->  TAIL
# dbl_ll_1.print_reverse()

# # dbl_ll_1.remove_by_index(2)
# # dbl_ll_1.print()
  
# dbl_ll_1.add_to_tail_2(1)
# # dbl_ll_1.print()
# dbl_ll_1.add_to_tail_2(2)
# dbl_ll_1.add_to_tail_2(3)
# dbl_ll_1.print()
# dbl_ll_1.print_reverse()

# dbl_ll_1.add_to_head(3)
# dbl_ll_1.print()  # HEAD >> 3 ->  TAIL
# dbl_ll_1.add_to_head(2)
# dbl_ll_1.add_to_head(1)
# dbl_ll_1.print() # HEAD >> 1 -> 2 -> 3 ->  TAIL
# dbl_ll_1.print_reverse()

# dbl_ll_1.add_after_value(0, 999)
# dbl_ll_1.add_after_value(1, 999)   # value 1000 does not exist in list
# dbl_ll_1.add_after_value(2, 999)
# dbl_ll_1.add_after_value(3, 999)
# dbl_ll_1.add_after_value(4, 999)
# dbl_ll_1.add_after_value(1, 888)
# dbl_ll_1.print()
# dbl_ll_1.print_reverse()

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

# dbl_ll_1.add_before_value_2(1, 999)
# dbl_ll_1.print()
# dbl_ll_1.remove_by_value(1)
# dbl_ll_1.print()
# dbl_ll_1.print_reverse()
# dbl_ll_1.get_length()

# dbl_ll_1.print()
# dbl_ll_1.reverse_list()
# dbl_ll_1.print()
# dbl_ll_1.print_reverse()


dbl_ll_1.convert_to_circular()
dbl_ll_1.detect_circular()

dbl_ll_1.add_value_to_front_circular(100)

# dbl_ll_1.remove_circular()

print(f' @@@@@@@@ \n')
dbl_ll_1.detect_circular()
dbl_ll_1.print_circular()
dbl_ll_1.print_circular_reverse()