def insertion_sort(list_to_sort): # ITERATIVE SOLUTION 
    # the first element is already in the "sorted side"
    # (abstract idea, no code required)
     
    # for all other items, we should do things
    # starting at the second item, iterate until the end of the array
    for i in range(1, len(list_to_sort)): 
        # the current number at the index represents the value currently being sorted
        current_num = list_to_sort[i]
        # move the current number back through the array ( to the "sorted side" )
        j = i
        # keep moving until: its greater than the number before it OR we reach the start of array
        while j > 0 and current_num < list_to_sort[j-1]: 
            # replace the current value with the one to left of it
            list_to_sort[j] = list_to_sort[j-1] # SWAP
            j -= 1 # decrement j as we go through the array
        # set the value at the current index to the current number
        # at this moment, J represents the new location for the current number
        list_to_sort[j] = current_num

    return list_to_sort

print(insertion_sort([8, 4, 2, 5, 1, 3]))


# This is O(n^2) because the while loop can run n times within the for loop for n times. 