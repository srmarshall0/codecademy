# define a binary search algorithm 
def binary_search(sorted_list, target_value):
    
    if not sorted_list:
        return "value not found"
    
    middle_index = len(sorted_list)//2
    middle_value = sorted_list[middle_index]

    if middle_value == target_value:
        return middle_index

    if middle_value > target_value:
        left_half = sorted_list[ :middle_index]
        return binary_search(right_half, target_value)

    if middle_value < target_value:
        right_half = sorted_list[middle_index + 1: ]
        result = binary_search(right_half, target_value)
        if result == "value not found":
            return result
        else:
            return middle_index + result

# implement a solution using two pointers 
def binary_search(sorted_list, left_pointer, right_pointer, target_value):

    # define a condition that tells us weve reached an empty sublist
    if left_pointer >= right_pointer:
        return "value not found"

    # calculate middle index using pointer location 
    middle_index = (left_pointer + right_pointer)//2
    middle_value = sorted_list[middle_index]

    # define conditions 
    if middle_value == target_value:
        return middle_index

    if middle_value > target_value:
        # overwrite the right pointer to equal the middle pointer
        return binary_search(sorted_list, left_pointer, middle_index, target_value)

    if middle_value < target_value:
        # overwrite the left pointer to equal the middle pointer + 1
        return binary_search(sorted_list, middle_index + 1, right_pointer, target_value)
    




