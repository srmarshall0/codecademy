from linked_lists import Node, LinkedList

class Stack:
    def __init__(self, limit = 1000):
        self.top_item = None
        self.limit = limit
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def has_space(self):
        return self.size < self.limit
    def push(self, value):
        if self.has_space():
            item_to_add = Node(value)
            item_to_add.set_next_node(self.top_item)
            self.top_item = item_to_add
            self.size += 1
        else:
            print("Stack overflow - No more space!")
    def pop(self):
        if self.is_empty():
            print("Stack underflow - No items to remove!")
        else:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
    def peek(self):
        return self.top_item.get_value()