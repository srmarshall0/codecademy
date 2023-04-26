class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    ## DEFINE HELPER FUNCTIONS ##
    def parent_index(self, index):
        return index // 2
    # parent and child indecies follow a formula
    def left_child_index(self, index):
        return index * 2
    def right_child_index(self, index):
        return index * 2 + 1

    def child_present(self, index):
        return self.left_child_index(index) <= self.count

    ## DEFINE PRIMARY HEAP FUNCTIONS ## 
    
    # define a fucntion to add to the heap
    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    # define method to get larger childs index
    def get_larger_child_index(self, index):

        # check to see if there is a left child present
        if self.right_child_index(index) > self.count:
            return self.left_child_index(index)
        else:
            left_child = self.heap_list[self.left_child_index(index)]
            right_child = self.heap_list[self.right_child_index(index)]
            if left_child > right_child:
                return self.left_child_index(index)
            else:
                return self.right_child_index(index)

    # define heapify up function
    def heapify_up(self):
        index = self.count
        while self.parent_index(index) > 0:
            child = self.heap_list[index]
            parent = self.heap_list[self.parent_index(index)]
            if parent > child:
                self.heap_list[index] = parent
                self.heap_list[self.parent_index(index)] = child
            index = self.parent_index(index) 

    # define heapify down function 
    def heapify_down(self):
        index = 1
        while self.child_present(index):

            # define helper variables 
            larger_child_index = self.get_larger_child_index(index)
            child = self.heap_list[larger_child_index]
            parent = self.heap_list[index]

            # make comparison to determine what needs to move 
            if parent < child:
                self.heap_list[index] = child
                self.heap_list[larger_child_index] = parent
            
            # reset index to continue moving through the heap
            index = larger_child_index

    # define a function to retrieve the max value of the heap
    def retrieve_max(self):
        if self.count == 0:
            return None
        # by design, max heap values are the ROOT of the heap and will be stored at index 1
        max_value = self.heap_list[1] 
        # replace the first value of the heap with the last value in the heap
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        # heapify down to restore heap 
        self.heapify_down()
        return max_value
    
    # define a heapsort function 
    def heapsort(list):
        sort = []
        max_heap = MaxHeap()
        for index in list:
            max_heap.add(index)
        while max_heap.count > 0:
            max_value = max_heap.retrieve_max()
            sort.insert(0, max_value)
        return sort

    
        

