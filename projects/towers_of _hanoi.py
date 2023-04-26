# build stacks for the game 
from linked_lists import Node

class HanoiStacks:
    def __init__(self, name):
        self.size = 0
        self.top_item = None
        self.limit = 1000
        self.name = name

    # define helper methods:
    def has_space(self):
        return self.limit > self.size
    
    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
    
    def get_name(self):
        return self.name

    def print_items(self):
        pointer = self.top_item
        print_list = []
        while (pointer):
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        print_list.reverse()
        print("{0} Stack: {1}".format(self.get_name(), print_list))
    
    # deifne core 3 methods 
    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("No space in this stack")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -=1 
            return item_to_remove.get_value()
        else:
            print("This stack is already empty")
    
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("This stack is totally empty")
        


# start initialization message 
print("\nLet's play Towers of Hanoi!")

# create 3 towers 
stacks = []

left_stack = HanoiStacks("Left")
middle_stack = HanoiStacks("Middle")
right_stack = HanoiStacks("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# create game disks 
num_disks = int(input("\nHow many disks would you like to play with?\n"))

# make sure that num_disks always exceeds 3
while num_disks < 3:
    num_disks = int(input("\nEnter a number greater than or equal to 3\n"))

# create disks using a for loop 
for i in range(num_disks, 0, -1):

    # place the last disk on the left stack 
    left_stack.push(i)

# find optimal number of moves and display
num_optimal_moves = 2 ** num_disks -1

print("\nThe fastest you can solve this game in in {0} moves".format(num_optimal_moves))

# define user inputs 
def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            print("To select the {0} stack, type {1}".format(name, name[0]))
    
        user_input = input("")

        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]
        else:
            print("\nThat was not a valid choice, please make a selection form the list above.\n")

# write code to play the game 
num_user_moves = 0

while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")
    for i in range(len(stacks)):
        stacks[i].print_items()

    # ask player what move they would like to make
    while True:
        print("\nWhich stack do you wnat to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        # run move validation 
        if from_stack.get_size() == 0:
            print("\n\nInvalid Move. Try Again")

        elif (to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek()):
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break

        else:
            print("\n\nInvalid Move. Try Agian")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))
