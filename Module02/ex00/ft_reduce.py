def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    try:
        iter(iterable)
        if len(iterable) == 1:
            return None
        res = iterable[0]
        for it in iterable[1:]:
            res = function_to_apply(res, it)
        return res
    except TypeError:
        sys.stderr.write("TypeError: {0} object is not iterable\n"
                         .format(type(iterable)))
        return None
