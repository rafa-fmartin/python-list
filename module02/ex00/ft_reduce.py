def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError

    it = iter(iterable)
    try:
        current_element = next(it)
    except StopIteration:
        raise TypeError
    
    for item in it:
        current_element = function_to_apply(current_element, item)
        
    return current_element
