import doctest

def split_and_join(line):
    """
    >>> split_and_join("this is a string")
    'this-is-a-string'
    """

    result = ""
    _s = line.split(" ")
    _s = "-".join(w for w in _s)
    result = _s
    return result


doctest.testmod()