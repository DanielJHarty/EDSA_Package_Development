def bubble_sort(items):
    
    """ the bubble sort algorithm takes in an unsorted list of numbers.
    returns a list in ascending order.

    Parameters
    ----------
    items : list
        list of unordered numbers

    Returns
    -------
    list
        list of elements in items in ascending order

    Examples
    -------
        >>> bubble_sort([1])
        1
        
        >>> bubble_sort([54,26,93,17,77,31,44,55,20])
        [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """

    for j in range(len(items)-1):

        try:
            if items[j] > items[j+1]:  # if item 1 is bigger than next item 2
                items[j], items[j+1] = items[j+1], items[j]  # swap them
                bubble_sort(items) #recurse swapped items to bubble_sort function
                
        except IndexError: # when index does not match
            pass
        
    return items

def merge_sort(items):
    
    """ the merge sort algorithm takes in an unsorted list of numbers.
    returns a list in ascending order.

    Parameters
    ----------
    items : list
        list of unordered numbers

    Returns
    -------
    list
        list of elements in items in ascending order
    """
    def merge(left, right):
        '''
        Merge sort merging function.
        
        '''

        left_index, right_index = 0, 0
        result = []
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result += left[left_index:]
        result += right[right_index:]
        return result    

    if len(items) <= 1:  # base case
        return items

    # divide array in half and merge sort recursively
    half = len(items) // 2
    left = merge_sort(items[:half])
    right = merge_sort(items[half:])

    return merge(left, right)

def quick_sort(items):
    
    """ the quick sort algorithm takes in an unsorted list of numbers.
    returns a list in ascending order.

    Parameters
    ----------
    items : list
        list of unordered numbers

    Returns
    -------
    list
        list of elements in items in ascending order
    
    Examples
    -------
        >>> bubble_sort([1])
            1
            
        >>> bubble_sort([54,26,93,17,77,31,44,55,20])
            [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    
    if len(items) == 0: # base case
        return items

    # divide array in half and quick sort recursively
    p = len(items) // 2 
    s = [i for i in items if i < items[p]] # small list
    d = [i for i in items if i == items[p]] # duplicate list
    l = [i for i in items if i > items[p]] # large list

    return quick_sort(s) + d + quick_sort(l)