def sum_array(array):
    """Return sum of all items in array.
    
    Parameters
    ----------
    
    array: list
        list or array-like object containing numerical values.
    
    
    Returns
    -------
    
    int: int
        sum of all elements contained within the array.

    Examples
    -------
        >>> sum_array((0))
        0

        >>> sum_array((1, 2, 3))
        6
    """
    
    if len(array)==0: # base case
        return 0 
    
    else:
        return array[0] + sum_array(array[1:]) # recurse first value added to sum_array for second value

def fibonacci(n):
    
    """Return nth term in fibonacci sequence
    
    Parameters
    ----------
    n: int
        nth term in fibonacci sequence to calculate
    
    Returns
    -------  
    int: int
        nth term of fibonacci sequence,
            equal to sum of previous two terms

    
    Examples
    -------
        >>> fibonacci(1)
        1        
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    """

    if n <= 1:
        return n # base case

    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # recurse sum of preceding two terms get nth term value

def factorial(n):
    
    """Return n factoral (n!)
    
    Parameters
    ----------
    n: int
        a positive integer.
    
    Returns
    -------  
    int: int
        the factoral of the given positive integer

    Examples
    -------
        >>> factorial(1)
        1
        >>> factorial(5)
        120
    """

    if n == 0:
        return 1 # base case 1
    
    elif n == 1:
        return n # base case 2
    
    elif:
        return n*factorial(n-1) # recurse the factorial of the term minus one times the term itself


def reverse(word):
    
    """Return a word in reverse
    
    Parameters
    ----------
    word: string
        a word containing letters.
    
    Returns
    -------  
    str: str
        the word inputted in reverse order
    

    Examples
    -------
        >>> reverse('hello')
        'olleh'
        >>> reverse('world')
        'dlrow'
    """

    if len(word) == 0: # base case
        return word

    else:
        return reverse(word[1:]) + word[0] # recurse all but the first letter of the word and sum this with the first letter of the word