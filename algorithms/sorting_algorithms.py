# import assisting functions 
from random import randrange

# bubble sort
def bubble_sort(input):
    for index in range(len(input)):
        for i in range(len(input) -1 - index):
            if input[i] > input[i + 1]:
                input [i], input[i + 1] = input [i + 1], input[i]
                

# test bubble sort 
# nums = [5, 2, 9, 1, 5, 6]
# print("Pre-Sort: {0}".format(nums))      
# bubble_sort(nums)
# print("Post-Sort: {0}".format(nums))

# merge sort 
def merge_sort(items):
    if len(items) <= 1:
        return items 

    middle_index = len(items) // 2
    left_split  = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)

def merge(left, right):

    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if left:
        result += left
    if right:
        resutl += right

    return result 

# test merge_sort
# unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
# unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
# unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

# ordered_list1 = merge_sort(unordered_list1)
# ordered_list2 = merge_sort(unordered_list2)
# ordered_list3 = merge_sort(unordered_list3)

# quicksort 
def quicksort(list, start, end):
    if start >= end:
        return list 

    pivot_index = randrange(start, end)
    pivot_value = list[pivot_index]
    list[end], list[pivot_index] = list[pivot_index], list[end]

    less_than = start
    for i in range(start, end):
        if list[i] < pivot_value:
            list[less_than], list[i] = list[i], list[less_than]
            less_than += 1

    list[end], list[less_than] = list[less_than], list[end]

    quicksort(list, start, less_than -1)
    quicksort(list, less_than + 1 , end)
  
    
# test quicksort 
my_list = [42, 103, 22]
print("BEFORE: ", my_list)
sorted_list = quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", sorted_list)


#


