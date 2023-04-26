# import helper structures 
from linked_lists import Node

# build a tree 
class TreeNode:
    def __init__(self, value):
        self.value    = value
        self.children = []
        
    # # create a visual representation of the tree structure to be printed to console
    # def __str__(self):
    #     stack = deque() ## SM - how to build thisl
    #     stack.append([self, 0])
    #     level_str = "\n"
    #     while len(stack) > 0:
    #         node, level = stack.pop()

    #         if level > 0:
    #             level_str += "| "*(level-1)+ "|-"
    #         level_str += str(node.value)
    #         level_str += "\n"
    #         level += 1

    #         for child in reversed(node.children):
    #             stack.append([child, level])
        
    #     return level_str

# initialize a BFS function
def bfs(root_node, goal_value):
    path_queue = dequeue()
    