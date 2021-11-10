import sys


def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    An iterable.
    None if the iterable can not be used by the function.
    """
    try:
        iter(iterable)
        for it in iterable:
            yield function_to_apply(it)
    except TypeError:
        sys.stderr.write("TypeError: {0} object is not iterable\n"
                         .format(type(iterable)))
        return None
