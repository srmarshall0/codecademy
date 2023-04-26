# write move to end function 
def move_to_end(lst, val):
    # initalize empty list to hold results 
    result = []
    # set base case --> retrun result once the length of result is 0 
    if len(lst) == 0:
        return result 
    # define the case when the first item in the list matches the value were lookng for
    if lst[0] == val:
        # add everything but the first item of LST to RESULT --> the first item being spliced off is being moved to the end 
        result += move_to_end(lst[1:], val)
        # now add the first item of lst to result becase it matched the value were searching for 
        result.append(lst[0])
    # if the first item of the list doesnt match
    else:
        # add the first entry to the begiing of the list BEFORE you append the spliced list to the reuslt --> adds to begining vs end
        result.append(lst[0])
        result += move_to_end(lst[1:], val)

    return result 
