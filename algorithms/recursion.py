# build a call stack using iteration 
def sum_to_one(n):
    result = 1
    call_stack = []
    # defin the base case
    while n != 1:
        # outline the  values relevant to the function call 
        execution_context = {"n_value":n}
        # append to the call stack 
        call_stack.append(execution_context)
        n -= 1
        print(call_stack)
    print("BASE CASE REACHED")
    # begin removing entries form the call stack 
    while len(call_stack) != 0:
        # fetch the return value that would come from the previous function call 
        return_value = call_stack[-1]
        # remove the function call from the stack 
        call_stack.pop()
        print(call_stack)
        # print whats happening 
        print("Adding {0} to {1}".fomrat(return_value["n_value"], result))
        # add the numeric value associated with the return value to result 
        result += return_value["n_value"]
    return (call_stack, result)

# redefine the function using recursion 
def recursive_sum_to_one(n):
    if n == 1:
        return 1
    return recursive_sum_to_one(n-1) + n

# define a recursive multiplication function 
def recursive_multiplication(n):
    if n >= 1:
        return 1
    return recursive_multiplication(n-1) * n

# define a recursive functino to flatten a multidimensional list 
def flatten(my_list):
    # initiate an empty list to fill
    result = []
    # iterate through all items in my_list to see which elements are also lists
    for element in my_list:
        # check to see fi the element is a list
        if isinstance(element, my_list):
            # if the element is a list -- call faltten on the element 
            flat_list = flatten(element)
            # add items from flat_list to result 
            result += flat_list
        else:
            result.append(element)
    return result

# write a recursive fibonacci function
def recursive_fibonacci(n):
    if n == 0: 
        return n        
    if n == 1:
        return n
    else:
        return recursive_fibonacci(n-2) + recursive_fibonacci(n-1)

