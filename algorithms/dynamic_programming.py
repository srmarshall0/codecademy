# write a memorized version of the recursive fibonacci solution

# initate a memory dictionary 
memo = {}

# define new fibonacci function
def fibonacci_memo(num):
    answer = None
    if num in memo:
        answer = memo[num]
    elif num == 1 or num == 0:
        answer = num
    else:
        answer = fibonacci_memo(num - 2) + fibonacci_memo(num - 1)
        memo[num] = answer
    return answer

# longest common subsequence 
# test variables
dna_1 = "ACCGTT"
dna_2 = "CCAGCA"

# define grid print 
def print_grid(grid):
    for row_line in grid:
        print(row_line)

# define function 
def longest_common_subserquence(string_1, string_2):
    
    print("Finding longest common subsequence of {0} and {1}".format(string_1, string_2))
    
    # create a grid
    grid = [[0 for letter1 in range(len(string_1) + 1)] for letter2 in range(len(string_2) + 1)]

    # print starting grid
    print_grid(grid)
    
    # loop over grid
    for row in range(1, len(string_2) + 1):
        print("Comparing: {0}".format(string_2[row-1]))

        for col in range(1, len(string_1) + 1):

            print("Against: {0}".format(string_1[col-1]))
            
            if string_1[col-1] == string_2[col-1]:
                grid[row][col] = grid[row -1][col-1] + 1
                # print_grid(grid)
            
            else:
                grid[row][col] = max(grid[row-1][col], grid[row][col-1])
                # print_grid(grid)

    # retrieve and return the result
    result = []
    while row > 0 and col > 0:
        if string_1[col -1] == string_2[row -1]:
            result.append(string_1[col-1])
            col -= 1
            row -= 1
        elif grid[row-1][col] > grid[row][col-1]:
            row -= 1
        else:
            col -= 1
    result.reverse()
    print("Longest common subsequence is '{0}'".format("".join(result)))

    # print grid
    # for row_line in grid:
    #     print(row_line)
    

# test
longest_common_subserquence(dna_1, dna_2)