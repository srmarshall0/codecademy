# recursive FACTORIAL
def recursive_factorial(n):
    if n < 0:
        ValueError("Inputs 0 or greater only")
    if n <= 1:
        return 1
    return n*recursive_factorial(n-1)

# test function 
print(recursive_factorial(3))

# iterative FACTORIAL -- contiges on the communicative property ... the order in which you multily make no different 
def iterative_factorial(n):
    # define case to reject negative inputs
    if n < 0:
        ValueError("Inputs 0 or greater only")
    # set base counter -- tells python where to begin
    result = 1
    # set condition for iteration
    while n != 0:
        # overwirte the current value of result by multiplying by the current number
        result = result * n 
        n -= 1
    return result 

# test function 
print(iterative_factorial(3))

# recursive FIBONACCI
def recursive_fibonacci(n):
    if n < 0:
        ValueError("Inputs 0 or greater only")
    if n <= 1: 
        return 1 
    return recursive_fibonacci(n-2) + recursive_fibonacci(n-1)

# iterative FIBONACCI
def iterative_fibonacci(n):
    if n < 0:
        ValueError("Inputs 0 or greater only")
    # initiate a list with the base 2 fibonacci numbers
    my_list = [0,1]
    # instruct what to do if the requested index is shorter than the length of the list -- number is already in the list 
    if n <= len(my_list) -1:
        return my_list[n]
    # add to fibonacci list UNTIL the list contains the index were interested in 
    while n > len(my_list) -1:
        next_item = my_list[-1] + my_list[-2]
        my_list.append(next_item)
    return my_list[n]


# sum digits ITERATIVE
def iterative_sum_digits(n):
    if n < 0:
        ValueError("Inputs 0 or greater only")
    # initiate value for reuslt 
    result = 0
    # define case in which to stop 
    while n is not 0:
        # obtain the last number of n 
        result += n % 10 
        # generate the new input (one digit shorter than prior) for the next iteration
        n = n//10
    # after round down division completes and were at 0, we have summed all numbers because reuslt is being updated each loop
    return result + n

# sum digits RECURSIVE
def recursive_sum_digits(n):
    # define ValueError
    if n < 0:
        ValueError("Inputs 0 or greater only")
    # define case for single digit numbers -- no summation needed
    if n <= 9:
        return n    
    # compute final number in the series 
    last_digit = n % 10
    # use a recursive call to sum the additional numbers 
    return(recursive_sum_digits(n//10) + last_digit)

# minimum value ITERATIVE
def iterative_find_min(my_list):
    # set blank var 
    min = None
    # loop though the list to find the minimum
    for element in my_list:
        # if the element isnt already stored as the min OR the element is less than the current min -- overwrite
        if not min or (element < min):
            min = element 
    # at the end of the list -- return min value
    return min 

# minimum value RECURSIVE
def recursive_find_min(my_list, min = None):
    # if the input is not my list return nothing
    if not my_list:
        return min
    # if the input is as expected and the first entry of the list is less than the current minimum 
    if not min or my_list[0] < min:
        # assign minimum value
        min = my_list[0]
    # if the value isnt less than the current minimum, repeat the function again, but truncate the list and feed in the new minimum
    return recursive_find_min(my_list[1:], min)

# valid palindrome ITERATIVE
def iterative_is_palindrome(my_string):
    while len(my_string) != 0:
        if my_string[0] != my_string[-1]:
            return False 
        my_string = my_string[1:]

# valid palindrome RECURSIVE
def recursive_palindrome(str):
  if len(str) < 2:
    return True
  if str[0] != str[-1]:
    return False
  return recursive_palindrome(str[1:-1])

# multiplication ITERATIVE
def iterative_multiplication(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result

# multiplaction RECURSIVE
def recursive_mulitplication(num_1, num_2):
    if num_1 == 0 or num_2 == 0:
        return 0
    return num_1 + recursive_mulitplication(num_1, num_2-1)

# find tree depth ITERATIVE
def iterative_depth(tree):
  result = 0
  # our "queue" will store nodes at each level
  queue = [tree]
  # loop as long as there are nodes to explore
  while queue:
    # count the number of child nodes
    level_count = len(queue)
    for child_count in range(0, level_count):
      # loop through each child
      child = queue.pop(0)
     # add its children if they exist
      if child["left_child"]:
        queue.append(child["left_child"])
      if child["right_child"]:
        queue.append(child["right_child"])
    # count the level
    result += 1
  return result

# find tree depth RECURSIVE
def recursive_depth(tree):
    if not tree:
        return 0  
    left_depth = recursive_depth(tree["left_child"])
    right_depth = recursive_depth(tree["right_child"])
    if left_depth > right_depth:
        return left_depth + 1
        
    else:
        return right_depth + 1