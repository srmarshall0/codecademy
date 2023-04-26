# build a binary tree
def build_bst(my_list):
    if len(my_list) == 0:
        print("No Child")
    else:
        middle_index = len(my_list) // 2
        middle_value = my_list[middle_index]

        tree_node = {"data": middle_value}
        tree_node["right_child"] = build_bst(my_list[:middle_index])
        tree_node["left_child"]  = build_bst(my_list[middle_index + 1:])

        return tree_node

# define a binary search tree
class BinarySearchTree:
    def __init__(self, value, depth = 1):
        self.value = value 
        self.depth = depth
        self.left  = None
        self.right = None

    def insert(self, value):
        if (value < self.value):
            if (self.left is None):
                self.left = BinarySearchTree(value, self.depth + 1)
            else:
                self.left.insert(value)
        else:
            if(self.right is None):
                self.right = BinarySearchTree(value, self.depth + 1 )
            else:
                self.left.insert(value)

    def get_node_by_value(self, value):
        if value == self.value:
            return self 
        elif value < self.value and self.left:
            return self.left.get_node_by_value(value)
        elif value > self.value and self.right:
            return self.right.get_node_by_value(value)
        else:
            return None

    def depth_first_traversal(self):
        if self.left is not None:
            self.left.depth_first_traversal()
        if self.right is not None:
            self.right.depth_first_traversal()
            
        
