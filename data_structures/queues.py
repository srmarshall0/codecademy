# create a node class
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    def set_next_node(self, next):
        self.next = next
    def get_next_node(self):
        return self.next
    def get_value(self):
        return self.value
    
# create a queue class
class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
    def peek(self):
        if self.size == 0:
            print("Queue is empty")
        else:
            return self.head
    def get_size(self):
        return self.size
    def has_space(self):
        if self.max_size == None:
            return True
        else:
          return self.size < self.max_size
    def is_empty(self):
        return self.size == 0
    def enqueue(self, new_value):
        if self.has_space():
            node_to_add = Node(new_value)
            if self.is_empty():
                self.head = self.tail = node_to_add
            else:
                self.tail.set_next_node(node_to_add)
                self.tail = node_to_add
            self.size += 1
        print("Queue overflow -- No more space in queue")
    def dequeue(self):
        # remove from an empty queue
        if self.is_empty() == False:
            node_to_remove = self.head
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
        else:
            print("Queue underflow -- Cannot remove node from an empty queue")