def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration'''

    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2

        mid_element = array[mid_element]

        if target == mid_element:
            return mid_index

        elif target < mid_element:
            end_index = mid_element - 1

        else:
            start_index = mid_element + 1

    return -1


################################ Recursive Solution ######################################

def binary_search_recursive(array, target):
    '''Write a function that implements the binary search algorithm using recursion'''
    return binary_search_recursive_soln(array, target, 0, len(array)-1)


def binary_search_recursive_soln(array, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_element

    elif target < mid_element:
        return binary_search_recursive_soln(array, target, start_index, mid_index-1)

    else:
        return binary_search_recursive_soln(array, target, mid_index+1, end_index)

################################### Variation on Binary Search ###############################


def recursive_binary_search(target, source, left=0):

    if len(source) == 0:
        return None

    center = (len(source)-1) // 2

    if source[center] == target:
        return center + left

    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)

    else:
        recursive_binary_search(target, source[:center], left)

####################################### find first ##############################################


def find_first(target, source):

    index = recursive_binary_search(target, source)

    if not index:
        return -1

    while source[index] == target:
        if index == 0:
            return 0

        if source[index-1] == target:
            index -= 1

        else:
            return index

#################################### Contains #####################################################


def contains(target, source):
    return recursive_binary_search(target, source) is not None


################################### First and Last Indexes ########################################

def first_and_last_index(arr, number):
    # search first occurence
    first_index = find_start_index(arr, number, 0, len(arr)-1)

    # search last occurence
    last_index = find_end_index(arr, number, 0, len(arr)-1)

    return [first_index, last_index]


def find_start_index(arr, number, start_index, end_index):
    # binary search solution to search for the first index of the array
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index)//2

    if arr[mid_index] == number:
        current_start_pos = find_start_index(
            arr, number, start_index, mid_index-1)
        if current_start_pos != -1:
            start_pos = current_start_pos
        else:
            start_pos = mid_index
        return start_pos

    elif arr[mid_index] < number:
        return find_start_index(arr, number, mid_index+1, end_index)

    else:
        return find_start_index(arr, number, start_index, end_index-1)


def find_end_index(arr, number, start_index, end_index):
    # binary search solution to search for the last index of the array
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index)//2

    if arr[mid_index] == number:
        current_end_pos = find_end_index(arr, number, mid_index+1, end_index)
        if current_end_pos != -1:
            end_pos = current_end_pos
        else:
            end_pos = mid_index
        return end_pos

    elif arr[mid_index] < number:
        return find_end_index(arr, number, mid_index+1, end_index)

    else:
        return find_end_index(arr, number, start_index, end_index-1)
