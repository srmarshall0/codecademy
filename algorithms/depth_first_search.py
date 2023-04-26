# define tree node class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return self.value

    def add_children(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)
    
    def remove_child(self, child_node):
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children if child is not child_node]

    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

# define depth first search function using recursion 
def depth_first_search(root, target, path = ()):

    path = path + (root, )

    if root.value == target:
        return path
    for child in root.children:
        path_found = depth_first_search(child, target, path)
        if path_found is not None:
            return path_found
    return None