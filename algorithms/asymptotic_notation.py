# import necessary data structures 
from linked_lists import LinkedList

# find the maximum of a linked list 
def find_max(linked_list):
    current_node = linked_list.get_head_node()
    max_value = current_node
    while linked_list.get_next_node():
        current_node = current_node.get_next_node()
        value = current_node.get_value()
        if max_value < value:
            max_value = value
    return max_value

# sort a linked list -- sorted descending 
def sort_linked_lsit(linked_list):
    sorted_list = LinkedList()
    while linked_list.get_head_node():
        max_value = find_max(linked_list)
        sorted_list.insert_begining(max_value)
        linked_list.remove_node(max_value)
    return sorted_list

# traverse a linked list where nodes consist of 2 values 
# search for a a key value in position 0 and return the corresponding value at position 1
my_linked_list = LinkedList()

traverse = my_linked_list.get_head_node()
while traverse.get_value()[0] != "key_value_p0":
    traverse = traverse.get_next_node()
key_value_p1 = traverse.get_value()[1]

