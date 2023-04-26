# define a linear search function 
def linear_search(search_list, target_value):
    for i in range(len(search_list)):
        if search_list[i] == target_value:
            return i 
    raise ValueError("{0} not in list".format(target_value))

# define a de-duping algorithm using linear search 
def find_duplicates(search_list, target_value):
    matches = []
    for i in range(len(search_list, target_value)):
        if search_list[i] == target_value:
            matches.append(i)
    if matches:
        return matches
    else:
        raise ValueError("{0} not in list".format(target_value))

# finding a maximum value
def find_max(search_list):
    max_value_index = None
    for i in range(len(search_list)):
        if search_list[i] > search_list[max_value_index] or max_value_index is None:
            max_value = search_list[i]
    return max_value